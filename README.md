# MyChess Application

## Initial Setup
```
cd website/chessProject
python3 manage.py runserver // Ubuntu
python manage.py runserver  // Windows
```
## Virtual Environments

You might need to download [Django](https://docs.djangoproject.com/en/5.1/)
```
pip install django
```

The above may fail for Ubuntu versions 24+. As a result, you may also need to use a virtual environment
```
python3 -m venv venv
pip install django
source venv/bin/activate 
pip install django

```