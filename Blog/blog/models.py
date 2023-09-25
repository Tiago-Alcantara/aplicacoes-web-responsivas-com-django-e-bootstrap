from django.db import models
from datetime import datetime
# Create your models here.
class Post(models.Model):
    autor = models.CharField(max_length = 255)
    titulo = models.CharField(max_length= 255)
    sutitulo = models.CharField(max_length= 255)
    counteudo = models.TextField()
    date_publicacao = models.DateTimeField(default=datetime.now())
    