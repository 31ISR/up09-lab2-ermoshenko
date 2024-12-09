from django.db import models

class community(models.Model):
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=150)
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    free = models.BooleanField(default=False)