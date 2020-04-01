from unittest import TestCase
import scraper.src.places as places

mock_good_result = {"candidates": [{"formatted_address": "1729 Maryland Ave, Baltimore, MD 21201, United States",
                                    "geometry": {"location": {"lat": 39.30948739999999, "lng": -76.61758999999999},
                                                 "viewport": {
                                                     "northeast": {"lat": 39.31083342989272, "lng": -76.61635362010728},
                                                     "southwest": {"lat": 39.30813377010728,
                                                                   "lng": -76.61905327989273}}},
                                    "name": "Le Comptoir du Vin"}], "status": "OK"}

mock_bad_result = {"candidates": [], "status": "ZERO_RESULTS"}


class TestPlaces(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestPlaces, self).__init__(*args, **kwargs)
        self.client = places.create_client()

    def test_create_places_api_service(self):
        self.assertIsNotNone(self.client.key)

    def test_get_place(self):
        good_query = places.get_place(self.client, "le comptoir du vin")
        self.assertEqual(good_query['status'], "OK")
        self.assertGreater(len(good_query['candidates']), 0)

        bad_query = places.get_place(self.client, "dsfdsfsdf bad boy2222")
        self.assertEqual(bad_query['status'], 'ZERO_RESULTS')
        self.assertEqual(len(bad_query['candidates']), 0)

    def test_extract_address(self):
        res = places.extract_address(mock_good_result)
        self.assertEqual(res, "1729 Maryland Ave, Baltimore, MD 21201, United States")
        res = places.extract_location(mock_bad_result)
        self.assertIsNone(res)

