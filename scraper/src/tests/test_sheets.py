from unittest import TestCase
import scraper.src.sheets as sheets_client

class TestSheets(TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSheets, self).__init__(*args, **kwargs)
        self.service = sheets_client.create_sheets_api_service()

    def test_create_sheets_api_service(self):
        self.assertTrue(self.service._baseUrl, 'https://sheets.googleapis.com/')

    def test_get_sheets(self):
        all_sheets = sheets_client.get_sheets(self.service)
        hampden_check = list(filter(lambda x: x['properties']['title'] == "Hampden", all_sheets))
        self.assertGreater(len(hampden_check), 0)

    def test_get_neighborhood_data(self):
        neighborhood_data = sheets_client.get_neighborhood_data(self.service)
        neighborhood_data