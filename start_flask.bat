@echo off
cd /d D:\WebProjects\Schools

:: Activate venv if you have one
:: call venv\Scripts\activate

set FLASK_APP=app.py
set FLASK_ENV=development

:: Run Flask on port 80, accessible at http://myschools.com/
flask run --host=0.0.0.0 --port=80
