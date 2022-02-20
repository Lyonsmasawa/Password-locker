

import random
import string


class Credentials:
    """
    Create new instance of credentials
    """
    crendetials_list = []

    def __init__(self, platform, username, password):
        self.platform = platform
        self.username = username
        self.password = password

    def save_cred(self):
        """
        Saves the new credentials to the credentials list
        """
        Credentials.crendetials_list.append(self)

    @classmethod
    def list_creds():
        """
        lists the existing credentials
        """
        return Credentials.crendetials_list

    def delete_cred(self):
        """
        Deletes credentias from the credential List
        """    
        Credentials.crendetials_list.remove(self)

    @classmethod
    def find_platform_cred(cls, platform):
        """
        Find saved credential by platform
        """
        for cred in cls.credentials_list:
            if cred.platform == platform:
                return cred

    def cred_exist(cls, platform):
        """
        Checks if a credential exists
        """
        for cred in cls.credentials_list:
            if cred.platform == platform:
                return True
        return False

    def generate_password(passwordLength):
        '''
        method that generates a random password for the user
        '''
        generated = string.ascii_letters + string.digits + "!"
        gen_password = ''.join(random.choice(generated) for i in range(2,11))
        return gen_password