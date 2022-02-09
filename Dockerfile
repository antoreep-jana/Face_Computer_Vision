FROM python:3.8
COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip --no-cache-dir install -r requirements.txt
RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python

EXPOSE 8501

ENTRYPOINT ['streamlit', 'run', '--server.maxUploadSize=5']
CMD ['app.py']