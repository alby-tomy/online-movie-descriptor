from django.db import models

# Create your models here.
class MovieDetails(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    description = models.TextField()
    img = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name