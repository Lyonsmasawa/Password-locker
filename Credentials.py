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