from django.db import models
from django.utils.timezone import now


class Jewellery(models.Model):
    name = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.URLField()
    price = models.IntegerField()
    product_type = models.CharField(max_length=100)
    tags = models.CharField(max_length=1000,default="")
    status = models.BooleanField(default=True)
    created = models.DateField(default=now().date())

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Jewellery"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
