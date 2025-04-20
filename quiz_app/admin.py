from django.contrib import admin
from .models import Question

# Register your models here.
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "correct_option")  # Display in admin panel
    search_fields = ("text",)