from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    population=models.IntegerField()
    GDP=models.FloatField()

def __str__(self):
    return self.name

@property
def states(self):
    return self.state_set.all()

class State(models.Model):
    country=models.ForeignKey(Country,on_delete=models.CASCADE,related_name='state_country')
    name = models.CharField(max_length=50)
    description = models.TextField()
    population = models.IntegerField()
    GDP = models.FloatField()

class City(models.Model):
    state=models.ForeignKey(State,on_delete=models.CASCADE)
    country=models.ForeignKey(Country,on_delete=models.CASCADE)
    description = models.TextField()
    population = models.IntegerField()
    GDP = models.FloatField()

class Town(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    description = models.TextField()
    population = models.IntegerField()
    GDP = models.FloatField()
    Pincode=models.CharField(max_length=10)

class Person(models.Model):
    name=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    town=models.CharField(max_length=50,default='Gangashaher')
    state=models.ManyToManyField(State,default='Rajasthan',related_name='persons')


    #https://www.thebookofjoel.com/rest-framework-dynamic-prefetch-select-related