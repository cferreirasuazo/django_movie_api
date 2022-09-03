from django.db import models

# Create your models here.
class Movie(models.Model):
    """
    {
        "title": "CharField",
        "imgUrl": "TextField",
        "releaseDate": "DateTimeField",
        "createdAt": "DateTimeField",
        "editedAt": "DateTimeField",
        "runtime": "IntegerField",
        "plot": "TextField",
        "omdbJson": "JSONField"
    }
    """
    title = models.CharField(max_length=255)
    imgUrl = models.TextField()
    releaseDate = models.DateTimeField()
    createdAt = models.DateTimeField(auto_now_add=True)
    editedAt = models.DateTimeField(auto_now=True)
    runtime = models.IntegerField()
    plot = models.TextField()
    omdbJson = models.JSONField()
    
    def __str__(self):
        return f'{self.title} ({self.releaseDate.year})'