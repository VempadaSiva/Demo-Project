from django.db import models

class Form(models.Model):
    title=models.CharField(max_length=20)
    des=models.CharField(max_length=20)
    date=models.DateField()
    datee=models.DateField()
