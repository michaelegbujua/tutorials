from django.db import models


class category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name



#tag model creation
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


# Create your models here.
class Lesson(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey('category', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True)        #included thetags field in the lesson model
    description = models.TextField( blank=True, null=True  )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    




    