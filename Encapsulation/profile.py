class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) not in range(5, 16):
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if not self.is_len_valid(value) or not self.has_number(value) or not self.has_upper(value):
              raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def is_len_valid(self, password):
        lenn = len(password)
        return True if lenn >= 8 else False

    def has_number(self, password):
        numm = [num for num in password if num.isdigit()]
        return True if numm else False

    def has_upper(self, password):
        upper = [upp for upp in password if upp.isupper()]
        return True if upper else False

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


# profile_with_invalid_password = Profile('My_username', 'My-password')

# profile_with_invalid_username = Profile('Too_long_username', 'Any')

correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)