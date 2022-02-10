

from deepface import DeepFace

class FaceVerifier:

	def __init__(self, img_path1, img_path2):

		self.img1 = img_path1
		self.img2 = img_path2

	def verify(self):

		result = DeepFace.verify(img1_path = self.img1, img2_path = self.img2)

		return result['verified']