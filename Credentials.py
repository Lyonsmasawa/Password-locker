class Credentials:
    """
    Create new instance of credentials
    """
    def __init__(self, platform, username, password):
        self.platform = platform
        self.username = username
        self.password = password

    def save_cred(self):
        """
        
        """