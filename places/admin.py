from django.contrib import admin
from .models import Place
class PlaceAdmin(admin.ModelAdmin):
    date_heirarchy=['time']
    list_display=['title','price','active']
    search_fields=['title','price']
    list_editable=['price','active']
    list_filter=['price','active']
    readonly_fields=['time']
    prepopulated_fields={"slug":("title",)}
    class Meta:
        model=Place
admin.site.register(Place, PlaceAdmin)


