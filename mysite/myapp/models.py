from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.timezone import make_aware
from django.contrib.auth.models import AbstractUser

from datetime import datetime, timedelta


class MyUser(AbstractUser):
    pass


# class Article(models.Model):
#     name = models.CharField(max_length=100)
#     text = models.TextField(null=True, blank=True)
#
#
# class Author(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name
#
#
# class Person(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name
#
#
# class BookInLibrary(models.Model):
#     name = models.CharField(max_length=100)
#     authors = models.ManyToManyField(Author, through='BooksAuthors')
#     taken = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='person', null=True, blank=True)
#
#     def __str__(self):
#         return self.name
#
#
# class BooksAuthors(models.Model):
#     author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')
#     book = models.ForeignKey(BookInLibrary, on_delete=models.CASCADE, related_name='book')
#
#     def __str__(self):
#         return f"{self.author} '{self.book}'"
#
#
# class Books(models.Model):
#     name = models.CharField(max_length=100)
#     author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name='books', null=True)

# 3

# class AuthorPost(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name


class Post(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField(null=True, blank=True)
    author = models.ForeignKey(MyUser, on_delete=models.SET_NULL, related_name='author_post', null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.SET_NULL, related_name='author_comment', null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comment', null=False, default=0)
    text = models.TextField(null=False, blank=False)
    comment_comment = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    post_at = models.DateTimeField(null=False, blank=True)

    def __str__(self):
        return f"Comment {self.author}"

    def save(self, *arg, **kw):
        self.post_at = datetime.now() - timedelta(days=365)
        if self.post_at.day != datetime.now().day:
            self.post_at -= timedelta(days=1)
        self.post_at = make_aware(self.post_at)
        return super().save(arg, kw)


class Like(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.SET_NULL, related_name='author_like', null=True)
    limit = models.Q(app_label='myapp', model='Comment') | models.Q(app_label='myapp', model='Post')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to=limit)
    object_id = models.PositiveIntegerField(auto_created=True)
    like_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"{self.author}: {self.like_object}"

class Dislike(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.SET_NULL, related_name='author_dislike', null=True)
    limit = models.Q(app_label='myapp', model='Comment') | models.Q(app_label='myapp', model='Post')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to=limit)
    object_id = models.PositiveIntegerField(auto_created=True)
    dislike_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"{self.author}: {self.dislike_object}"