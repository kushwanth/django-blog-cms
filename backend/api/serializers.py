from rest_framework import serializers
from blog.models import post

class postSerializer(serializers.ModelSerializer):
   class Meta:
       fields = (
      'title',
      'slug',
      'author',
      'updated_on',
      'content',
      'created_on',
      'status',
      )
       model=post
