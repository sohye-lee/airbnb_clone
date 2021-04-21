from django.core.management.base import BaseCommand
from rooms.models import HouseRule

class Command(BaseCommand):

    def handle(self, *args, **options):
        rules = [
            "No smoking",
            "No parties or events",
            "No pets/Pets allowed",
            "No unregistered guests",
            "No food or drink in bedrooms",
            "No loud noise after 11 PM",
        ]

        for f in rules:
            HouseRule.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f'{len(rules)} house rules created!'))
