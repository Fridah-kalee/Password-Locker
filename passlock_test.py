import unittest
from passlock import User
from passlock import Credentials

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



if __name__ == '__main__':
    unittest.main()
