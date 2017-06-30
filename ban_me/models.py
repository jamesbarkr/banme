from django.db import models

# Create your models here.
class Post(models.Model):
    """A saved post from Reddit"""
    title = models.TextField()

    def __str__(self):
        """Return a string representation of the model"""
        return self.title
