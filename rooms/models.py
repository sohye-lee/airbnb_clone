from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models

class AbstractItem(core_models.TimeStampedModel):

    """ ABSTRACT ITEM """
    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class RoomType(AbstractItem):

    """ ROOM TYPES OBJECT """
    class Meta:
        verbose_name="Room Type"
        ordering = ["name"]


class Amenity(AbstractItem):

    """ AMENITY OBJECT """
    class Meta:
        verbose_name_plural="Amenities"

class Facility(AbstractItem):

    """ FACILITY OBJECT """
    class Meta:
        verbose_name_plural="Facilities"

class HouseRule(AbstractItem):

    """ HOUSE RULL MODEL DEFINITION """
    class Meta:
        verbose_name="House Rule"

class Photo(core_models.TimeStampedModel):
    
    """ PHOTO MODEL DEFINITION """
    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption

class Room(core_models.TimeStampedModel):

    """ ROOM MODEL DEFINITION """
    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_models.User, related_name="rooms", on_delete=models.CASCADE)
    room_type = models.ForeignKey("RoomType", related_name="rooms", on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        words = self.city.split(" ")
        cityname = []
        for word in words:
            cityname.append(str.capitalize(word))
        self.city = ' '.join(cityname)

        words_title = self.name.split(" ")
        titlewords = []
        for word in words_title:
            titlewords.append(str.capitalize(word))
        self.name = ' '.join(titlewords)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={'pk': self.pk})

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rating_average()
            return round(all_ratings / len(all_reviews))
        return 0