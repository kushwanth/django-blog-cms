from django.contrib import admin
from .models import post
from django_summernote.admin import SummernoteModelAdmin

class postadmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

admin.site.register(post, postadmin)
