from . import views
from django.urls import path, include

urlpatterns = [
    path('post/', views.postlist.as_view()),
    path('post/<slug>/', views.postdetail.as_view()),
]
