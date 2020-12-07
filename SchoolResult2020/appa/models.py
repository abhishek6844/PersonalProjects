from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=256)
    standard = models.PositiveSmallIntegerField()
    marks = models.PositiveBigIntegerField()


    def __str__(self):
        return self.name

