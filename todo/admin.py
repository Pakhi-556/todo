from django.contrib import admin
from .models import Task

## the class is created to update the the admin panel to overide the class
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task','is_completed','updated_at')
    search_fields=('task',)

# Register your models here.
admin.site.register(Task,TaskAdmin)
