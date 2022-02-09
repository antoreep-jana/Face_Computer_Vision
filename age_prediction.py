from deepface import DeepFace

class AgePredictor:


	def __init__(self, img):

		self.image = img 

	def predict_age(self):
		return DeepFace.analyze( img_path = self.image, actions = ['age'])['age']

		