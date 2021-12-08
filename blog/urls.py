from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.postlist.as_view(), name='posts'),
    path('post/<slug:slug>/', views.postdetail.as_view(), name='post_detail'),
    path('post/amp/<slug:slug>/', views.postdetailamp.as_view(), name='post_detail_amp'),
    path('manifest.json', views.manifest, name='manifest.json'),
    path('serviceworker.js',views.sw, name='serviceworker.js'),
    path('offline', views.offline, name='offline'),
]
