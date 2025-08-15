# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/7/19 01:00
#    @Description   : 手撕TextCNN
#
# ===============================================================


import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras.layers import Dense, Dropout, Layer, Input, Embedding, Conv1D, MaxPool1D, Concatenate, Flatten, ReLU


def text_cnn(seq_length, vocab_size, embedding_dim, num_cla, kernel_num):
    """
    seq_length: 输入的文字序列长度
    vocab_size: 词汇库的大小
    embedding_dim: 生成词向量的特征维度
    num_cla: 分类类别
    kernel_num:：卷积层的卷积核数
    """

    # 定义输入层
    inputX = Input(shape=(seq_length,), dtype='int32')
    # 嵌入层，将词汇的one-hot编码转为词向量
    embOut = Embedding(vocab_size, embedding_dim, input_length=seq_length)(inputX)

    # 分别使用长度为3，4，5的词窗口去执行卷积, 接着进行最大池化处理
    conv1 = Conv1D(kernel_num, 3, padding='valid', strides=1, activation='relu')(embOut)
    maxp1 = MaxPool1D(pool_size=int(conv1.shape[1]))(conv1)

    conv2 = Conv1D(kernel_num, 4, padding='valid', strides=1, activation='relu')(embOut)
    maxp2 = MaxPool1D(pool_size=int(conv2.shape[1]))(conv2)

    conv3 = Conv1D(kernel_num, 5, padding='valid', strides=1, activation='relu')(embOut)
    maxp3 = MaxPool1D(pool_size=int(conv3.shape[1]))(conv3)

    # 合并三个经过卷积和池化后的输出向量
    combineCnn = Concatenate(axis=-1)([maxp1, maxp2, maxp3])
    # 扁平化
    flatCnn = Flatten()(combineCnn)

    # 全连接层1，节点数为128
    desen1 = Dense(128)(flatCnn)
    # 在全连接层1和2之间添加dropout减少训练过程中的过拟合，随机丢弃25%的结点值
    dropout = Dropout(0.25)(desen1)
    # 为全连接层添加激活函数
    densen1Relu = ReLU()(dropout)
    # 全连接层2（输出层）
    predictY = Dense(num_cla, activation='softmax')(densen1Relu)

    # 指定模型的输入输出层
    model = keras.models.Model(inputs=inputX, ouputs=predictY)
    # 指定loss的计算方法，设置优化器，编译模型
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    return model
