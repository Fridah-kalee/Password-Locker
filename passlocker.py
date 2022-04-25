import random
import string
import pyperclip
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
    def display_users(cls):
        return cls.user_list

    @classmethod
    def verify_user(cls,username,password):
        '''
        a method to verify if the user is in our user_list or not
        '''
        user=''
        for user in User.user_list:
            if(user.username == username and user.password == password):
                user ==user.username
        return user    


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

    @classmethod
    def display_credentials(cls):
        '''
        method that returns a list of all credentials.
        '''
        return cls.credentials_list

    def generatePassword(stringLength=7):
        '''
        Generate a random password string of letters,digits and special characters
        '''
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "@^!&$*#"
        return ''.join(random.choice(password)for i in range(stringLength))

    @classmethod
    def copy_password(cls,account):
        found_credentials = Credentials.find_credential(account)
        pyperclip.copy(found_credentials.password)                                                      
