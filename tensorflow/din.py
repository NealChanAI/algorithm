# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/7/18 23:06
#    @Description   : 手撕DIN
#
# ===============================================================


import tensorflow as tf
from tensorflow.keras.layers import Layer, Dense, Embedding, Input


class AttentionLayer(Layer):
    def __init__(self, units):  # units为Activation unit中的隐藏层维度
        super(AttentionLayer, self).__init__()
        self.dense1 = Dense(units, activation="relu")
        self.dense2 = Dense(1)

    def call(self, query, keys):
        # query: batch_size, embedding_dim
        # keys:  batch_size, max_seq_len, embedding_dim

        # 扩展query维度
        query = tf.expand_dims(query, axis=1)  # batch_size, 1, embedding_dim
        query = tf.tile(query, [1, keys.shape[1], 1])  # batch_size, max_seq_len, embedding_dim

        # 计算attention分数
        combined = tf.concat([query, keys, query * keys, query - keys],
                             axis=-1)  # batch_size, max_seq_len, 4 * embedding_dim
        dense_out = self.dense1(combined)  # batch_size, max_seq_len, units
        scores = self.dense2(dense_out)  # batch_size, max_seq_len, 1
        # scores = tf.nn.softmax(scores, axis=1)  # batch_size, max_seq_len, 1  没有使用softmax

        # 计算用户兴趣向量
        weighted_keys = tf.matmul(keys, scores, transpose_a=True)  # batch_size, embedding, 1
        used_intersted_embedding = tf.squeeze(weighted_keys, axis=-1)  # batch_size, embedding
        return used_intersted_embedding


if __name__ == '__main__':
    # 测试 AttentionLayer
    batch_size = 32
    seq_len = 10
    embedding_dim = 16
    units = 8

    # 假设我们有当前候选物品的嵌入向量 query 和用户历史行为的嵌入序列 keys
    query = tf.random.normal(shape=(batch_size, embedding_dim))
    keys = tf.random.normal(shape=(batch_size, seq_len, embedding_dim))

    attention_layer = AttentionLayer(units)
    context_vector = attention_layer(query, keys)

    print("Context vector shape:", context_vector.shape)  # (batch_size, embedding_dim)
