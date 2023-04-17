from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    rating_author = models.FloatField(default=0.00)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Category(models.Model):
    name_category = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    title = models.CharField(max_length=255)
    text_post = models.TextField()
    datetime_post = models.DateTimeField(auto_now_add=True)
    rating_post = models.FloatField(default=0.00)
    CHOICES = (
        ('PO', 'Post'),
        ('NE', 'New'),
    )
    type_information = models.CharField(max_length=2, choices=CHOICES)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, through='PostCategory')


class PostCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Comment(models.Model):
    text_comment = models.TextField()
    datetime_comment = models.DateTimeField(auto_now_add=True)
    rating_comment = models.FloatField(default=0.00)
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
