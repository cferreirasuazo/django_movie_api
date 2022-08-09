from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.TextField()
    is_availiable = models.BooleanField(default=False)
    premiere_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name
