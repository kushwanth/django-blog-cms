from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0,"Draft"),
    (1,"Publish"),
    (2, "Delete")
)

class post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_news')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("news_detail", kwargs={"slug": str(self.slug)})
