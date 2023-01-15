from django.test import TestCase

# Class for Testing  
class API_APP_Test(TestCase):

    # Testing 'check/' endpoint
    def test_check_user_exists(self):
        response = self.client.get('/api/check/google')
        self.assertEqual(response.status_code, 200)

    def test_check_user_does_not_exists(self):
        response = self.client.get('/api/check/agfcjhgafcjag')
        self.assertEqual(response.status_code, 404)

    # Testing 'detail/' endpoint
    def test_get_user_details(self):
        response = self.client.get('/api/detail/google')
        self.assertEqual(response.status_code, 200)

    def test_get_invalid_user_details(self):
        response = self.client.get('/api/detail/agfcjhgafcjag')
        self.assertEqual(response.status_code, 404)

    # Testing 'repos/' endpoint
    def test_get_user_repo_details(self):
        response = self.client.get('/api/repos/google?per_page=10&page=1')
        self.assertEqual(response.status_code, 200)


    def test_get_invalid_user_repo_details(self):
        response = self.client.get('/api/repos/agfcjhgafcjag?per_page=10&page=1')
        self.assertEqual(response.status_code, 404)