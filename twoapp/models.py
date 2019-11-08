from django.db import models

# Create your models here.

class Student(models.Model):
    sname = models.CharField(max_length=80)
    sage = models.IntegerField()
    sfees = models.FloatField()

    class Meta:
        db_table = 'studinfo'