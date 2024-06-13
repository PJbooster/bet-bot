import json
import requests

from django.core.management.base import BaseCommand, CommandError

from bot_api.services.bet_offer_parser import BetOfferParser

class Command(BaseCommand):
    help = 'Get STS bet offer'
    url = 'https://spoon.sts.pl/offer/?lang=pl'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            data = response.json()
            
            parser = BetOfferParser()
            parsed_data = parser.parse_offers(data, category=BetOfferParser.VOLLYBALL, live_only=False)
            self.save_data_to_json_file(parsed_data, 'offer.json')
        
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    def save_data_to_json_file(self, data, filename):
        try:
            with open(filename, 'w') as json_file:
                json.dump(data, json_file, indent=4)
            print(f'Data successfully saved to {filename}')
        except Exception as err:
            print(f'Error occurred while saving data to JSON file: {err}')
