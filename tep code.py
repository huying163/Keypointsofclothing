# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 23:08:53 2018

@author: Administrator
"""
# score tem code
resized_image = tf.image.resize_images(img, [size, size])
sess = tf.Session()
result = sess.run(resized_image)

imgplot = plt.imshow(img)
shapelist,