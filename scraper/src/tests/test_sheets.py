from unittest import TestCase
import scraper.src.sheets as sheets

class TestSheets(TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSheets, self).__init__(*args, **kwargs)
        self.service = sheets.create_client()

    def test_create_sheets_api_service(self):
        self.assertTrue(self.service._baseUrl, 'https://sheets.googleapis.com/')

    def test_get_sheets(self):
        all_sheets = sheets.get_sheets(self.service)
        hampden_check = list(filter(lambda x: x['properties']['title'] == "Hampden", all_sheets))
        self.assertGreater(len(hampden_check), 0)

    def test_get_neighborhood_data(self):
        neighborhood_data = sheets.get_neighborhood_data(self.service)
        self.assertGreater(len(neighborhood_data),50)
        self.assertEqual(list(neighborhood_data.columns), [*sheets.columns, "Neighborhood"])