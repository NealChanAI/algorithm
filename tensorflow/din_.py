    # -*- coding: utf-8 -*-
# ===============================================================
#

#    @Create Time   : 2024/8/22 09:23
#    @Description   : 
#
# ===============================================================


import tensorflow as tf
from tensorflow.keras.layers import Layer, Dense


class DINLayer(Layer):
    def __init__(self, units):
        """
        Activation Unit计算逻辑
        :param units: activation层维度数
        """

        self.dense_layer_1 = Dense(units, activation='relu')
        self.dense_layer_2 = Dense(1)

    def call(self, query, keys):
        """
        完全前向计算
        :param query: 候选item id, shape(batch_size, embedding_dim)
        :param keys: 序列item ids, shape(batch_size, max_seq_len, embedding_dim)
        :return:
        """
        query = tf.expand(query, axis=1)  # batch_size, 1, embedding_dim
        query = tf.tile(query, [1, keys.shape[1], 1])  # batch_size, max_seq_len, embedding_dim

        combined = tf.concat([query, keys, query - keys, query * keys], axis=-1)  # batch_size, max_seq_len, embedding_dim * 4
        hidden_output_1 = self.dense_layer_1(combined)  # batch_size, max_seq_len, units
        attention_scores = self.dense_layer_2(hidden_output_1)  # batch_size, max_seq_len, 1
        attention_scores = tf.nn.softmax(attention_scores, axis=1)  # batch_size, max_seq_len, 1
        user_interested_embedding = tf.matmul(keys, attention_scores, transpose_a=True)  # batch_size, embedding_dim, 1
        user_interested_embedding = tf.squeeze(user_interested_embedding, axis=-1)  # batch_size, embedding_dim

        return user_interested_embedding






