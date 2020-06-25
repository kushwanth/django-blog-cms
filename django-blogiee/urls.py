"""blogiee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import postSitemap
from django_otp.admin import OTPAdminSite

'''admin.site.__class__ = OTPAdminSite'''  #remove the comment from this line and replace it with "admin.site.__class__ = OTPAdminSite"

sitemaps = {
    "post": postSitemap,
}

admin.site.site_header = 'Django Blogiee'
admin.site.site_title = 'Django Blogiee'
admin.site.index_title = 'Django Blogiee Administration'
admin.empty_value_display = '**Empty**'

urlpatterns = [
    path('djangoblogieeadmin/', admin.site.urls),
    path('', include('blog.urls')),
    re_path('', include('pwa.urls')),
    path('summernote/', include('django_summernote.urls')),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
