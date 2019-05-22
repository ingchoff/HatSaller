from django.contrib import admin

from hatseller.models import hat


class hatAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'stock', 'created_by_id']
    list_per_page = 10
    list_filter = ['title', 'stock', 'created_at', 'created_by_id']
    search_fields = ['title']


admin.site.register(hat, hatAdmin)
