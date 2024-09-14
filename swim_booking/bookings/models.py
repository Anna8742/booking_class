from django.db import models
from django.contrib.auth.models import User

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Child(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

class Class(models.Model):
    date = models.DateField()
    time = models.TimeField()
    max_children = models.IntegerField(default=10)
    
    def __str__(self):
        return f"Class on {self.date} at {self.time}"

class Booking(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    swim_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    payment_confirmed = models.BooleanField(default=False)

    class Meta:
        unique_together = ['child', 'swim_class']
