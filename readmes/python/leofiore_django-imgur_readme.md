# django-imgur
> Version 0.0.1

# What

django-imgur is a Django App that contains a Django Storage which uses Imgur.
Inspired, based, and forked from [django-dropbox](https://github.com/andres-torres-marroquin/django-dropbox)

# Installing

## First of all

    pip install -e git+http://github.com/leofiore/django-imgur#egg=django-imgur

## Add it to your Django Project

INSTALLED_APPS on settings.py

    INSTALLED_APPS = (
        ...
        'django_imgur',
        ...
    )

additionally you must need to set the next settings:

    IMGUR_CONSUMER_ID = "xxx"
    IMGUR_CONSUMER_SECRET = "xxx"
    IMGUR_USERNAME = "xxx"
    IMGUR_ACCESS_TOKEN = "xxx"
    IMGUR_ACCESS_TOKEN_REFRESH = "xxx"

if you don't have `IMGUR_CONSUMER_ID` or `IMGUR_CONSUMER_SECRET` 
you will need to create an Imgur app 
then set `IMGUR_CONSUMER_ID` and `IMGUR_CONSUMER_SECRET` settings in `settings.py`,
after that run:

    $ python manage.py get_imgur_token

And follow up on screen instructions, finally set the `IMGUR_ACCESS_TOKEN` and `IMGUR_USERNAME` in `settings.py`
