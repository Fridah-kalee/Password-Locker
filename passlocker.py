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

    def delete_user(self):
        '''
        a method that deletes a saved user account
        '''
        User.user_list.remove(self)

    @classmethod
    def find_by_user_name(cls,username):
        '''
        method that takes a name and returns a user that matches that username
        Args:
        name:user to search for
        Returns:
        username of the person that matches the name
        '''
        for user in cls.user_list:
            if user.username==username:
                return user        

    @classmethod
    def display_users(cls):
        return cls.user_list


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

    @classmethod
    def find_credential(cls,account):
        '''
        a method that takes in an account_name and returns a credentials that matches account name
        '''
        for credential in cls.credentials_list:
            if credential.account==account:
                return credential

    @classmethod
    def credential_exist(cls,account):
        '''
        method to check if a credential exists from credentials list
        '''
        for credential in cls.credentials_list:
            if credential.account == account:
                return True
                return False                                  
