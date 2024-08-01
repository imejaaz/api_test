from django.db import models

class Data(models.Model):
    Title = models.CharField(max_length=100)
    Text  = models.CharField(max_length=2000)

    class Meta:
        verbose_name_plural = "Data"
