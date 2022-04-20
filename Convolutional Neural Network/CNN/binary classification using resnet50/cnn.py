from contextlib import suppress
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import skimage.io
import os
import tqdm
import glob
import tensorflow

from tqdm import tqdm
from sklearn.utils import shuffle
from sklearn import metrics
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split

from skimage import io
from skimage.io import imread, imshow
from skimage.transform import resize
from skimage.color import gray2rgb

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image_dataset_from_directory
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import InputLayer, BatchNormalization, Dropout, Flatten, Dense, Activation, MaxPool2D, Conv2D
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.utils import to_categorical
from keras import optimizers

from keras.callbacks import Callback, ModelCheckpoint
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout
from keras.wrappers.scikit_learn import KerasClassifier
import keras.backend as K

from keras.applications.imagenet_utils import decode_predictions
#import tensorflow_addons as tfa
#from tensorflow.keras.metrics import Metric
#from tensorflow_addons.utils.types import AcceptableDTypes, FloatTensorLike
from typeguard import typechecked
from typing import Optional

import keras


class CNN:
    def __init__(self):
        self.model = self.buildModel()

    def buildModel(self):
        AUTOTUNE = tf.data.experimental.AUTOTUNE
        train_datagen = ImageDataGenerator(rescale=1./255,
                                           validation_split=0.2,
                                           rotation_range=5,
                                           width_shift_range=0.2,
                                           height_shift_range=0.2,
                                           shear_range=0.2,
                                           # zoom_range=0.2,
                                           horizontal_flip=True,
                                           vertical_flip=True,
                                           fill_mode='nearest')
        valid_datagen = ImageDataGenerator(rescale=1./255,validation_split=0.2)
        test_datagen = ImageDataGenerator(rescale=1./255)
        train_dataset = train_datagen.flow_from_directory(directory='./binaryClassificationDataset/train',
                                                  target_size=(224, 224),
                                                  class_mode='categorical',
                                                  subset='training',
                                                  batch_size=32)
        valid_dataset = valid_datagen.flow_from_directory(directory='./binaryClassificationDataset/train',
                                                  target_size=(224, 224),
                                                  class_mode='categorical',
                                                  subset='validation',
                                                  batch_size=32)
        test_dataset = test_datagen.flow_from_directory(directory='./binaryClassificationDataset/test',
                                                target_size=(224, 224),
                                                class_mode='categorical',
                                                batch_size=32)
        base_model = ResNet50(input_shape=(224, 224, 3),
                      include_top=False,
                      weights="imagenet")
        for layer in base_model.layers:
            layer.trainable = False
        model = Sequential()
        model.add(base_model)
        model.add(Dropout(0.5))
        model.add(Flatten())
        model.add(BatchNormalization())
        model.add(Dense(64, kernel_initializer='he_uniform'))
        model.add(BatchNormalization())
        model.add(Activation('relu'))
        model.add(Dropout(0.5))
        model.add(Dense(64, kernel_initializer='he_uniform'))
        model.add(BatchNormalization())
        model.add(Activation('relu'))
        model.add(Dropout(0.5))
        model.add(Dense(64, kernel_initializer='he_uniform'))
        model.add(BatchNormalization())
        model.add(Activation('relu'))
        model.add(Dropout(0.5))
        model.add(Dense(32, kernel_initializer='he_uniform'))
        model.add(BatchNormalization())
        model.add(Activation('relu'))
        model.add(Dropout(0.5))
        model.add(Dense(32, kernel_initializer='he_uniform'))
        model.add(BatchNormalization())
        model.add(Activation('relu'))
        model.add(Dense(2, activation='softmax'))

        def f1_score(y_true, y_pred): #taken from old keras source code
            true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
            possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
            predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
            precision = true_positives / (predicted_positives + K.epsilon())
            recall = true_positives / (possible_positives + K.epsilon())
            f1_val = 2*(precision*recall)/(precision+recall+K.epsilon())
            return f1_val

        METRICS = [
        tf.keras.metrics.BinaryAccuracy(name='accuracy'),
        tf.keras.metrics.Precision(name='precision'),
        tf.keras.metrics.Recall(name='recall'),  
        tf.keras.metrics.AUC(name='auc'),
        f1_score,
        ]

        def exponential_decay(lr0, s):
            def exponential_decay_fn(epoch):
                return lr0 * 0.1 **(epoch / s)
            return exponential_decay_fn

        exponential_decay_fn = exponential_decay(0.01, 5) # when i run it for 50 epochs

        lr_scheduler = tf.keras.callbacks.LearningRateScheduler(exponential_decay_fn)

        model.compile(optimizer='rmsprop', loss='categorical_crossentropy',metrics=METRICS)
        return model

    def predictSetup(file_path):
        fileName = file_path
        img = tf.keras.preprocessing.image.load_img(
        fileName,
        target_size=(224,224)
        )
        img_nparray = tf.keras.preprocessing.image.img_to_array(img)
        type(img_nparray) # numpy.ndarray
        input_Batch = np.array([img_nparray])
        np.set_printoptions(suppress=True)
        
        return input_Batch
