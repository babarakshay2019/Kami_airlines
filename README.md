# Installation #

Follow these steps to get the application running in your local/test environment:


## clone project##
git clone https://github.com/babarakshay2019/Kami_airlines.git


## Requirements ##
* Python 3 and above


## local setup ##
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## commands for create db tables and runserver ##
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 
```

## for run test cases ##

python manage.py test airplanes

## for checking coverage ##
```
coverage run manage.py test airplanes
coverage report
```

## API  link ##
http://127.0.0.1:8001/api/airplanes/