#!/bin/sh
#!/bin/sh
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python manage.py db init
python manage.py db migrate --message 'init db migration'
python manage.py db upgrade
