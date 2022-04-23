import unittest
from passlock import User

class TestClass (unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()
