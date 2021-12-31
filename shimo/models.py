from django.db import models

# Create your models here.
class Shimo(models.Model):
    on_air = models.DateField()
    segment = models.TextField()
    address = models.TextField()
    user = models.TextField()
    contents = models.TextField()
    answer = models.TextField()
    pt = models.IntegerField()

    def __str__(self):
        on_air_str = self.on_air.strftime('%Y/%m/%d')
        return on_air_str