from django.db import models

# Create your models here.
class Track(models.Model):

    track_title = models.TextField()
    track_author = models.TextField()
    track_album = models.TextField()
    class Meta:
        verbose_name_plural = "Tracks"
    # TODO: implement __str__ method
    def __str__(self): return self.track_title