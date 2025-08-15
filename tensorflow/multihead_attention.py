# -*- coding: utf-8 -*-
# ===============================================================
#
#
# ===============================================================


import tensorflow as tf
from tensorflow import keras


class MultiHeadSelfAttention(keras.layers.Layer):
    def __init__(self, d_model, num_heads, **kwargs):
        """
        多头注意力层(无Masking功能)
        :param d_model:
        :param num_heads:
        :param kwargs:
        """
        super(MultiHeadSelfAttention, self).__init__(**kwargs)
        self.d_model = d_model
        self.num_heads = num_heads

        # 每个注意力头的维度
        self.head_dim = d_model // num_heads

        self.query_dense = keras.layers.Dense(
            units=d_model,
            name='query_dense'
        )
        self.key_dense = keras.layers.Dense(
            units=d_model,
            name='key_dense'
        )
        self.value_dense = keras.layers.Dense(
            units=d_model,
            name='value_dense'
        )

        self.final_output_dense = keras.layers.Dense(
            units=d_model,
            name='final_output_dense'
        )

    def _split_heads(self, x, batch_size):
        """
        将张量拆分成多个头
        :param x:
        :param batch_size:
        :return:
        """
        # 将d_model维度重塑为(num_heads, head_dim)
        x = tf.reshape(x, (batch_size, -1, self.num_heads, self.head_dim))
        # 转置维度, 使num_heads成为第二个维度, 方便并行计算
        return tf.transpose(x, perm=[0, 2, 1, 3])

    def call(self, inputs):
        """
        完成多头自注意力前向计算
        :param inputs: shape (B, S, d_model)
        :return:
        """
        batch_size = tf.shape(inputs)[0]

        # 线性投影
        query = self.query_dense(inputs)  # (B, S, d_model)
        key = self.key_dense(inputs)  # (B, S, d_model)
        value = self.value_dense(inputs)  # (B, S, d_model)

        # 拆分注意力头
        query_heads = self._split_heads(query, batch_size)
        key_heads = self._split_heads(key, batch_size)
        value_heads = self._split_heads(value, batch_size)

        # 计算缩放点击注意力分数
        scaled_attention_scores = tf.matmul(query_heads, key_heads, transpose_b=True)

        # 缩放因子
        dk = tf.cast(self.head_dim, tf.float32)
        scaled_attention_scores /= tf.math.sqrt(dk)

        # softmax归一化
        attention_weights = keras.activations.softmax(scaled_attention_scores, axis=-1)

        # 注意力权重乘以Value
        context_heads = tf.matmul(attention_weights, value_heads)

        # 拼接所有头的输出
        context_all = tf.transpose(context_heads, perm=[0, 2, 1, 3])
        context_all = tf.reshape(context_all, (batch_size, -1, self.d_model))

        # 最终的线性投影
        output = self.final_output_dense(context_all)

        return output, attention_weights

    def get_config(self):
        config = super(MultiHeadSelfAttention, self).get_config()
        config.update({
            'd_model': self.d_model,
            'num_heads': self.num_heads
        })
        return config


if __name__ == '__main__':
    batch_size = 32
    seq_len = 10
    d_model = 16
    num_heads = 4

    inputs = tf.random.normal(shape=(batch_size, seq_len, d_model))
    multi_head_attention_layer = MultiHeadSelfAttention(d_model, num_heads)
    output_tensor, attention_weights = multi_head_attention_layer(inputs)

    print(output_tensor)
