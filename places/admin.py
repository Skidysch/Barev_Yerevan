from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Place, Category


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time_create',
                    'get_html_photo', 'is_published')
    list_display_links = ('id', 'name')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create', 'categories')

    fields = ('name', 'slug', 'categories', 'photo',
              'get_html_photo', 'address', 'description',
              'time_create', 'time_update', 'is_published')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width=50')

    get_html_photo.short_description = 'Miniature'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Place, PlaceAdmin)
admin.site.register(Category, CategoryAdmin)
