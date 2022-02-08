import streamlit as st 

from PIL import Image 

st.title("Face Computer Vision")


st.sidebar.markdown("""Perform various tasks related face using this tool""")


#st.subheader("Choose an option")

option = st.selectbox("Choose the operation to perform", ['Age Prediction', 'Face Deblur', 'Face Recognition', 'Sentiment Classification', "Mask Prediction"])


file = st.file_uploader("Upload an image from local disk", type = ['jpg', 'jpeg', 'png'])

    if file is not None:

        image = Image.open(file)

        #st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write("")
        #st.write("Classifying...")

        #label = 'Label1'
        #st.write(f"Classified as {label}")

        if option == 'Age Prediction':

            age = '10'
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



