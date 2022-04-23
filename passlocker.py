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
        return cls.user_list

    @classmethod 
    def delete_user(self):
        '''
        a method that deletes a saved user account
        '''
        User.user_list.remove(self)

class Credentials():
    '''
    create credentials class that creates new objects of credentials
    '''
    credentials_list = [] 

    def __init__(self,account,userName,password):
        self.account = account
        self.userName = userName
        self.password = password

    def save_credentials(self):
        '''
        method that stores new credential object to credential list
        '''
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        a method that deletes credential account from the credential list.
        '''
        Credentials.credentials_list.remove(self)                  
