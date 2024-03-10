from django.db import models

# Create your models here.
class Movie(models.Model):#Table name is Movie
    moviename=models.CharField(max_length=20)
    moviedesp=models.CharField(max_length=600)
    movieyear=models.CharField(max_length=20)
    movieimage=models.ImageField(upload_to="movieapp/images")

    def __str__(self):
        return self.moviename