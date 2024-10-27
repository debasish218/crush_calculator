from django.db import models

class MyData(models.Model):
    name1 = models.CharField(max_length=100)
    name2 = models.CharField(max_length=100)

    def __str__(self):
        return self.name1