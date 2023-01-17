class User:
    def __init__(self, user_name):
        self.user_name = user_name
        self.login_attempts = 2

    def read_login(self):
        print(f"The login times is {self.login_attempts}.")

    def increment_login_attempts(self, times):
        self.login_attempts += times
    
    def reset_login(self):
        self.login_attempts = 0





