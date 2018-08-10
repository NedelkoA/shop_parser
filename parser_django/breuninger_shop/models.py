from django.db import models


class ItemModel(models.Model):
    name = models.CharField(max_length=60)
    brand = models.CharField(max_length=60)
    price = models.FloatField()
    description = models.TextField()
    size = models.TextField(null=True)
    currency = models.CharField(max_length=4, null=True)
    image = models.TextField()

    def __str__(self):
        return self.name
