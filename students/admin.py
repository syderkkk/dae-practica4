from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'last_name', 'first_name', 'email', 'career', 'semester', 'is_active']
    list_filter = ['career', 'semester', 'is_active', 'created_at']
    search_fields = ['first_name', 'last_name', 'email', 'student_id']
    list_editable = ['is_active']
    ordering = ['last_name', 'first_name']