# -*- coding: utf-8 -*-
"""
comments
author: diqiuzhuanzhuan
email: diqiuzhuanzhuan@gmail.com

"""
import numpy as np
from tensorflow.keras.datasets import mnist
import tensorflow as tf
import matplotlib.pyplot as plt


class VaeModel(object):

    def __init__(self):
        self.mean = None
        self.stddev = None
        self.likelihood_loss = None
        self.kl_divergence = None
        self.loss = None

    def create_encoder_layer(self, x, n_hidden, keep_prob, latent_dimension):
        """
        创建一个编码层
        :return:
        """
        with tf.variable_scope("encoder"):
            x_shape = x.get_shape().as_list()

            w_0 = tf.get_variable(name="encoder_w0", shape=[x_shape[1], n_hidden], initializer=tf.variance_scaling_initializer)
            b_0 = tf.get_variable(name="encoder_b0", shape=[n_hidden], initializer=tf.zeros_initializer)
            h_0 = tf.matmul(x, w_0) + b_0
            h_0 = tf.nn.elu(h_0)
            h_0 = tf.nn.dropout(h_0, keep_prob=keep_prob)
            h_0_shape = h_0.get_shape().as_list()

            w_1 = tf.get_variable(name="encoder_w1", shape=[h_0_shape[1], n_hidden], initializer=tf.variance_scaling_initializer)
            b_1 = tf.get_variable(name="encoder_b1", shape=[n_hidden], initializer=tf.zeros_initializer)
            h_1 = tf.matmul(h_0, w_1) + b_1
            h_1 = tf.nn.elu(h_1)
            h_1 = tf.nn.dropout(h_1, keep_prob=keep_prob)
            h_1_shape = h_1.get_shape().as_list()

            # 获得均值
            w_2_0 = tf.get_variable(name="encoder_w2_0", shape=[h_1_shape[1], latent_dimension], initializer=tf.variance_scaling_initializer)
            b_2_0 = tf.get_variable(name="encoder_b2_0", shape=[latent_dimension], initializer=tf.zeros_initializer)
            h_2_0 = tf.matmul(h_1, w_2_0) + b_2_0
            mean = h_2_0

            # 获得标准差
            w_2_1 = tf.get_variable(name="encoder_w2_1", shape=[h_1_shape[1], latent_dimension], initializer=tf.variance_scaling_initializer)
            b_2_1 = tf.get_variable(name="encoder_b2_1", shape=[latent_dimension], initializer=tf.zeros_initializer)
            h_2_1 = tf.matmul(h_1, w_2_1) + b_2_1
            # 标准差应当为正数，因此我们需要将之修正为正数，取指数是一个比较好的方式
            stddev = tf.nn.softplus(h_2_1)

            return mean, stddev

    def create_decoder_layer(self, z, n_hidden, keep_prob, output_dimension, predict=False):
        """
        创建一个解码层
        :param x:
        :param n_hidden:
        :param keep_prob:
        :param output_dimension:
        :param predict: True 说明是测试解码阶段
        :return:
        """
        with tf.variable_scope("decoder", reuse=tf.AUTO_REUSE):
            z_shape = z.get_shape().as_list()
            w_0 = tf.get_variable(name="decoder_w0", shape=[z_shape[1], n_hidden], initializer=tf.variance_scaling_initializer)
            b_0 = tf.get_variable(name="decoder_b0", shape=[n_hidden], initializer=tf.zeros_initializer)
            h_0 = tf.matmul(z, w_0) + b_0
            h_0 = tf.nn.elu(h_0)
            h_0 = tf.nn.dropout(h_0, keep_prob=keep_prob)
            h_0_shape = h_0.get_shape().as_list()

            w_1 = tf.get_variable(name="decoder_w1", shape=[h_0_shape[1], n_hidden], initializer=tf.variance_scaling_initializer)
            b_1 = tf.get_variable(name="decoder_b1", shape=[n_hidden], initializer=tf.zeros_initializer)
            h_1 = tf.matmul(h_0, w_1) + b_1
            h_1 = tf.nn.elu(h_1)
            h_1 = tf.nn.dropout(h_1, keep_prob=keep_prob)
            h_1_shape = h_1.get_shape().as_list()

            w_2 = tf.get_variable(name="decoder_w2", shape=[h_1_shape[1], output_dimension], initializer=tf.variance_scaling_initializer)
            b_2 = tf.get_variable(name="decoder_b2", shape=[output_dimension], initializer=tf.zeros_initializer)
            x = tf.matmul(h_1, w_2) + b_2
            # 我们的目标是像素值，也就是计算机中的0或者1，所以可以采用伯努利分布来做
            #if predict:
            x = tf.nn.sigmoid(x)

            #x = tf.clip_by_value(x, 1e-8, 1 - 1e-8)
            return x

    def create_sample_layer(self, shape):
        """
        重参数化，采样层
        :return:
        """
        with tf.variable_scope("sample"):
            mean = tf.constant(shape=[shape[1]], value=0.0)
            stddev = tf.constant(shape=[shape[1]], value=1.0)
            dist = tf.distributions.Normal(loc=mean, scale=stddev)
            samples = dist.sample([1], seed=1)

            return samples

    def build(self, x, n_hidden, keep_prob, latent_dimension, decode_z):
        self.mean, self.stddev = self.create_encoder_layer(x, n_hidden, keep_prob=keep_prob, latent_dimension=latent_dimension)
        samples = self.create_sample_layer(self.mean.get_shape().as_list())
        z = self.mean + samples * self.stddev
        y_hat = self.create_decoder_layer(z, n_hidden, keep_prob, output_dimension=x.get_shape().as_list()[1])
        self.likelihood_loss = tf.nn.sigmoid_cross_entropy_with_logits(labels=x, logits=y_hat)
        self.likelihood_loss = tf.reduce_sum(self.likelihood_loss, 1)
        self.likelihood_loss = tf.reduce_mean(self.likelihood_loss)
        normal_origin = tf.distributions.Normal(loc=tf.zeros(shape=tf.shape(z)), scale=tf.ones(shape=tf.shape(z)))
        normal_estimate = tf.distributions.Normal(loc=self.mean, scale=self.stddev)
        self.kl_divergence = tf.distributions.kl_divergence(normal_estimate, normal_origin)
        self.kl_divergence = tf.reduce_sum(self.kl_divergence, 1)
        self.kl_divergence = tf.reduce_mean(self.kl_divergence)
        # 我们要最小化损失，所以取负
        self.loss = -(-self.likelihood_loss - self.kl_divergence)
        predict = self.create_decoder_layer(decode_z, n_hidden, keep_prob, output_dimension=x.get_shape().as_list()[1], predict=True)

        return self.loss, predict


def load_data():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train = x_train /255
    x_test = x_test / 255
    x = np.append(x_train, x_test, axis=0)
    y = np.append(y_train, y_test, axis=0)
    samples = x.shape[0]
    x = np.reshape(x, [samples, -1])
    y = np.reshape(y, [samples, -1])
    return x, y


def main():
    tf.reset_default_graph()
    # 定义隐变量维度
    latent_dimension = 100
    x_train, y_train = load_data()
    x = tf.placeholder(dtype=tf.float32, shape=[None, 784])
    y = tf.placeholder(dtype=tf.float32, shape=[None, 1])
    z = tf.placeholder(dtype=tf.float32, shape=[None, latent_dimension])
    keep_prob = tf.placeholder(dtype=tf.float32)
    global_step = tf.Variable(0, trainable=False)

    loss, predict = VaeModel().build(x=x, n_hidden=100, keep_prob=keep_prob, latent_dimension=latent_dimension, decode_z=z)
    train_op = tf.train.AdagradOptimizer(learning_rate=0.001).minimize(loss=loss, global_step=global_step)
    epochs = 100

    it = 0
    test_z_list = [np.random.normal(0, 1, latent_dimension) for _ in range(10)]


    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for epoch in range(epochs):
            for _x, _y in zip(x_train, y_train):
                it = it + 1
                _, _loss = sess.run([train_op, loss], feed_dict={x: [_x], y: [_y], keep_prob: 0.8})
                if it % 20000 == 0:
                    print("iterator size is {}, loss is {}".format(it, _loss))
                    _z = sess.run(tf.random_normal(shape=[1, latent_dimension]))
                    decode_z = [255 * sess.run(predict, feed_dict={z:[_z], keep_prob: 1.0}) for _z in test_z_list]
                    decode_z = [np.reshape(_z, [28, 28]) for _z in decode_z]
                    for _decode_z, i in zip(decode_z, range(len(decode_z))):
                        plt.subplot(2, 5, i + 1)
                        plt.figure(figsize=(1, 1))
                        plt.axis("off")
                        plt.imshow(_decode_z, cmap="gray")
                    plt.show()





if __name__ == "__main__":
    main()


