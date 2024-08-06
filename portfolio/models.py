from django.db import models
from ckeditor.fields import RichTextField
from hitcount.models import HitCountMixin,HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return f"{self.name} {self.email}"

class PortfolioCategory(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"

class Portfolio(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Images/portfolio')
    description = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(PortfolioCategory,on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"


class Blog(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='Images/blog')
    created_date = models.DateTimeField(auto_now=True)
    content = RichTextField()

    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self) -> str:
        title = self.title[:10]
        return f"{title}"

class Comment(models.Model):
    full_name = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.message} by {self.full_name}"

# Gallery Books

class GalleryCategory(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Images/gallery_category') 
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"

class Gallery(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Images/gallery') 
    created_date = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(GalleryCategory,on_delete=models.CASCADE)


class Book(models.Model):
    cover = models.ImageField(upload_to='Images/books')
    spine = models.ImageField(upload_to='Images/books')
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    pages = models.IntegerField()
    publication_date = models.DateField()
    publisher = models.CharField(max_length=255)


class Portfolio_single(models.Model):
    image = models.ImageField(upload_to='Images/portfolio_single')
    def __str__(self) -> str:
        return f"{self.image}"