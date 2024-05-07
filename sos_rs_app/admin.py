from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('created', 'name', 'age', 'missing_date', 'founded')

