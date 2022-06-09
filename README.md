# django-blogiee

A Blog based on Django where users can add, edit, publish and delete posts with additional features of custom  WYSIWYG editor Summernote, TOTP token and Honeypot security for users, with Progressive Web App support, Trusted Web Activity compatiable and Minimal customized Admin Dashboard

## Dependencies(Tested versions) used
- asgiref==3.5.2
- backports.zoneinfo==0.2.1
- bleach==5.0.0
- Django==4.0.5
- django-ipware==4.0.2
- django-otp==1.1.3
- django-summernote==0.8.20.0
- qrcode==7.3.1
- six==1.16.0
- sqlparse==0.4.2
- webencodings==0.5.1

## App features
- Integrated with Django Summernote Editor
- Django Admin security with Django Admin Honeypot and Django OTP
- Responsive Web pages
- custom Progressive Web App(TWA compatiable)

### Instructions to use
- Install Python3
- clone the Repo
```
git clone https://github.com/kushwanth/django-blogiee.git
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

#### django_admin_honeypot app is an extention of [django-admin-honeypot 1.1.0](https://github.com/dmpayton/django-admin-honeypot) project

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

- open the manifest.json file in the django-blogiee/blog/templates folder
- customize the JSON file according to your requirements

```
{
    "name": "Django Blogiee",
    "short_name": "Django Blogiee",
    "description": "PWA for django Blogiee",
    "start_url": "/",
    "display": "standalone",
    "scope": "/",
    "orientation": "any",
    "background_color": "#ffffff",
    "theme_color": "#0A0302",
    "status_bar": "default",
    "icons": [
        {
            "src": "/static/icons/Django-Blogiee.png",
            "sizes": "160x160"
        }
    ],
    "dir": "ltr",
    "lang": "en-US"
}
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
