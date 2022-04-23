class User:
    '''
    Create User class that generates new instances of users
    '''
    user_list = [] #Empty user list for storing our created user objects.

    def __init__(self, username, password):
        '''
        Method that defines the properties of a user.
        '''
        self.username =username
        self.password =password

    def save_user(self):
        '''
        method that saves user objects into user_list.
        '''
        User.user_list.append(self)