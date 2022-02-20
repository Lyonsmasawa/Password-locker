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

    @classmethod
    def verify_username(cls, user_name):
        """
        looks up username in Users List
        """
        for user in User.user_list:
            if user.user_name == user_name:
                return user

    @classmethod
    def verify_username_and_password(cls, user_name, passwd):
        """
        verify user by looking up the username and password of the given user
        """
        for user in User.user_list:
            if user.user_name == user_name and user.passwd == passwd:
                return True
        return False



