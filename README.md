# instawork
Team Members Project

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
