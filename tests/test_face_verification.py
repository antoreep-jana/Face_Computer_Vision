from face_verification import FaceVerifier

def test_Face_verifier():
	img_path1 = 'tests/data/face_verification/carl_jung_1.jpg'
	img_path2 = 'tests/data/face_verification/carl_jung_2.jpg'
	verifier = FaceVerifier(img_path1, img_path2)
	result = verifier.verify()
	assert result == True
