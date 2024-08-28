import unittest
from app import create_app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Upload Video', response.data)

    def test_upload_video(self):
        # Implement test for video upload
        pass

if __name__ == "__main__":
    unittest.main()