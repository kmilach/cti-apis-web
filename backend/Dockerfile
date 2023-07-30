# base image
FROM python:3.10.12-slim-bullseye
# work directory
WORKDIR /app
# first install the required python modules
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
# copy the entire backend and run the flask app
COPY . .
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
EXPOSE 5000/tcp