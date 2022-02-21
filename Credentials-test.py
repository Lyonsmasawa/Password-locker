import unittest
from Credentials import Credentials


class TestCredentials(unittest.TestCase):
    def setUp(self):
        """
            Setup method for the test
        """
        self.new_credentials = Credentials(
            "Facebook", "Lyons", "lyons!")

    def test_init(self):
        """
        Test for new credentials
        """
        self.assertEqual(self.new_credentials.platform, "Facebook")
        self.assertEqual(self.new_credentials.username, "Lyons")
        self.assertEqual(self.new_credentials.password, "lyons!")
    
    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []

    def test_save_cred(self):
        """
        test the save function
        """
        self.assertEqual(len(Credentials.credentials_list), 0)
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_delete_cred(self):
        """
        test if the delete credential works
        """
        self.new_credentials.save_credentials()
        self.new_credentials.delete_cred()
        self.assertEqual(len(Credentials.credentials_list), 0)



if __name__ == '__main__':
    unittest.main()