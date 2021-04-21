import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from django.contrib.admin.utils import flatten
from rooms import models as room_models
from users import models as user_models

class Command(BaseCommand):

    help = "This command creates rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="please put the number of rooms you want to create i.e. '--number 10'"
        )
    
    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        seeder.add_entity(
            room_models.Room, 
            number, 
            {
                'name': lambda x: seeder.faker.address(),
                'host': lambda x: random.choice(all_users),
                'room_type': lambda x: random.choice(room_types),
                'guests': lambda x: random.randint(1, 12),
                'price': lambda X: random.randint(10, 300),
                'beds': lambda X: random.randint(1, 5),
                'bedrooms': lambda X: random.randint(1, 5),
                'baths': lambda X: random.randint(1, 5),
            }
        )
        created_photos = seeder.execute()
        created_clean = flatten(created_photos.values())
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        rules = room_models.HouseRule.objects.all()
        for pk in created_clean:
            room = room_models.Room.objects.get(pk=pk)
            for i in range(3, random.randint(8, 12)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"room_photos/seed{random.randint(1, 12)}.jpg",
                )
            for a in amenities:
                num = random.randint(0, 15)
                if num % 2 == 0:
                    room.amenities.add(a)
            for f in facilities:
                num = random.randint(0, 15)
                if num % 2 == 0:
                    room.facilities.add(f)
            for r in rules:
                num = random.randint(0, 15)
                if num % 2 == 0:
                    room.house_rules.add(r)

        self.stdout.write(self.style.SUCCESS(f"{number} rooms have been successfully created!"))


