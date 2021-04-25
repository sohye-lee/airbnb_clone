import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from lists.models import List
from users.models import User
from rooms.models import Room

NAME = 'lists'

class Command(BaseCommand):

    help = f"This command creates many {NAME}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", 
            default=2,
            type=int,
            help="How many lists do you want to create?"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_rooms = Room.objects.all()
        all_users = User.objects.all()
        seeder.add_entity(List, number, {
            "user": lambda x: random.choice(all_users),
        })
        created = seeder.execute()
        cleaned = flatten(list(created.values()))
        for pk in cleaned:
            list_model = List.objects.get(pk=pk)
            to_add = all_rooms[random.randint(0, 5) : random.randint(6, 10)]
            list_model.rooms.add(*to_add)
        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created successfully!"))