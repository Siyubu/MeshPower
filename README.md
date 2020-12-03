# Getting started

### Create the virtual environment

python -m venv venv

### Activate the virtual environment
venv\Scripts\activate

### Install the requirements

pip install -r requirements.txt


### Make and run migrations

python manage.py makemigrations
python manage.py migrate


### Createsuperuser

python manage.py createsuperuser

### Then run the thingy

python manage.py runserver
