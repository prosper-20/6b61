from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["headline", "category", "reporter"]
    list_filter = ["category", "reporter", "date_posted"]
    search_fields = ["headline", "reporter"]