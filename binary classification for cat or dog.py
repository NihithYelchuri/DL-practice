from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras import *
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array



#adding layers
classifier=Sequential()
classifier.add(Conv2D(32,(3,3),input_shape=(64,64,3),activation='relu'))
classifier.add(Conv2D(32,(3,3),activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2,2)))
#flattening
classifier.add(Flatten())
#Full connection
classifier.add(Dense(units=128,activation='relu'))
classifier.add(Dense(units=1,activation='sigmoid'))
#Compile the CNN
classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
#fitting cnn to the images
from keras.preprocessing.image import ImageDataGenerator
train_datagen=ImageDataGenerator(rescale=1./255,
                                 shear_range=0.2,
                                 zoom_range=0.2,
                                 horizontal_flip=True)
training_set =train_datagen.flow_from_directory("C:/Users/nihit/Desktop/New folder/train",target_size=(64,64),batch_size=32,class_mode='binary')


test_datagen=ImageDataGenerator(rescale=1./255)
test_set=train_datagen.flow_from_directory("C:/Users/nihit/Desktop/New folder/test",target_size=(64,64),batch_size=32,class_mode='binary')

classifier.fit_generator(training_set,steps_per_epoch=8000,epochs=25,validation_data=test_set,validation_steps=2000)

test_image=load_img("C:/Users/nihit/Desktop/images.jpg",target_size=(64,64))
test_image=img_to_array(test_image)
test_image=np.expand_dims(test_image,axis=0)
result=classifier.predict(test_image)
training_set.class_indices
if result[0][0]==1:
    prediction='dog'
else:
    prediction='cat'
print(prediction)
