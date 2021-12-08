from django.contrib.sitemaps import Sitemap
from .models import post

class postSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return news.objects.filter(status=1)

    def lastmod(self, obj):
        return obj.updated_on
