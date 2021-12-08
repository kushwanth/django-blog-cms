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

admin.site.site_header = 'Django Blogiee Reacted'
admin.site.site_title = 'Django Blogiee Reacted'
admin.site.index_title = 'Django Blogiee Reacted Administration'
admin.empty_value_display = '**Empty**'

urlpatterns = [
    path('blogieeadmin/', admin.site.urls),
    path('', include('blog.urls')),
    path('api/', include('api.urls')),
    path('summernote/', include('django_summernote.urls')),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
