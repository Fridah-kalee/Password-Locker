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

def find_credential(account):
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

def main():
    print("Hello welcome to the Password Locker...\n Please enter one of the following to proceed.\n CA -Create New Account  \n EA- Have an existing Account?  \n")
    short_code = input("").lower().strip()
    if short_code == "ca":
        print("Sign Up")
        print('*' * 40)
        username=input("Username: ")
        while True:
            print("TP- Type your own password:\n GP- To generate random password")
            password_Choice = input("").lower().strip()
            if password_Choice == 'tp':
               password =input("Enter Password\n")
               break
            elif password_Choice =='gp':
                password=generate_Password()
                break    
            else:
                print("Invalid password please try again")
        save_user(create_new_user(username,password))
        print("*"*80)
        print(f"Hello {username}, Your account has been created succesfully! Your password is: {password}")
        print("*"*80)
    elif short_code == "ea":
        print("*"*50)
        print("Enter your User name and your Password to log in:")
        print('*' * 50)
        username = input("User name: ")
        password = input("password: ")
        print(f"Hello {username}.Welcome To PassWord Locker")
        print('\n')
        while True:
            print("Use these short codes:\n CC - Create a new credential \n DC - Display Credentials \n FC - Find a credential \n GP - Generate A random password \n D - Delete credential \n EX - Exit the application \n")
            short_code = input("").lower().strip()
            if short_code == "cc":
                print("Create New Credential")
                print("."*20)
                print("Account name ....")
                account = input("").lower()
                print("Your Account username")
                userName = input("")
                while True:
                    print("TP - To type your own password if you already have an account:\n GP - To generate random Password")
                    password_Choice = input("").lower().strip()
                    if password_Choice == 'tp':
                        password = input("Enter Your Own Password\n")
                        break
                    elif password_Choice =='gp':
                        password_Choice =generate_Password()
                        break
                    else:
                        print("Invalid password please try again")
                save_credentials(create_new_credentials(account,userName,password))
                print('\n')
                print(f"Account Credential for: {account} - UserName: {userName} - Password:{password} created succesfully")
                print('\n')
            elif short_code == 'dc':
                if display_account_details():
                    print("Here's your list of accounts:")
                    
                    for account in display_account_details():
                        print(f" Account:{account.account} \n User Name:{username}\n Password:{password}")
                        
                    else:
                        print("Credentials successfully saved.")
                
            elif short_code == "fc":
                    print("Enter the Account Name you want to search for")
                    search_account = input().lower()
                    if find_credential(search_account):
                        search_credential = find_credential(search_account)
                        print(f"Account Name : {search_credential.account}")
                        print('-' * 50)
                    else:
                        print("That Credential does not exist")
                        print('/n')
            elif short_code=="d":
                    print("Enter the account name of the Credentials you want to delete")
                    search_account = input().lower()
                    if find_credential(search_account):
                        search_credential = find_credential(search_account)
                        print("_"*50)
                        search_credential.delete_credentials()
                        print('\n')
                        print(f"Your stored credentials for : {search_credential.account} successfully deleted!!!")
                        print('\n')
                    else:
                        print("credential you want to delete does not exist")

            elif short_code =='gp':
                password = generate_Password()
                print(f"{password} Has been generated successfully")
            elif short_code =="ex":
                    print("Bye..")
                    break
            else:
                print("Thanks for using passwords keep safe manager")
        else:
            print("Please enter a valid input to continue")


if __name__ == '__main__':

    main()
