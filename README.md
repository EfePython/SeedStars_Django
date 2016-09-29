# DjangoApp


### Project specifications
- Operating System platform: Windows
- Python version: 3.5.2
- Pip version: 8.1.1


### Project setup steps:
----------
- Create project directory

- Initialize git repository

- Create virtual environment
```terminal
virtualenv env
```

- Add "env" directory to .gitignore file

- Install Library dependencies
```
env\Scripts\pip install django==1.10.1
```

- Generate requirements file for repeatable installations:
```terminal
env\Scripts\pip freeze > requirements.txt
```
For later installations, use:
```
env\Scripts\pip install -r requirements.txt
```

- Create users app
```terminal
cd djangoapp
..\env\Scripts\python manage.py startapp users
```

- Add users app to settings.py of djangoapp
```python
INSTALLED_APPS = [
    'users.apps.UsersConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

- Add Users model in users\models.py
```python
class User(models.Model):
    user_name = models.CharField(max_length=200)
    user_email = models.CharField(max_length=200)
```

- Run migrate to add Users table to the database
```python
env\Scripts\python djangoapp\manage.py makemigrations users
```



- Turn off DEBUG in djangoapp/settings.py




### Libraries used
---------


### How to run
```terminal
virtual env
env\Scripts\pip install -r requirements.txt
env\Scripts\python djangoapp\manage.py runserver
env\Scripts\python djangoapp\manage.py migrate
```

### References
