import streamlit as st 



st.title("Face Computer Vision")


st.sidebar.markdown("""Perform various tasks related face using this tool""")


#st.subheader("Choose an option")

st.selectbox("Choose the operation to perform", ['Age Prediction', 'Face Deblur', 'Face Recognition', 'Sentiment Classification', "Mask Prediction"])
