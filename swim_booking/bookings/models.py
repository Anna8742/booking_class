from django.db import models
from django.contrib.auth.models import User

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username


class Child(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class SwimClass(models.Model):
    class_name = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    max_students = models.IntegerField(default=15)

    def __str__(self):
        return self.class_name


class Booking(models.Model):
    swim_class = models.ForeignKey(SwimClass, on_delete=models.CASCADE)
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    date_booked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.child.name} - {self.swim_class.class_name}"
