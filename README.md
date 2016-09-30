# DjangoApp


### Project specifications
- Operating System platform: Windows
- Python version: 3.5.2
- Pip version: 8.1.1


### Steps I used for writing this app
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


### How to run
```terminal
virtual env
env\Scripts\pip install -r requirements.txt

env\Scripts\python djangoapp\manage.py makemigrations users
env\Scripts\python djangoapp\manage.py migrate

env\Scripts\python djangoapp\manage.py runserver 0.0.0.0:80
```

### References
- https://tutorial.djangogirls.org/
