import unittest
from Client import Client

class TestClient(unittest.TestCase):
    def test_client_connection(self):
        client = Client()
        result = client.connect()
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
