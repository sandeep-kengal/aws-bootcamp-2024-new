# Using the python image provided by docker
# FROM python:3.10-slim-buster
# Using the python image stored in ECR
FROM 652162945585.dkr.ecr.us-east-1.amazonaws.com/cruddur-python:3.10-slim-buster

ENV PORT=4567 
#Inside container
#make a new folder inside container
WORKDIR /backend-flask

#outside container -> inside container 
#this contains the libraries we want installed to run the app
COPY requirements.txt requirements.txt

#Inside container 
#Install the python libraries used by the app
RUN pip3 install -r requirements.txt

#outide container -> inside container
# . means evrything in the current directory
# first period . ~ /backend flask (outside container) 
# second period . ~ /backend flask (inside container)
COPY . .

#Set environment variables
#inside container and will remain set while the container runs
# ENV FLASK_DEBUG=1 # Having the flag "--debug" enables debugging

EXPOSE ${PORT}

#CMD (Command)
# python3 -m flask run --host=0.0.0.0 --port=4567 //Shortcut to run flask
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567", "--debug"]

