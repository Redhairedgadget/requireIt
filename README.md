#Option 1: the project is used from zip file

Open two cdm terminals and keep them running  simultaniously 

##In cdm window
```
cd path\to\project\backend 
python manage.py runserve
```

##In another cdm window
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

#Option 2: the project is cloned from github
You need Node.js, npm and Python3 installed.

##Install dependencies for front end
In cdm window:
```
cd path\to\project\frontend npm install
```

##Install dependencies for back end

In cdm window:
```
cd path\to\project\backend pip install -r requirements.txt
```

##Repeat same actions as in option 1