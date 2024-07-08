from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=100)
    no_movies = models.IntegerField()
    place = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    language = models.CharField(max_length=50)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
