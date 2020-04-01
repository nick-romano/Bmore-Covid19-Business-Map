import json
import os.path
import googlemaps
import pandas as pd
from scraper.src.config import get_root_path

location_bias = "point:39.286241, -76.612729"
fields = ["formatted_address", "name", "geometry"]


class Point:
    def __init__(self, x, y):
        self.type = "Point"
        self.x = x
        self.y = y

    def as_geojson(self):
        return {
            "type": "Point",
            "coordinates": [self.x, self.y]
        }


class Feature:
    def __init__(self, geometry, properties):
        self.geometry = geometry
        self.properties = properties

    def as_geojson(self):
        return {
            "type": "Feature",
            "geometry": self.geometry,
            "properties": self.properties
        }


with open(os.path.join(get_root_path(), 'credentials.json'), "r") as f:
    creds = json.load(f)
    key = creds['maps_api_key']


def create_client():
    gmaps = googlemaps.Client(key=key)
    return gmaps


def get_place(client, place_name):
    query = client.find_place(place_name, location_bias=location_bias, input_type="textquery", fields=fields)
    return query


def extract_location(api_result):
    if len(api_result['candidates']) > 0:
        loc = api_result['candidates'][0]['geometry']['location']
        return Point(loc['lng'], loc['lat'])
    else:
        return None


def extract_address(api_result):
    if len(api_result['candidates']) > 0:
        loc = api_result['candidates'][0]['formatted_address']
        return loc
    else:
        return None


