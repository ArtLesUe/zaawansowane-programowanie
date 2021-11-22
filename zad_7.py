import requests
import json


class Brewery:
    def __init__(self, id: str, name: str, brewery_type: str, street: str, address_2: str, address_3: str,
                 city: str, state: str, county_province: str, postal_code: str, country: str, longitude: str,
                 latitude: str, phone: str, website_url: str, updated_at: str, created_at: str):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state = state
        self.county_province = county_province
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url
        self.updated_at = updated_at
        self.created_at = created_at

    def __str__(self):
        linia_1 = f"Browar o ID '{self.id}' o nazwie '{self.name}', typ browaru '{self.brewery_type}', ulokowany przy "
        linia_2 = f"{self.street}, {self.address_2}, {self.address_3}, {self.city}, {self.state}, "
        linia_3 = f"{self.county_province}, {self.postal_code}, {self.country}, w lokalizacji GPS o współżędnych "
        linia_4 = f"({self.longitude}, {self.latitude}), kontakt: {self.phone}, {self.website_url}"
        return linia_1 + linia_2 + linia_3 + linia_4


json_data = requests.get("https://api.openbrewerydb.org/breweries?per_page=20&page=0")
api_data = list()

for line in json.loads(json_data.content):
    api_data.append(Brewery(line['id'], line['name'], line['brewery_type'], line['street'], line['address_2'],
                    line['address_3'], line['city'], line['state'], line['county_province'], line['postal_code'],
                    line['country'], line['longitude'], line['latitude'], line['phone'], line['website_url'],
                    line['updated_at'], line['created_at']))

for line in api_data:
    print(line)
