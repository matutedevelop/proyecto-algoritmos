import unittest

from src.proyecto_algoritmos.DB_writer_reader import DBWriter  # Assuming you have a DBWriter class in db_writer module

class TestDBWriter(unittest.TestCase):

    def setUp(self):
        # Set up any necessary initial state
        self.db_writer = DBWriter()
        self.test_data = {"id": 1, "name": "Test"}

    def test_write_data_success(self):
        # Test successful data writing
        result = self.db_writer.write_data(self.test_data)
        self.assertTrue(result)

    def test_write_data_failure(self):
        # Test data writing failure
        with self.assertRaises(Exception):
            self.db_writer.write_data(None)

    def test_write_data_invalid_format(self):
        # Test data writing with invalid format
        invalid_data = "This is not a dictionary"
        with self.assertRaises(TypeError):
            self.db_writer.write_data(invalid_data)

    def tearDown(self):
        # Clean up any necessary state
        pass

if __name__ == '__main__':
    unittest.main()