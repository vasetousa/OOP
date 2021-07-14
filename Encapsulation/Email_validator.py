class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        data = email.split("@")
        username = data[0]
        email_part_domain = data[1]
        email_part_data = email_part_domain.split('.')
        email_part = email_part_data[0]
        domain_part = email_part_data[1]
        if self.__is_name_valid(username) and self.__is_mail_valid(email_part) and self.__is_domain_valid(domain_part):
            return True
        return False







mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
