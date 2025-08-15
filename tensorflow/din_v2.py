# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2025-08-12 14:36
#    @Description   : 
#
# ===============================================================


import tensorflow as tf
from tensorflow import keras


class DINAttentionLayer(keras.layers.Layer):
    def __init__(self, hidden_units, activation='relu', dropout=0.0, l2_reg=1e-6, **kwargs):
        """
        DIN 的局部激活单元 (Local Activation Unit) 和加权求和池化。
        Args:
            units (int): 局部激活单元MLP中的隐藏层维度。
            activation(str): 激活函数, 论文中使用PRelu, 这里为了简单, 使用通用的relu
            dropout_rate (float): Dropout率。
            l2_reg (float): L2正则化系数。
        """
        super(DINAttentionLayer, self).__init__(**kwargs)
        self.hidden_units = hidden_units
        self.activation = activation
        self.dropout = dropout
        self.l2_reg = l2_reg

        # Local Activation Unit
        self.dense1 = keras.layers.Dense(
            units=self.hidden_units,
            activation=self.activation,
            kernel_regularizer=keras.regularizers.l2(self.l2_reg),
            name='attention_dense1'
        )
        if self.dropout > 0:
            self.dropout1 = keras.layers.Dropout(rate=self.dropout, name='attention_dropout1')

        self.dense2 = keras.layers.Dense(
            units=1,
            activation=None,
            kernel_regularizer=keras.regularizers.l2(self.l2_reg),
            name='attention_dense2'
        )

    def call(self, query, keys, mask=None, training=None):
        """

        Args:
            query (tf.Tensor): 候选物品Embedding,形状 (batch_size, embedding_dim)。
            keys (tf.Tensor): 用户历史行为Embedding序列,形状 (batch_size, max_seq_len, embedding_dim)。
            mask (tf.Tensor, optional): 历史行为序列的Padding Mask,形状 (batch_size, max_seq_len)。
                                        True 表示非填充,False表示填充。
            training (bool, optional): 是否处于训练模式,用于Dropout。
        Returns:
            tf.Tensor: 用户兴趣表示向量,形状 (batch_size, embedding_dim)。

        Returns:

        """
        # 获取序列长度和Embedding维度
        seq_len = tf.shape(keys)[1]
        embedding_dim = tf.shape(keys)[2]

        # 扩展query维度以匹配keys的序列维度
        # (batch_size, embedding_dim) -> (batch_size, 1, embedding_dim) -> (batch_size, seq_len, embedding_dim)
        query_tiled = tf.tile(tf.expand_dims(query, axis=1), [1, seq_len, 1])

        # 拼接输入特征
        combined = keras.layers.Concatenate()([
            query_tiled,
            keys,
            query_tiled * keys,
            query_tiled - keys
        ])  # (batch_size, seq_len, 4 * embedding_dim)

        # 将输入展平, 以便通过Dense层
        mlp_input = tf.reshape(combined, (-1, 4 * embedding_dim))  # (batch_size * seq_len, 4 * embedding_dim)

        hidden_state = self.dense1(mlp_input)  # (batch_size * seq_len, hidden_units)
        attention_weight = self.dense2(hidden_state)  # (batch_size * seq_len, 1)

        attention_weight = tf.reshape(attention_weight, (-1, seq_len, 1))

        # 应用Padding Mask到注意力分数上
        if mask is not None:
            # 将mask扩展到(batch_size, seq_len, 1)
            mask_expanded = tf.cast(tf.expand_dims(mask, axis=-1), tf.float32)
            # 将填充位置的分数置为0
            attention_weight = attention_weight * mask_expanded

        # 加权求和池化(weighted sum)
        # (batch_size, seq_len, embedding_dim) * (batch_size, seq_len, 1)
        weighted_keys = keys * attention_weight
        user_interested_embedding = tf.reduce_sum(weighted_keys, axis=1)  # (batch_size, embedding_dim)

        return user_interested_embedding

    def get_config(self):
        config = super(DINAttentionLayer, self).get_config()
        config.update({
            'hidden_units': self.hidden_units,
            'dropout': self.dropout,
            'l2_reg': self.l2_reg,
            'activation': self.activation
        })


if __name__ == '__main__':
    batch_size = 32
    seq_len = 10
    embedding_dim = 16
    hidden_units = 8

    query_emb = tf.random.normal(shape=(batch_size, embedding_dim))
    keys_emb = tf.random.normal(shape=(batch_size, seq_len, embedding_dim))

    print("Query Embedding shape:", query_emb.shape)
    print("Keys Embedding shape:", keys_emb.shape)

    attention_layer = DINAttentionLayer(hidden_units, dropout=0.1, l2_reg=1e-5)
    user_interest_vector = attention_layer(query_emb, keys_emb, mask=None, training=True)

    print("\nUser Interest Vector shape:", user_interest_vector.shape) # 期望 (batch_size, embedding_dim)

