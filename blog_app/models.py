from django.db import models

# Create your models here.
class Memo(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField('DATE PUBLISHED')
    body = models.TextField()

    def __str__(self):
        return self.title

class KorTexts(models.Model):
    ko_text = models.CharField(max_length=200)


class EngTexts(models.Model):
    en_text = models.CharField(max_length=200)