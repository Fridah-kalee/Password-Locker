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

    @classmethod
    def display_user(cls):
        '''
        '''
        return cls.user_list

    @classmethod 
    def delete_user(self):
        '''
        a method that deletes a saved user account
        '''
        User.user_list.remove(self)  
