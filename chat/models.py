from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class BlogUser(AbstractBaseUser):
    name = models.CharField(max_length=50,blank=False)
    bio = models.TextField(blank=True)
    Address = models.CharField(max_length=500, blank=False)
    email = models.EmailField(unique=True,blank=False)
    occupatioin = models.CharField(max_length=30)
    avatar = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=100, blank=False)
    desciption = models.TextField(blank=True)
    participant = models.ManyToManyField(BlogUser,blank=True)
    host = models.ForeignKey(BlogUser, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-updated', '-created']
class BlogPost(models.Model):
    group = models.ForeignKey(Group,on_delete=models.DO_NOTHING)
    user = models.ForeignKey(BlogUser,on_delete=models.DO_NOTHING)
    body = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.body[:50]
    class Meta:
        ordering = ['-created','-updated']
class Attachments(models.Model):
    user = models.ForeignKey(BlogUser,on_delete=models.DO_NOTHING)
    post = models.ForeignKey(BlogPost,on_delete=models.CASCADE)
    group = models.ForeignKey(Group,on_delete=models.DO_NOTHING)
    images = models.ImageField()