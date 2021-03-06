# Password-Locker
### Author
Fridah-Kalee
## Description
This project is a python application that manages login and signup credentials of a person for various accounts i.e. username and passwords for each account. It also stores the passwords and generates a unique password for a user automatically.
## Table of Content
* Description
* User Requirements
* setup and instruction
* Cloning Process
* Running Application
* BDD
* Technology Used
* Known Bugs
* Contact Information
* Licence
 

## User REquirements
The user would like to;
* Create a password locker account with details, a login username and password.
* Store already existing account credentials in the application for various accounts.
* Create new account credentials in the application and have the application generate a random password for me to use when I sign up.
* Have the option of putting in a password that I want to use for the new credential account instead of the generated one.
* View various account credentials and their passwords in the application.
* Delete a credentials account that I no longer need in the application.
## Installation/Setup instructions
The application requires the following installations to run;
* python3.9
## Cloning Process
* Open Terminal{Ctrl+Alt+T}
* git clone https://github.com/Fridah-kalee/Password-Locker.git
* cd Password-Locker
* code .
## Running the Application
To run the application, open the cloned file in terminal and run the following commands:
   * $ chmod +x run.py
   * $ ./run.py

To run test for the application 
   * $ python3.9 passlocker_test.py 
## Behaviour Driven Development
* On the terminal run the command ./run.py

* Creating account
Input: enter 'ca' 
Output: input username and password and it returns your account has been created.

* Login in to an already existing account
Input: enter 'ea'
Ouput: enter your your password and username you signed up with.

* Creating a new credential in the application.
Input: enter 'cc'
Output: enter Account,username,password choose tp to enter or gp for the application to generate a  password for you.

* Find a stored credential based on the account.
Input: enter 'fc'
Output: enter the account you want to search and it returns account details.

* Displaying the accounts. 
Input: enter 'dc' 
Output: returns list of accounts that are available in the application.

* Delete an existing credential that u dont want anymore.
Input: enter 'd'
Output: enter the account name of the credentials you want to delete and it returns true/false according to existance of the account.

* Exit Application
Input: enter 'ex'
Output: the application exists                           
## Technologies Used
* python3.9
## Known Bugs
* All known bugs were fixed (Bug fixed) . Seen any Bug? Feel free to reach me through Email:fridakalee@gmail.com.
## Contact Information
* Incase of any questions or contributions ,you can reach me at [fridakalee@gmail.com]
## License
* MIT License:

* Copyright(c)2022 Fridah kalee

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

