# -*- coding: utf-8 -*-
# ===============================================================
#    @Create Time   : 2024/7/18 21:08
#    @Description   : 手撕Attention
#
# ===============================================================


import tensorflow as tf
from tensorflow.keras.layers import Layer, Dense


class SelfAttention(Layer):
    def __init__(self, units):
        super(SelfAttention, self).__init__()
        """定义模型的层次"""
        self.units = units
        self.query_dense = Dense(units)  # W_q
        self.key_dense = Dense(units)  # W_k
        self.value_dense = Dense(units)  # W_v

    def call(self, inputs):
        """完成前向计算"""
        # input shape: (batch_size, seq_len, input_dim)
        query = self.query_dense(inputs)  # batch_size, seq_len, units
        key = self.key_dense(inputs)
        value = self.value_dense(inputs)

        attention_scores = tf.matmul(query, key, transpose_b=True) / tf.math.sqrt(tf.cast(self.units, tf.float32)) # batch_size, seq_len, seq_len
        scores = tf.nn.softmax(attention_scores, axis=-1)  # batch_size, seq_len, seq_len

        convex_vector = tf.matmul(scores, value)  # batch_size, seq_len, units
        return convex_vector, scores


if __name__ == '__main__':
    batch_size = 32
    seq_len = 10
    input_dim = 16
    units = 8

    inputs = tf.random.normal(shape=(batch_size, seq_len, input_dim))
    self_attention = SelfAttention(units)
    convex_vector, scores = self_attention(inputs)

