from django.contrib import admin
""" import djangoClasses python class from the classApp.models module """
from .models import djangoClasses

""" register the model classApp.models class djangoClasses to be shown in the admin page """
admin.site.register(djangoClasses)

