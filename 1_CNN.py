# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 10:54:45 2024

@author: nayek
"""

from keras.layers import Convolution2D, MaxPooling2D, Activation
from keras.models import Sequential
from numpy import asarray
import numpy as np
import matplotlib.pyplot as plt
import cv2

# Reading an image
img =  cv2.imread('pcos3.jpg' , cv2.IMREAD_GRAYSCALE)
img = img
plt.imshow(img, cmap = 'gray')
plt.show()

# know shape (300,300)
print(img.shape)

# Keras expects batches of images, so we have to add a dimension to trick it into a batch
img_batch =  img.reshape(1, img.shape[0], img.shape[1],1)
img_batch.shape
img_batch.shape[1:]

# here we are using 1 filter valid padding = no padding so image size will get reduced
  
model1 = Sequential()
model1.add(Convolution2D(1, (15,15) , padding = 'valid' , input_shape = img_batch.shape[1:])) # Random weight Initilaization
model1.summary()

conv_img = model1.predict(img_batch)

conv_img_show = conv_img.reshape(conv_img.shape[1], conv_img.shape[2])
print(conv_img_show)
plt.imshow(conv_img_show, cmap = 'gray')
plt.show()

# add RELU Unit
model2 = Sequential()
model1.add(Convolution2D(1, (15,15) , padding = 'valid' , input_shape = img_batch.shape[1:])) # Random weight Initilaization
model2.add(Activation('relu'))

conv_img = model2.predict(img_batch)

conv_img_show = conv_img.reshape(conv_img.shape[1], conv_img.shape[2])
print(conv_img_show)
plt.imshow(conv_img_show, cmap = 'gray')
plt.show()

# Combining both relu and maxpooling 

model4 = Sequential()
model4.add(Convolution2D(1, (15,15) , padding = 'valid' , input_shape = img_batch.shape[1:])) # Random weight Initilaization
model4.add(Activation('relu'))
model4.add(MaxPooling2D(pool_size=(2,2)))

model4.summary()

conv_img = model4.predict(img_batch)
conv_img_show = conv_img.reshape(conv_img.shape[1], conv_img.shape[2])
plt.imshow(conv_img_show, cmap = 'gray')
plt.show()


# Define custom weights to the model

model5 = Sequential()
model5.add(Convolution2D(1, (3,3) , input_shape = img_batch.shape[1:])) # Random weight Initilaization

# define a vertical line detector
detector_x = [[[[-1]],[[0]],[[1]]],
              [[[-2]],[[0]],[[2]]],
              [[[-1]],[[0]],[[1]]]]
detector_y = [[[[1]],[[2]],[[1]]],
              [[[0]],[[0]],[[0]]],
              [[[-1]],[[-2]],[[-1]]]]

weights = [[asarray(detector_y)]]
print(len(weights))


# store the wewights in the model
model5.set_weights(weights)
conv_img = model5.predict(img_batch)

conv_img_show = conv_img.reshape(conv_img.shape[1], conv_img.shape[2])
plt.imshow(conv_img_show, cmap = 'gray')
plt.show()







