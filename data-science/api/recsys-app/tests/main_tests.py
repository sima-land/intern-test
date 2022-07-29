import unittest
from main import app


class TestApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        app.config['TESTING'] = True
        cls.app = app.test_client()

    def test_main_page(self):

        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_search_request(self):

        response = self.app.post('/search', data=dict(user_id=111))
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
