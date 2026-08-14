from django.contrib import admin
from .models import category, Lesson, Tag, Question, Option 





class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at',)  # Filtering by created date makes more sense for categories


class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'description', 'created_at', 'updated_at')
    search_fields = ('title', 'description')  # Search by lesson title or description
    list_filter = ('category', 'created_at')  # Filter lessons by category or creation date
    filter_horizontal = ('tags',)  # Use horizontal filter for ManyToMany field 'tags'


class OptionInline(admin.TabularInline):
    model = Option
    extra = 4  # Number of extra option forms to display in the admin interface


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'lesson', 'created_at', 'updated_at')
    search_fields = ('text',)  # Search by question text
    list_filter = ('lesson', 'created_at')  # Filter questions by lesson or creation date
    inlines = [OptionInline]  # Include the OptionInline for adding options directly from the question admin

# Register your models here.
admin.site.register(category, CategoryAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Tag)  # Register the Tag model with default admin options
admin.site.register(Question, QuestionAdmin) #register the Question model with the custom QuestionAdmin 
admin.site.register(Option)  # Register the Option model with default admin options


