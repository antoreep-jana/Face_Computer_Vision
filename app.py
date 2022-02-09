import streamlit as st 

from PIL import Image 

st.title("Face Computer Vision")


st.sidebar.markdown("""Perform various tasks related face using this tool""")


#st.subheader("Choose an option")


uploaded_file = st.file_uploader("Upload an image from local disk", type = ['jpg', 'jpeg', 'png'])



option = st.selectbox("Choose the operation to perform", ['Age Prediction', 'Face Deblur', 'Face Recognition', 'Sentiment Classification', "Mask Prediction", "Face Verification"])




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
		

		print("Image Path -> ", img_path)
		predictor = AgePredictor(img_path)
		#print(predictor)

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

	elif option == "Face Recognition":

		st.write("Recognizing face")

	elif option == 'Sentiment Classification':

		sentiment = 'happy'
		st.write(f"Sentiment of the face : {sentiment}")

	elif option == "Mask Prediction":

		st.write("Predicted Mask")

