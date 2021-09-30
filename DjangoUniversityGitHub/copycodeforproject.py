""" my code from the Django Challenge Submission Assignment """

"""from the models.py file"""

from django.db import models
""" a class with 4 attributes for a class database holding the course informtion.  When called will take the input from
the user and imput it into the database in a table with object referance to """
class djangoClasses(models.Model):
    title = models.CharField(max_length=30)
    course_number = models.CharField(max_length=30)
    instructorName = models.CharField(max_length=30)
    duration = models.DecimalField(max_digits=30, decimal_places=2)



"""from the admin.py file"""

    from django.contrib import admin
""" import djangoClasses python class from the classApp.models module """
from .models import djangoClasses

""" register the model classApp.models class djangoClasses to be shown in the admin page """
admin.site.register(djangoClasses)


""" from the settings.py file """

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # added the classApp name to the Main Project setting.py to tell the project that classApp is installed
    'classApp',
