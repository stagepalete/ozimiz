from django.contrib import admin
from .models import Course, Category, Course_stream
# Register your models here.

tables = [Course, Category, Course_stream]
admin.site.register(tables)