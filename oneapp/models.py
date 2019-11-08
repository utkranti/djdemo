from django.db import models

# Create your models here.

class Employee(models.Model):
    ename = models.CharField(max_length=80)
    eage = models.IntegerField()
    esal = models.FloatField()

    class Meta:
        db_table = 'empinfo'