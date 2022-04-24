#!/usr/bin/env python3.9
from passlocker import User, Credentials

def create_new_user(username,password):
    '''
    Function to create a new user
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def display_user():
    '''
    Function to display existing user
    '''
    return User.display_user()

def login_user(username,password):
    '''
    Function that checks whether a user exist and then login the user in
    '''
    check_user = User.verify_user(username,password)
    return check_user

def create_new_credentials(account,userName,password):
    '''
    Function that creates new credentials for a given account for the user
    '''
    new_credentials = Credentials(account,userName,password)
    return new_credentials

def save_credentials(credentials):
    '''
    Function to save Credentials to the credentials list
    '''
    credentials.save_credentials()

def display_account_details():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()

def delete_credential(credentials):
    '''
    Function that deletes credentials from the credential_list
    '''
    credentials.delete_credentials()

def check_credentials(account):
    '''
    Function that check if a Credentials exists with that account name and return true or false
    '''
    return Credentials.credential_exist(userName)

def find_credential(userName):
    '''
    Function that finds a credential by use of userName and returns credentials about that account
    '''
    return Credentials.find_credential(account)

def generate_Password():
    '''
    generates a random password for the user
    '''
    automatic_password=Credentials.generatePassword()
    return automatic_password

def passlocker():
    print("Hello welcome to the Password Locker...\n Please enter one of the following to proceed.\n CA -Create New Account  \n EA- Already has an existing Account  \n")
    short_code = input("").lower().strip()
    if short_code == "ca":
        print("Sign Up")
        print('*' * 40)
        username=input("User_name: ")
        while True:
            print("TP- Type your own password:\n GP- To generate random password")
            password_Choice = input("").lower().strip()
            if password_Choice == 'tp':
               password =input("Enter Password\n")
               break
            


