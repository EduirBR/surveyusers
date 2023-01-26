# surveyusers

A Simple API to show off a little practice of Python Django

- download and install python (add it to path)
  https://www.python.org/downloads/

- Open cmd or powershell with adm permisons
- pip install virtualenv

- move to thge folder where this project went clonned at cmd (or open cmd here)

- virtualenv env #this create a virtual enviroment called 'env'

- env/scripts/activate #to activate the virtual enviroment (deactivate to desactivate)

- pip install -r requirements.pip #inside the (env)

- python manage.py migrate (to build the tables inside the database)

- python manage.py seedcountries (to set the countries inside the database)

- python manage.py runserver 0.0.0.0:8000 (# the 8000 is any number, unless you use my demo front)

demo front at: https://github.com/EduirBR/ConsumerAPIJsVanilla
