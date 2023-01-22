from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# i need to write right or diferent to be good at the site?



# class Curiosity(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     # title = models.ForeignKey(Title, on_delete=models.SET_NULL, null=True)
#     curiosity = models.TextField(null=True, blank=True)

#     def __str__(self):
#         return self.curiosity




class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    author = models.CharField(max_length=200)
    about = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author

class Title(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    curiosity = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    title = models.ForeignKey(Title, on_delete=models.SET_NULL, null=True)
    comment = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment[0:50]

