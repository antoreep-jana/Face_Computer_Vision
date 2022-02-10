

from deepface import DeepFace

class SentimentClassifier:

	def __init__(self, img_path):

		self.img = img_path


	def get_sentiment(self):

		emotions = DeepFace.analyze(img_path = self.img, actions = ['emotion'])['emotion']	
		return max(zip(emotions.values(), emotions.keys()))[1]