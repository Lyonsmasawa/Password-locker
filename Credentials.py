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