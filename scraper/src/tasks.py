import os.path
import json
import scraper.src.sheets as sheets
import scraper.src.places as places
from scraper.src.config import get_root_path

def create_dataset():
    sheets_client = sheets.create_client()
    places_client = places.create_client()

    spreadsheet_data = sheets.get_neighborhood_data(sheets_client)
    locations = map(lambda x: (x[0], places.get_place(places_client, x[1].Place + x[1].Neighborhood)), spreadsheet_data.iterrows())

    geojson = {
        "type": "FeatureCollection",
        "features": [
        ]
    }

    for index, item in locations:
        props = dict(spreadsheet_data.iloc[index])
        props["Address"] = places.extract_address(item)
        loc = places.extract_location(item)
        geom = loc.as_geojson() if loc else None
        geojson['features'].append(
            places.Feature(
                geometry=geom,
                properties=dict(props)
            ).as_geojson()
        )

    with open(os.path.join(get_root_path(), 'data.json'), "w") as f:
        json.dump(geojson, f)

    return os.path.join(get_root_path(), 'data.json')




