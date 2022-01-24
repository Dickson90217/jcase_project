from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    createdon = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name


class Respondent(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    createdon = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name
