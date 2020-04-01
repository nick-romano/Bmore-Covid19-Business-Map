from unittest import TestCase
from scraper.src import tasks


class TestTasks(TestCase):
    def test_create_dataset(self):
        result = tasks.create_dataset()
        self.assertTrue("data.json" in result)