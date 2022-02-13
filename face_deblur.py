import tensorflow
from tensorflow.keras.layers import *
from tensorflow.keras import Model
import cv2 
import numpy as np
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt 
from PIL import Image 

class FaceUnblur:

	def __init__(self, image_path):

		self.img = image_path
		self.img = image.load_img(self.img, target_size = (64, 64))

		#self.img = self.img / 255.0
		self.img_array = image.img_to_array(self.img)
		self.img_batch = np.expand_dims(self.img_array, axis=0)

	def load_model(self):
		deblur_CNN_input = Input(shape=(64,64,3))

		#HIDDEN LAYERS
		deblur_CNN_layer1 = Conv2D(filters=128, kernel_size=10, strides = 1, padding='same')(deblur_CNN_input)
		deblur_CNN_layer1 = BatchNormalization()(deblur_CNN_layer1)
		deblur_CNN_layer1 = Activation('relu')(deblur_CNN_layer1)

		deblur_CNN_layer2 = Conv2D(filters=320, kernel_size=1, strides = 1, padding='same')(deblur_CNN_layer1)
		deblur_CNN_layer2 = BatchNormalization()(deblur_CNN_layer2)
		deblur_CNN_layer2 = Activation('relu')(deblur_CNN_layer2)

		deblur_CNN_layer3 = Conv2D(filters=320, kernel_size=1, strides = 1, padding='same')(deblur_CNN_layer2)
		deblur_CNN_layer1 = BatchNormalization()(deblur_CNN_layer3)
		deblur_CNN_layer1 = Activation('relu')(deblur_CNN_layer3)

		deblur_CNN_layer4 = Conv2D(filters=320, kernel_size=1, strides = 1, padding='same')(deblur_CNN_layer3)
		deblur_CNN_layer4 = BatchNormalization()(deblur_CNN_layer4)
		deblur_CNN_layer4 = Activation('relu')(deblur_CNN_layer4)

		deblur_CNN_layer5 = Conv2D(filters=128, kernel_size=1, strides = 1, padding='same')(deblur_CNN_layer4)
		deblur_CNN_layer5 = BatchNormalization()(deblur_CNN_layer5)
		deblur_CNN_layer5 = Activation('relu')(deblur_CNN_layer5)

		deblur_CNN_layer6 = Conv2D(filters=128, kernel_size=3, strides = 1, padding='same')(deblur_CNN_layer5)
		deblur_CNN_layer6 = BatchNormalization()(deblur_CNN_layer6)
		deblur_CNN_layer6 = Activation('relu')(deblur_CNN_layer6)

		deblur_CNN_layer7 = Conv2D(filters=512, kernel_size=1, strides = 1, padding='same')(deblur_CNN_layer6)
		deblur_CNN_layer7 = BatchNormalization()(deblur_CNN_layer7)
		deblur_CNN_layer7 = Activation('relu')(deblur_CNN_layer7)

		deblur_CNN_layer8 = Conv2D(filters=128, kernel_size=5, strides = 1, padding='same')(deblur_CNN_layer7)
		deblur_CNN_layer8 = BatchNormalization()(deblur_CNN_layer8)
		deblur_CNN_layer8 = Activation('relu')(deblur_CNN_layer8)

		deblur_CNN_layer9 = Conv2D(filters=128, kernel_size=5, strides = 1, padding='same')(deblur_CNN_layer8)
		deblur_CNN_layer9 = BatchNormalization()(deblur_CNN_layer9)
		deblur_CNN_layer9 = Activation('relu')(deblur_CNN_layer9)

		deblur_CNN_layer10 = Conv2D(filters=128, kernel_size=3, strides = 1, padding='same')(deblur_CNN_layer9)
		deblur_CNN_layer10 = BatchNormalization()(deblur_CNN_layer10)
		deblur_CNN_layer10 = Activation('relu')(deblur_CNN_layer10)

		deblur_CNN_layer11 = Conv2D(filters=128, kernel_size=5, strides = 1, padding='same')(deblur_CNN_layer10)
		deblur_CNN_layer11 = BatchNormalization()(deblur_CNN_layer11)
		deblur_CNN_layer11 = Activation('relu')(deblur_CNN_layer11)

		deblur_CNN_layer12 = Conv2D(filters=128, kernel_size=5, strides = 1, padding='same')(deblur_CNN_layer11)
		deblur_CNN_layer12 = BatchNormalization()(deblur_CNN_layer12)
		deblur_CNN_layer12 = Activation('relu')(deblur_CNN_layer12)

		deblur_CNN_layer13 = Conv2D(filters=256, kernel_size=1, strides = 1, padding='same')(deblur_CNN_layer12)
		deblur_CNN_layer13 = BatchNormalization()(deblur_CNN_layer13)
		deblur_CNN_layer13 = Activation('relu')(deblur_CNN_layer13)

		deblur_CNN_layer14 = Conv2D(filters=64, kernel_size=7, strides = 1, padding='same')(deblur_CNN_layer13)
		deblur_CNN_layer14 = BatchNormalization()(deblur_CNN_layer14)
		deblur_CNN_layer14 = Activation('relu')(deblur_CNN_layer14)

		deblur_CNN_output = Conv2D(filters=3, kernel_size=7, strides = 1, padding='same', activation='relu')(deblur_CNN_layer14)

		deblur_CNN = Model(inputs= deblur_CNN_input, outputs=deblur_CNN_output )


		adam = tensorflow.keras.optimizers.Adam(learning_rate= 0.00001)
		deblur_CNN.compile(optimizer= adam, loss= 'mean_squared_error')
		deblur_CNN.load_weights('celebA_deblur_cnn_weights.h5')
		return deblur_CNN

	def unblur_face(self):

		model = self.load_model()
		#self.process_image()
		#print(self.img)
		Deblurred = model.predict(self.img_batch)
		Deblurred = np.clip(Deblurred, 0, 255)

		#print(Deblurred)
		# f, ax = plt.subplots(3,10, figsize=(15,5))
		# for i in range(1):
		# 	#ax[0,i].imshow(Images[i].astype('uint8'));  ax[0,i].axis('Off'); ax[0,i].set_title('Clean', size=15)
		# 	#ax[1,i].imshow(Blurry[i].astype('uint8'));  ax[1,i].axis('Off'); ax[1,i].set_title('Blurry', size=15)
		# 	ax[2,i].imshow(Deblurred[i].astype('uint8'));  ax[2,i].axis('Off'); ax[2,i].set_title('Deblurred', size=15)
		# plt.show()
		#print((Deblurred))

		Deblurred = Deblurred.astype("uint8")
		#return cv2.resize(Deblurred, dsize = (256, 256), interpolation = cv2.INTER_CUBIC)
		return Deblurred