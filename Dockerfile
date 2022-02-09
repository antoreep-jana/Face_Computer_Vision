FROM python:3.8
COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip --no-cache-dir install -r requirements.txt
#RUN apt-get update
#RUN apt-get update && apt-get install libgl1
#RUN sudo apt install libgl1-mesa-glx
RUN ECHO "Installation Completed"
#RUN apt-get install ffmpeg libsm6 libxext6  -y

EXPOSE 8501

ENTRYPOINT ['streamlit', 'run', '--server.maxUploadSize=5']
CMD ['app.py']