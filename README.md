# requreIt: Qualifind module

### Overview

Qualifind (working title) is a service connecting clients and freelance web developers.
The purpose of it is to create a safe space with proper quality, which would help
clients to have clear and complete scope of requirements.  
   
This application is the first cycle of 'requireIt' module. There is a prototype front-end,
but the idea is to put this module during the project posting process, so user could send
the detailed requirements together with project description.
   
The main function of this module is to propose a list of necessary requirements and tips 
depending on a series of questions, such as industry, scope, target audience, revenue model 
etc. The user afterwards will have an opportunity to add their own requirements to the list.

## Installation
You need Node.js, npm and Python3 installed.

### Install dependencies for front end
In cmd window:
```
cd path\to\project\frontend npm install
```

### Install dependencies for back end

In cmd window:
```
cd path\to\project\backend pip install -r requirements.txt
```

## Run the app

Open two cmd terminals and keep them running  simultaneously 

### In cmd window
```
cd path\to\project\backend
python manage.py runserve
```

### In another cmd window
```
cd path\to\project\frontend
npm run serve
```

You will see the following message
```
  App running at:
  - Local:   http://localhost:8080/
  - Network: http://192.168.0.13:8080/

  Note that the development build is not optimized.
  To create a production build, run npm run build.
```
Go to your browser and open window with http://localhost:8080/ as address (it will probably be http://127.0.0.1:8080).