from django.contrib import admin
from .models import category, Lesson


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at',)  # Filtering by created date makes more sense for categories


class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'description', 'created_at', 'updated_at')
    search_fields = ('title', 'description')  # Search by lesson title or description
    list_filter = ('category', 'created_at')  # Filter lessons by category or creation date


admin.site.register(category, CategoryAdmin)
admin.site.register(Lesson, LessonAdmin)

