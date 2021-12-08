# Extension of [django-blogiee](https://django-blogiee.herokuapp.com)

A Blog based on Django where users can add, edit, publish and delete posts with additional features of custom  WYSIWYG editor Summernote, TOTP token and Honeypot security for users, with Progressive Web App support, Trusted Web Activity compatiable and Minimal customized Admin Dashboard

![logo](https://github.com/codekushi/django-blogiee/blob/master/blog/static/icons/Django-Blogiee.png?raw=true)

## Dependencies used
- django
- django-summernote
- django-otp
- django-admin-honeypot
- django-rest-framework

You can deploy the app in any hosting service that supports Django. You can use my [Digitalocean referral link](https://m.do.co/c/7d066b069429) and get $100 credit for 60 days

## App features
- Integrated with Django Summernote Editor
- Django Admin security with Django Admin Honeypot and Django OTP
- Responsive Web pages with Dark Mode
- custom Progressive Web App(TWA compatiable)

### Instructions to use
- Install Python3
- clone the Repo
```
git clone https://github.com/codekushi/django-blogiee.git
```
- install Dependencies
```
pip install -r requirements.txt
```
- run the following commands
```
python manage.py makemigrations
python manage.py makemigrations blog
python manage.py migrate
python manage.py runserver
```
## Now you can see the home page by going to 127.0.0.1:8000

## I am working under development of transforming [PWA](https://django-blogiee.herokuapp.com) into APK using [Trusted web activity(TWA)](https://github.com/codekushi/django-blogiee/blob/deploy-twa/twa-app/app-release-signed.apk) whose code is in [deploy-twa](https://github.com/codekushi/django-blogiee/tree/deploy-twa) branch

## [deploy-twa](https://github.com/codekushi/django-blogiee/tree/deploy-twa) branch contains [deployed website](https://django-blogiee.herokuapp.com) and APK file for the deployed wesite built using Trusted Web Activity(TWA) using [Bubblewrap](https://github.com/GoogleChromeLabs/bubblewrap)

## Customizing Django Blogiee

### open the templates folder in the blog folder and open home.html file with your favourite editor
```
<h1 class=""h2""> Welcome to <strong>[your blog name]</strong></h1>
```

### Now we are going to customize the django admin dashboard

move into django-blogiee folder and open the urls.py file with your editor

```
admin.site.site_header = <your site header>
admin.site.site_title = <your site title>
admin.site.index_title = <admin title>
admin.empty_value_display = '**Empty**'
```

### Customizing logo image

- open the static folder in the blog folder
- open the icons folder in static
- remove the default logo and place your image with name logo.png to avoid name collosions


### Customizing the Progressive web app data

- open the settings.py file in the django-blogiee folder
- go to progressive web app data line and add your own details
- you can also change theme color and background color if you wish

```
PWA_APP_NAME = '[your app name]'
PWA_APP_DESCRIPTION = ""[your app description]""
PWA_APP_THEME_COLOR = '#0A0302'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [
    {
        'src': '/static/icons/logo.png',
        'sizes': '160x160'
    }
]
PWA_APP_ICONS_APPLE = [
    {
        'src': '/static/icons/logo.png',
        'sizes': '160x160'
    }
]
PWA_APP_SPLASH_SCREEN = [
    {
        'src': '/static/icons/logo.png',
        'media': '(device-width: 320px) and (device-height: 640px) and (-webkit-device-pixel-ratio: 2)'
    }
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'
```

### Enabling OTP safety for your blog
- open the django admin dashboard with superuser access
- go to TOTP devices and click add button
- add user and add the device name and click save
- open your authenticator app and scan the Qr code by clicking the qr code option
- logout and open the urls.py file in the django-blogiee folder
- remove the comment in the 24th and make it as interpretable line
```
admin.site.__class__ = OTPAdminSite #remove the comment fom this line
```
### If you are familiar with Django you can customize more
