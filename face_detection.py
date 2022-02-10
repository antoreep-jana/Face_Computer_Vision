
from deepface import DeepFace


class FaceDetector:

	def __init__(self, img, detector = 'mtcnn'):

		self.image = img 
		self.detector = detector


	def detect_face(self):

		detection = DeepFace.detectFace(img_path = self.image, detector_backend = self.detector)

		return detection

