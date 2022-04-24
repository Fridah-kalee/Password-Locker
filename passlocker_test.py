import unittest
from passlocker import User
from passlocker import Credentials

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    Args:
    unittest.TestCase:TestCase class that helps in creating test class
    '''
    def setUp(self):
        '''
        Set up method that runs before each test case for individual
        '''
        self.new_user = User('FridahKalee', 'Kate@16z')

    def test_init(self):
        '''
        A test case method to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username,'FridahKalee')
        self.assertEqual(self.new_user.password,'Kate@16z')

    def test_save_user(self):
        '''
        test case to test if the user object is saved into the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
        '''
        a method that cleans up after each test case has run
        '''
        User.user_list =[]    

    def test_save_multiple_user(self):
        '''
        a method to check if we can save multiple user objects to our user_list
        '''
        self.new_user.save_user()
        test_user=User('Test','sw5TF2!')
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_display_all_users(self):
        '''
        a method that displays all users stored in user list
        '''
        self.assertEqual(User.display_users(),User.user_list)

    def test_delete_user(self):
        '''
        a method to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user=User('Test','sw5TF2!')
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

    def test_find_user_by_name(self):
        '''
        a test method to find a user by username
        '''
        self.new_user.save_user()
        test_user = User('Test','sw5TF2!')
        test_user.save_user()

        test_user=User.find_by_user_name('Test')
        self.assertEqual(test_user.username,test_user.username)              

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for credentials class.
    '''
    def setUp(self):
        '''
        A set up method that runs before each individual credentials test methods.
        '''
        self.new_credential=Credentials('Telegram','Fridah_Kalee','gT8@2z!')
    def test_init(self):
        '''
        Test method to check if new credential is instantiated properly.
        ''' 
        self.assertEqual(self.new_credential.account,'Telegram')
        self.assertEqual(self.new_credential.userName,'Fridah_Kalee')
        self.assertEqual(self.new_credential.password,'gT8@2z!')

    def test_save_credential(self):
        '''
        Test case to test if credentials are saved.
        '''
        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list =[]

    def test_save_multiple_accounts(self):
        '''
        a test method to check if we can save multiple credentials account to the credentials list.
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials('Twitter','CuteBabra','Kl4z@h4')
        test_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credentials(self):
        '''
        test method to test if we can remove an account credentials from credentials list
        ''' 
        self.new_credential.save_credentials()
        test_credential = Credentials('Twitter','CuteBabra','Kl4z@h4')
        test_credential.save_credentials()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_credential(self):
        '''
        test to check if we can find user credential based on the credentials
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials('Twitter','CuteBabra','Kl4z@h4')
        test_credential.save_credentials()

        the_credential = Credentials.find_credential('Twitter')
        self.assertEqual(the_credential.account,test_credential.account)

    def test_credential_exists(self):
        '''
        a test method to check if credential exists if yes it returns true 
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials('Twitter','CuteBabra','Kl4z@h4')
        test_credential.save_credentials()

        credential_exists =Credentials.credential_exist('Twitter')
        self.assertTrue(credential_exists)

    def test_display_all_saved_credentials(self):
        '''
        test method that returns a list of all credentials saved
        '''
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)   


if __name__ == '__main__':
    unittest.main()
