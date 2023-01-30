from django.contrib import admin
from django.utils.html import format_html
from .models import Location, Image
from adminsortable2.admin import SortableInlineAdminMixin


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ['image', ]
    fields = ['location', 'image']

    def image_preview(self, obj):
        return obj.image_preview


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    search_fields = ['title', ]
    inlines = [
        PlaceImageInline,
    ]


@admin.register(Image)
class ImagesAdmin(admin.ModelAdmin):
    fields = ('location', 'image')
