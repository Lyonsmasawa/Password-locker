from User import User
from Credentials import Credentials

#deals with user class
def createuser(user_name, user_passwd):
    """
    Create user account
    """
    new_user = User(user_name, user_passwd)
    return new_user

def saveuser(new_user):
    """
    Save new user account
    """
    new_user.save_user()

def deleteuser(new_user):
    """
    Delete user account
    """
    new_user.delete_user()

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
    # Introduction
    intro()
    print("                   Welcome to my password manager                ")
    print("Please input name")
    name = input().upper()
    if name != "":
         print(f"\n Hello {name}")
    else:
        print(" Hello ANONYMOUS ")

    print("Please pick one of the options below to proceed (Type it into the console)")
    print("     sign ---> New Account       ")
    print("     login ---> Login to Account       ")
    user_option = input().lower().strip()

    # Sign Up Logic
    if user_option == "sign":
        print("Sign Up to Password Locker")
        print("        ")
        print(            " | "   "*" * 30," | "          )
        print("        ")
        user_name = input("Enter preferred username: "  ).upper()
        while True:
            print(f"       \n     Username: {user_name} "   )
            print("Please pick one password option below to proceed (Type it into the console)")
            print("     create ---> Create password     ")
            print("     gen ---> generate password      ")
            pass_option = input().lower().strip(' ')

            if pass_option == "create":
                user_passwd = input(" Enter preffered Password: ")
                break
            elif pass_option == "gen":
                user_passwd = ""
                user_passwd = generatepasswd(user_passwd)
                break
            else:
                print(" please select an available option!!! ")
    
        # save new user
        saveuser(createuser(user_name,user_passwd))
        print("   Account created successfully   ")
        print(            " | "   "*" * 30," | "          )
        print("        ")
        print(f" Username: {user_name}, Password: {user_passwd}  ")

     # Login Logic
    elif user_option == "login":
        print(            " | "   "*" * 30," | "          )
        print("        ")
        print("Login to your Password Locker Account")
        print("        ")

        user_name = input("Enter your username: ").strip(' ').upper()
        user_passwd = input(" Enter your Password: ").strip(' ')

        if verifyusernameandpasswd(user_name, user_passwd):
            print(" Login successful")

            
        else:
           while True:
                print("Please pick one of the options below to proceed (Type it into the console)")
                print("     New ---> new credential       ")
                print("     Delete ---> delete a credential    ")
                print("     List ---> list existing credential    ")
                print("     exit ---> exit application    ")
                user_option2 = input().lower().strip()

                if user_option2 == "new":
                    platform = input(" Enter Platform to proceed ").lower().strip(" ")
                    username = input("Enter platform usernamr here . . . ")
                    while True:
                        print("Please pick one password option below to proceed (Type it into the console)")
                        print("     create ---> Create password     ")
                        print("     gen ---> generate password      ")
                        pass_option2 = input().lower().strip(' ')

                        if pass_option2 == "create":
                            password = input(" Enter preffered Password: ")
                            break
                        elif pass_option2 == "gen":
                            password = ""
                            password = generatepasswd(password)
                            break
                        else:
                            print(" please select an available option!!! ")
                    # save new user
                    savecred(createcred(platform, username,password))
                    print("   Credentials added successfully   ")
                    print(            " | "   "*" * 30," | "          )
                    print("        ")
                    print(f" Platform: {platform} Username: {username}, Password: {password}  ")
                    break
                elif user_option2 == "delete":
                    platformname = input(" Enter Platform Name: ").lower().strip(" ")
                    credtodel = findplatformcred(platformname)
                    credtodel.deletecred()  
                    print(" Credential deleted successfully")
                elif user_option2 == "list":
                    if listcred():
                        print("         Saved Credentials      ")
                        for cred in listcred():
                         print(f"Platform: {Credentials.platform}   Username: {Credentials.username} Password: {Credentials.password}")
                        else:
                            print("List is empty at the moment")
                elif user_option2 == "exit":
                    print("See you later!")
                    break
                else:
                    print("please restart the application")
 
if __name__ == '__main__':
    main()