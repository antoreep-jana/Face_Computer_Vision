from deepface import DeepFace


#img_path = 'tests/data/1.jpg'

# obj = DeepFace.analyze(img_path = img_path, actions = ['age'])
# print(obj['age'])

class AgePredictor:


	def __init__(self, img):

		self.image = img 

	def predict_age(self):
		obj = DeepFace.analyze(img_path = self.image, actions = ['age'])

		return obj['age']



# obj = AgePredictor(img_path)
# print(obj.predict_age())