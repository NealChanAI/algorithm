# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/21 20:38
#    @Description   : tensorflow实现attention层
#
# ===============================================================


import tensorflow as tf
from tensorflow.keras.layers import Layer, Dense


class AttentionLayer(Layer):
    def __init__(self, units):
        super(AttentionLayer, self).__init__()

        self.units = units
        self.query_dense = Dense(units)  # query_embedding
        self.key_dense = Dense(units)  # key_embedding
        self.value_dense = Dense(units)  # value_embedding

    def call(self, inputs):
        """
        前向传播
        :param inputs: shape(batch, max_seq_len, input_dim)
        :return:
        """
        query = self.query_dense(inputs)  # batch, max_seq_len, units
        key = self.key_dense(inputs)  # batch, max_seq_len, units
        value = self.value_dense(inputs)  # batch, max_seq_len, units

        attention_scores = tf.matmul(query, key, transpose_b=True) / \
                           tf.math.sqrt(tf.cast(self.units, tf.float32))  # batch, max_seq_len, max_seq_len

        attention_scores = tf.nn.softmax(attention_scores, axis=-1)  # batch, max_seq_len, max_seq_len
        value_embed = tf.matmul(attention_scores, value)  # batch, max_seq_len, units

        return value_embed, attention_scores




