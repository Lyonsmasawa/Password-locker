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
def createcred(platform, username, password):
    """
    creates a new credential
    """
    new_cred = Credentials(platform, username, password)
    return new_cred

def savecred(credentials):
    """
    Save user credentials
    """
    credentials.save_cred()

def deletecred(credentials):
    """
    delete credentials
    """
    credentials.delete_cred()

def listcred():
    """
    List credentials stored
    """
    return Credentials.list_creds()

def findplatformcred(platform):
    """
    find credentials based on platform
    """
    return Credentials.find_platform_cred(platform)

def checkexists(platform):
    """
    Checks the existance of a platforms credentials
    """
    return  Credentials.cred_exist(platform)

def generatepasswd(self):
    return Credentials.generate_password(self)

def intro():
    print("          .____                                      __________                                               .___    _____                                                  ")
    print("          |    |    ___.__. ____   ____   ______     \______   \_____    ______ ________  _  _____________  __| _/   /     \ _____    ____ _____     ____   ___________      ")
    print("          |    |   <   |  |/  _ \ /    \ /  ___/      |     ___/\__  \  /  ___//  ___/\ \/ \/ /  _ \_  __ \/ __ |   /  \ /  \\__  \  /    \\__  \   / ___\_/ __ \_  __ \     ")
    print("          |    |___ \___  (  <_> )   |  \\___ \       |    |     / __ \_\___ \ \___ \  \     (  <_> )  | \/ /_/ |  /    Y    \/ __ \|   |  \/ __ \_/ /_/  >  ___/|  | \/     ")
    print("          |_______ \/ ____|\____/|___|  /____  >      |____|    (____  /____  >____  >  \/\_/ \____/|__|  \____ |  \____|__  (____  /___|  (____  /\___  / \___  >__|        ")
    print("                  \/\/                \/     \/                      \/     \/     \/                          \/          \/     \/     \/     \//_____/      \/            ")
    print("                                                                                                                                                                         ")

def main():
    intro()
    print("                   Welcome to my password manager                ")
    print("Please input name")
    name = input().upper()
    if name != "":
         print(f"\n Hello {name}")
         while True:
             print("Please pick one of the options below to proceed (Type it into the console)")
             print("     SignUP ---> New Account       ")
             print("     Login ---> Login to Account       ")
             user_option = input().strip().lower()

             if user_option

if __name__ == '__main__':
    main()