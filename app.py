import streamlit as st 

from PIL import Image 

st.title("Face Computer Vision")


st.sidebar.markdown("""Perform various tasks related face using this tool""")


#st.subheader("Choose an option")


uploaded_file = st.file_uploader("Upload an image from local disk", type = ['jpg', 'jpeg', 'png'])



option = st.selectbox("Choose the operation to perform", ['Age Prediction', 'Face Deblur', 'Face Detection', 'Sentiment Classification', "Mask Prediction", "Face Verification"])




if uploaded_file is not None:

	image = Image.open(uploaded_file)
	#print(uploaded_file.name)
	#print(str(uploaded_file.name))

	image.save("tmp/" + str(uploaded_file.name))
	img_path = "tmp/" + str(uploaded_file.name)
	st.write("")
		
	if option == 'Age Prediction':

		#age = '10'
		from age_prediction import AgePredictor
		
		# https://github.com/serengil/deepface_models/releases/download/v1.0/age_model_weights.h5

		# to /home/appuser/.deepface/weights/age_model_weights.h5

		#print("Image Path -> ", img_path)
		predictor = AgePredictor(img_path)
		#print(predictor)

		with st.spinner("Predicting age..."):
			age = predictor.predict_age()
		#age = 10
		#print(predictor.predict_age())
		#from deepface import DeepFace
		#print(uploaded_file)
		#age = DeepFace.analyze(img_path = img_path, actions = ['age'])['age']

			st.write(f"Predicted age : {age}")

	elif option == 'Face Deblur':

		st.image(image, caption = 'Deblurred Image', use_column_width = True)
		st.write("Face Deblurred")

	elif option == "Face Detection":

		with st.spinner("Detecting Faces...."):
			from face_detection import FaceDetector 

			face = FaceDetector(img_path)
			detection = face.detect_face()


			st.image(image, width = 250, caption = 'Input Image', use_column_width = False)
			st.image(detection, width = 250, caption = 'Detection', use_column_width = False)


	elif option == 'Sentiment Classification':

		sentiment = 'happy'
		st.write(f"Sentiment of the face : {sentiment}")

	elif option == "Mask Prediction":

		st.write("Predicted Mask")

	elif option == "Face Verification":

		uploaded_file2 = st.file_uploader("Upload another image from local disk for verification", type = ['jpg', 'jpeg', 'png'])

		if uploaded_file2 is not None:

			image2 = Image.open(uploaded_file2)

			image2.save("tmp/" + str(uploaded_file2.name))
			img_path2 = "tmp/" + str(uploaded_file2.name)

			with st.spinner("Verifying input images..."):
				from face_verification import FaceVerifier

				verifier = FaceVerifier(img_path, img_path2)

				result = verifier.verify()

				st.write(f"Output of verification : {result}")


