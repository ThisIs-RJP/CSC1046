# MyChess Application

## NOTE
Please change branch to `prod`

```
git checkout prod
```

Our main branch is considered our `dev` environment. Much *redundant* code may be left in this branch.

`prod` however, will have the most refined changes. So please switch to this branch when using our application.

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