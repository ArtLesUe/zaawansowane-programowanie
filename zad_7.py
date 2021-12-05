import requests
import json

from zadanie_7.Brewery import Brewery


json_data = requests.get("https://api.openbrewerydb.org/breweries?per_page=20&page=0")
api_data = list()

for line in json.loads(json_data.content):
    api_data.append(Brewery(line['id'], line['name'], line['brewery_type'], line['street'], line['address_2'],
                    line['address_3'], line['city'], line['state'], line['county_province'], line['postal_code'],
                    line['country'], line['longitude'], line['latitude'], line['phone'], line['website_url'],
                    line['updated_at'], line['created_at']))

for line in api_data:
    print(line)
