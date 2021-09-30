from django.db import models
""" a class with 4 attributes for a class database holding the course informtion.  When called will take the input from
the user and imput it into the database in a table with object referance to """
class djangoClasses(models.Model):
    title = models.CharField(max_length=30)
    course_number = models.CharField(max_length=30)
    instructorName = models.CharField(max_length=30)
    duration = models.DecimalField(max_digits=30, decimal_places=2)

