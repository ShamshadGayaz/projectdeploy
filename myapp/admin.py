from django.contrib import admin
from .models import FrontPageImage

@admin.register(FrontPageImage)
class FrontPageImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title',)
    list_editable = ('is_active',)
    fields = ('title', 'image', 'is_active')
