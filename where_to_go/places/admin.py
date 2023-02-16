from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Location, Image
from adminsortable2.admin import SortableInlineAdminMixin


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ['image_preview']
    fields = ['location', 'image', 'image_preview', 'index']

    def image_preview(self, model):
        try:
            preview = mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
                url=model.image.url,
                width=400,
                height=200,
            )
            )
            return preview
        except Exception as exc:
            print(Exception, exc)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    search_fields = ['title', ]
    inlines = [
        PlaceImageInline,
    ]


@admin.register(Image)
class ImagesAdmin(admin.ModelAdmin):
    fields = ('location', 'image', 'index')
