# instawork
Team Members Project

APIs - 
- GET - http://127.0.0.1:8010/api/user/ (to get the list of all team members).
- POST -  http://127.0.0.1:8010/api/user/ (to create a team member).  
```sh
- request
  {   
     "first_name": "Satish",
    "last_name": "Shekhar",
    "phone_number": "9148450822",
    "email": "shekhar@gmail.com",
    "role": 2
  }
 - response
{
    "is_success": true,
    "message": null,
    "response_data": {
        "id": 11,
        "first_name": "Satish",
        "last_name": "Shekhar",
        "phone_number": "9148450822",
        "email": "shekhar@gmail.com",
        "role": "Regular"
    }
}
```
- PUT -  http://127.0.0.1:8010/api/user/ (to update a team member). 
```sh
- request
          {   
                "id":9,
                "first_name": "SatishczxSC",
                "last_name": "ShekharcXxzc",
                "phone_number": "9148450811"
           }
 - response
{
    "is_success": true,
    "message": [
        "Member details updated!"
    ],
    "response_data": {
        "id": 8,
        "first_name": "SatishczxSC",
        "last_name": "ShekharcXxzc",
        "phone_number": "9148450812"
    }
}
```

# Steps to run the application:-
- clone the project - ```git clone https://github.com/Raj160907/instawork.git```<br/>
- create and start a virtual environment - ```virtualenv env -p python3```</br>
- Activate virtual environment - ```source env/bin/activate```<br/>
- Install the project dependencies: - 
```pip install -r requirements.txt``` <br/>
- create a mysql db and add the credentials to settings.py - <br/>
```sh
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_name',
        'USER': 'db_user',
        'PASSWORD': 'db_password',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}
```

```sh
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
```
