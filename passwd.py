#this file contains the User class and the Credentials class
from curses.ascii import US


class User: 
    
    """
    This class is responsible for generating new instance of a User
    """

    user_list = []

    def __init__(self, user_name, user_passwd):

        """
        Create an instance of the object with the given properties
        """

        self.user_name = user_name
        self.user_passwd = user_passwd

    def save_user(self):
        """
        Adds the new user to the user list above
        """
        User.user_list.append(self)

    def delete_user(self):
        """
        deletes a user from the user list
        """
        User.user_list.remove(self)



