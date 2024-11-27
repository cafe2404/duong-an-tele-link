from django.contrib import admin
from .models import Link
# Register your models here.
@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'url', 'button_text', 'created_at', 'updated_at')
    search_fields = ('name', 'title', 'url', 'button_text')
    list_filter = ('created_at', 'updated_at')
    