from django.contrib import admin
from .models import EmployeeProfile, EmployeeGoals, Note

admin.site.register(EmployeeProfile)
admin.site.register(EmployeeGoals)
admin.site.register(Note)