from django.contrib import admin
from .models import *

# admin.site.register(Item)

@admin.register(EventSite)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'site_title', 'site_nav', 'site_nav_position', 'site_content']
    list_display_links = ['site_title', ]
    list_editable = ['site_nav', 'site_nav_position',]
    search_fields = ['site_content',]
    list_filter = ['site_title', 'site_nav']
    list_per_page = 15
