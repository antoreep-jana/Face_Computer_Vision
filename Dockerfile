FROM python:3.8
COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip --no-cache-dir install -r requirements.txt

EXPOSE 8501

ENTRYPOINT ['streamlit', 'run', '--server.maxUploadSize=5']
CMD ['app.py']