from django.db import models
from django.urls import reverse


# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    available = models.BooleanField(default=True)
    image = models.ImageField(blank=True, null=True)
    price = models.FloatField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pet_id': self.id})
