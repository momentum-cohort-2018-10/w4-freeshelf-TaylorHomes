from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length=255) 
    author = models.CharField(max_length=255)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=False)



    