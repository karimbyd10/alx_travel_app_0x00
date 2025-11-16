from django.core.management.base import BaseCommand
from listings.models import Listing
import random


class Command(BaseCommand):
    help = "Seed the database with sample listings"

    SAMPLE_LISTINGS = [
        {
            "title": "Beachfront Villa",
            "description": "A beautiful villa with an ocean view.",
            "price_per_night": 180.00,
            "location": "Agadir, Morocco",
        },
        {
            "title": "Mountain Cabin",
            "description": "A cozy cabin in the mountains.",
            "price_per_night": 120.00,
            "location": "Ifrane, Morocco",
        },
        {
            "title": "City Apartment",
            "description": "Modern apartment in the city center.",
            "price_per_night": 90.00,
            "location": "Casablanca, Morocco",
        },
    ]

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding listings...")

        for data in self.SAMPLE_LISTINGS:
            Listing.objects.get_or_create(
                title=data["title"],
                defaults={
                    "description": data["description"],
                    "price_per_night": data["price_per_night"],
                    "location": data["location"],
                },
            )

        self.stdout.write(self.style.SUCCESS("Successfully seeded listings"))

