FROM python:3.8
COPY . /home
WORKDIR /home

RUN pip install --upgrade pip
RUN pip --no-cache-dir install -r requirements.txt
#RUN apt-get update
#RUN apt-get update && apt-get install libgl1
#RUN sudo apt install libgl1-mesa-glx
RUN apt-get install -y wget 
RUN wget https://github.com/serengil/deepface_models/releases/download/v1.0/age_model_weights.h5
RUN mkdir home/appuser/.deepface
RUN mkdir home/appuser/.deepface/weights
COPY age_model_weights.h5 home/appuser/.deepface/weights/age_model_weights.h5
RUN ECHO "Installation Completed"

#RUN apt-get install ffmpeg libsm6 libxext6  -y

EXPOSE 8501

ENTRYPOINT ['streamlit', 'run', '--server.maxUploadSize=5']
CMD ['app.py']