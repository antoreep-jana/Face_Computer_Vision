from mask_prediction import MaskPredictor 
	
def test_mask_prediction():
	
	img_path1 = 'tests/data/mask_prediction/mask1.jpeg'
	img_path2 = 'tests/data/mask_prediction/mask2.jpg'
	img_path3 = 'tests/data/mask_prediction/mask3.jpg'
	img_path4 = 'tests/data/mask_prediction/mask4.jpg'
	img_path5 = 'tests/data/mask_prediction/mask5.jpg'
	img_paths = [img_path1, img_path2, img_path3, img_path4, img_path5]

	for img in img_paths:
		predictor = MaskPredictor(img)
		result = predictor.predict()

		assert result == True


def test_no_mask_prediction():

	#img_paths = []
	img_path1 = 'tests/data/mask_prediction/nomask1.jpg'
	img_path2 = 'tests/data/mask_prediction/nomask2.jpeg'
	img_path3 = 'tests/data/mask_prediction/nomask3.jpeg'
	img_paths = [img_path1, img_path2, img_path3]
	
	for img in img_paths:
		
		predictor = MaskPredictor(img)
		result = predictor.predict()

		assert result == False
