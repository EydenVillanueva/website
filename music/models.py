from django.db import models

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=150)
    album_title = models.CharField(max_length=150)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.album_title + ' - ' + self.artist

class Song(models.Model):
    #on_delete=models.CASCADE quiere decir que cuando borremos un album que este también borre todas las canciones que estan escritas dentro de este album
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)

    def __str__(self):
        return self.song_title + ' - '
        
