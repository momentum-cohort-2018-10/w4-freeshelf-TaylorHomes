from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Book(models.Model):
    book_name = models.CharField(max_length = 500)
    author = models.CharField(max_length = 255)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    python = models.BooleanField(default=False)
    css = models.BooleanField(default=False)
    html = models.BooleanField(default=False)
    javascript = models.BooleanField(default=False)
    image = models.ImageField(upload_to='templates/index.html', null=True)
    slug = models.SlugField(unique=True)

    def save(self):
        if not self.id:
            self.slug = slugify(self.name)
        super(Book, self).save()
    
    def get_categories(self):
        categories = []
        if self.python:
            categories.append("Python")
        if self.css:
            categories.append("CSS")
        if self.html:
            categories.append("HTML")
        if self.javascript:
            categories.append("Javascript")
        return categories
    
    def __str__(self):
        return self.title





    