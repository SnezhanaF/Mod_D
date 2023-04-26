from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    rating_author = models.FloatField(default=0.00)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def update_rating(self):
        post_rat = self.post_set.aggregate(postRating=Sum('rating_post'))
        sum_post_rat = 0
        sum_post_rat += post_rat.get('postRating')

        com_rat = self.user.comment_set.aggregate(commentRating=Sum('rating_comment'))
        sum_com_rat = 0
        sum_com_rat += com_rat.get('commentRating')

        self.rating_author = sum_post_rat * 3 + sum_com_rat
        self.save()

class Category(models.Model):
    name_category = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    title = models.CharField(max_length=255)
    text_post = models.TextField()
    datetime_post = models.DateTimeField(auto_now_add=True)
    rating_post = models.FloatField(default=0.00)
    CHOICES = (
        ('AR', 'Статья'),
        ('NE', 'Новость'),
    )
    type_information = models.CharField(max_length=2, choices=CHOICES, default='AR')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.rating_post += 1
        self.save()

    def dislike(self):
        self.rating_post -= 1
        self.save()

    def preview(self):
        return f'{self.text_post[:124]}...'

    def __str__(self):
        return f'{self.title.title()}: {self.text_post}'


class PostCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Comment(models.Model):
    text_comment = models.TextField()
    datetime_comment = models.DateTimeField(auto_now_add=True)
    rating_comment = models.FloatField(default=0.00)
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def like(self):
        self.rating_comment += 1
        self.save()

    def dislike(self):
        self.rating_comment -= 1
        self.save()
