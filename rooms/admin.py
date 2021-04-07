from django.contrib import admin
from . import models

@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ ITEM ADMIN DEFINITION """

    list_display = (
        "name", 
        "used_by",
    )
    
    def used_by(self, obj):
        return obj.rooms.count()
    pass

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ ROOM ADMIN DEFINITION """

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "country", "city", "address", "description", "price")}
        ), 
        (
            "Times", 
            {
                "fields": ("check_in", "check_out", "instant_book")
            }
        ),
        (
            "Spaces", 
            {"fields": ("guests", "beds", "bedrooms", "baths")}
        ), 
        (
            "More About the Space", 
            {
                "classes": ("collapse",),
                "fields": ("room_type", "amenities", "facilities", "house_rules")
            }
        ), 
        (
            "Last Details",
            {"fields": ("host",)}
        ),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
    )

    list_filter = (
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "host__superhost",
        "city", 
        "country",
    )

    ordering = ("price",)
    search_fields = ["city", "name", "country", "address", "host__username"]

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ PHOTO ADMIN DEFINITION """
    list_display = (
        '__str__',
        'get_thumbnail',
    )

    def get_thumbnail(self, obj):
        print(obj.file)
        return "thumb"
    get_thumbnail.short_description = "Thumbnail"