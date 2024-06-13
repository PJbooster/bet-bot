

#"orn": "Korea Po\u0142udniowa",
#"ig": 1331891,
#"gpn": "Nierozpocz\u0119ty",
#"mn": "UR FC - Nyanza",
#"sn": "Pi\u0142ka No\u017cna",
#"c2n": "Nyanza",
#"c1n": "UR FC",
from unidecode import unidecode

class BetOfferParser:
    VOLLYBALL = "Siatkowka"

    parsed_fields = {'where': "orn", "id": "ig", "status": "gpn", "category": "sn", "team1": "c1n", "team2": "c2n", "date": "gsttz"}

    def __init__(self):
        pass
    
    def parse_offers(self, data, category=None, live_only=False):

        data_parsed_rows = []
        for row in data:
            value = self.parse_single_offer(row)
        
            if category:
                value = self.category_filter(category, value)

            if not value:
                continue
            
            if live_only and value["status"] == 'Nierozpoczety' or value["status"] == 'Mecz zakonczony':
                pass
            if not live_only and value["status"] == 'Mecz zakonczony':
                pass
            else:
                data_parsed_rows.append(value)

        return data_parsed_rows

    def category_filter(self, category, data):
        if category and category == data['category']:
            return data
        else:
            return None

    def parse_single_offer(self, data_row):
        return_value = {}

        for key, value in self.parsed_fields.items():
            if value in data_row:
                return_value[key] = unidecode(str(data_row[value]))
        
        return return_value
    
    def parse_bet(self, data):
        return data['opportunities']
        

    def get_all_possible_events(self, data): 
        pass




    