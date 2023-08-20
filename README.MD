ChatBot


### Description: 
Chatbot powered by gpt-3.5-turbo answers questions related to Nifty Bridge terms of service.


## Installation:

Clone the project and then go to the root directory and create .env file like in .env.example 
(You might want to change the credentials). Then you can install app in tho ways:


### 1. Installation with docker:

Go to the root dir and build the image:

```commandline
docker build -t chatbot .
```
then run container:
```commandline
docker run -p 127.0.0.1:8000:8000 chatbot
```

### 1. Manually installation:

To install it manually you need python 3.9.10. First install the dependencies from the pyproject.toml file (you will need poetry, so if you don't have it, install 
it using the 'pip install poetry' command):


```commandline
poetry install
```

Then run command:

```commandline
uvicorn app.main:app
```

## Usage:

To ask question you have to send post request to http://127.0.0.1:8000/api/v1/nifty_bridge_terms/send_question

with request body parameter {"message": "your question"}

also you need to pass api_key from .env file in headers like this:

{"Authorization": "Bearer xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}