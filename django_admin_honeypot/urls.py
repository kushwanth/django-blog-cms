from django_admin_honeypot import views
from django.urls import path, re_path

app_name = 'django_django_admin_honeypot'

urlpatterns = [
    path('login/', views.AdminHoneypot.as_view(), name='login'),
    re_path(r'^.*$', views.AdminHoneypot.as_view(), name='index'),
]
