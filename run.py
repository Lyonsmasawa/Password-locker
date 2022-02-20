from curses.ascii import CR
from hashlib import new
from User import User
from Credentials import Credentials

#deals with user class
def createuser(user_name, user_passwd):
    """
    Create user account
    """
    new_user = User(user_name, user_passwd)
    return new_user

def saveuser(user):
    """
    Save new user account
    """
    user.save_user()

def deleteuser(user):
    """
    Delete user account
    """
    user.delete_user()

def verifyuser(user_name):
    """
    Verify user using the username
    """
    return User.verify_username(user_name)

def verifyusernameandpasswd(user_name, user_passwd):
    """
    Verify the user and password exists in the given lists
    """
    return User.verify_username_and_password(user_name, user_passwd)

# mostly deals with credentials class
def create_credentials(platform, username, password):
    """
    creates a new credential
    """
    new_cred = Credentials(platform, username, password)
    return new_cred

 