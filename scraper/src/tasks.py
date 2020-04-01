import os.path
import json
import scraper.src.sheets as sheets
import scraper.src.places as places
from scraper.src.config import get_root_path

def create_dataset():
    sheets_client = sheets.create_client()
    places_client = places.create_client()

    spreadsheet_data = sheets.get_neighborhood_data(sheets_client)
    locations = map(lambda x: (x[0], places.get_place(places_client, x[1].Place)), spreadsheet_data.iterrows())

    geojson = {
        "type": "FeatureCollection",
        "features": [
        ]
    }

    for index, item in locations:
        props = spreadsheet_data.iloc[index]
        props["address"] = places.extract_address(item)
        geojson['features'].append(
            places.Feature(
                geometry=places.extract_location(item),
                properties=props
            ).as_geojson()
        )

    with open(os.path.join(get_root_path(), 'data.json'), "r") as f:
        json.dump(geojson, f)

    return os.path.join(get_root_path(), 'data.json')




