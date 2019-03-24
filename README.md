# HRPlat
HR Platform (HRPlat)
________________________________________________________________________________

This HR website is designed for users to be able to register, login and make their profiles, save notes and goals. This technically could be used for a company to maintain their own working environment and all information about their employees.
This website was made using HTML/CSS/Vue.js for the frontend development and Django/Python/SQLite for the backend.

#Prerequisites
________________________________________________________________________________

    Pip
    Python 3.5/3.6/3.7
    Django 2.1
    Crispy-forms        #for html styling to use forms, which can be submitted by user 
    Rest_framework      #for Django Rest APIs
    Terminal

#Installation
________________________________________________________________________________

    sudo apt-get update
    sudo apt-get install python3.6
    sudo apt install python3-pip
    alias python=python3      or       alias python='/usr/bin/python3'
    git clone git://github.com/django/django.git
    pip install -e django/
    pip install django-crispy-forms
    pip install djangorestframework
    pip install markdown       # Markdown support for the browsable API.
    pip install django-filter  # Filtering support
    pip install -U django   or    pip3 install -U django    or    pip install --upgrade django   #if it is not Django 2.1 version

    or git clone https://github.com/encode/django-rest-framework

    Hint: if you receive "permission denied" error when using any of these commands, please try adding sudo in the beginning of the command.

#Implementation
________________________________________________________________________________

    In order to run the backend just type the commands
    cd test_project
    python manage.py runserver

    After that you can open any browser such as Google Chrome/Firefox/Internet Explorer/Microsoft Edge and navigate into 
    http://localhost:8000/
    or
    http://127.0.0.1:8000/
