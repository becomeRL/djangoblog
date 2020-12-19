from django.db import models

# Create your models here.
class Memo(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField('DATE PUBLISHED')
    body = models.TextField()

    def __str__(self):
        return self.title
        
class Photo(models.Model):
    memo = models.ForeignKey(Memo, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

class KorTexts(models.Model):
    ko_text = models.CharField(max_length=200)

class EngTexts(models.Model):
    en_text = models.CharField(max_length=200)

class NewsData(models.Model):
    title = models.CharField(max_length=200)
    
class NewsLink(models.Model):
    link = models.URLField()