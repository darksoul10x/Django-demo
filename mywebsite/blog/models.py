from django.db import models

# Create your models here.
class Blog(models.Model):
    Title = models.CharField(max_length=200)
    Author_Name = models.CharField(max_length=300)
    Content = models.CharField(max_length=1000)
    URL = models.URLField()

    class Meta:
        db_table = 'Blog'