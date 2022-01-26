from tkinter import CASCADE
from django.db import models
from user.models import Profile,Respondent
from django.db.models.deletion import CASCADE,SET_NULL

# Create your models here.
#Category
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    createdon = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name

#Amount
class Amount(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    createdon = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name

#Mode
class Mode(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    createdon = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name

#State
class State(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    createdon = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name

#Period
class Period(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    createdon = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name

class Case(models.Model):
    owner=models.ForeignKey(Profile,on_delete=CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    contact = models.CharField(max_length=100)
    skill = models.TextField(null=True, blank=True)
    createdon = models.DateTimeField(auto_now_add=True)
    view = models.IntegerField(default=0)
    
    
    category = models.ForeignKey(Category, null=True,on_delete=SET_NULL)
    amount = models.ForeignKey(Amount, null=True, on_delete=SET_NULL)
    period = models.ForeignKey(Period, null=True, on_delete=SET_NULL)
    respondent = models.ManyToManyField(Respondent)
    state = models.ForeignKey(State, null=True, on_delete=SET_NULL)
    mode = models.ManyToManyField(Mode)
    
    class Meta:
        ordering = ['-createdon']

    def __str__(self):
        return self.title
