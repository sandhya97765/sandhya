from app import app
import unittest

class TestApp(unittest.TestCase):

    def test_hello(self):
        with app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn('Hello, World!', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()