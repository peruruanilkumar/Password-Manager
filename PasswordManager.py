
class BasePasswordManager(object):
    old_passwords = ["Simplilearn"]                              # a list that holds all of the user's past passwords
                                                           # returns the current password as a string
    def get_password(self):
        return self.old_passwords[-1]

    def is_correct(self, password):                            # receives a string and returns a boolean True or False
        return self.get_password() == password                 # depending on whether the string is equal to the current password or not.

class PasswordManager(BasePasswordManager):                # sets the user's password only if Security level of the new password is greater
                                                           # and length of new password is minimum                                                        

    def set_password(self, new_password):
        if self.get_level() < self.get_level(new_password) and len(new_password) >= 6:
            self.old_passwords.append(new_password)
            print("Password changed Successfully.")
        else:
            print("Password can't be changed.")

    def get_level(self, password = None):     # returns the security level of the current password.
        if password == None:
            password = self.get_password()

        if password.isalpha() or password.isnumeric():
            level = 0
        elif password.isalnum():
            level = 1
        else:
            level = 2
        return level


Pass= BasePasswordManager()
new_pass = input("Enter new Password: ")
print(f"Is current password same as a new password: {Pass.is_correct(new_pass)}")

mange= PasswordManager()
mange.set_password(new_pass)
print(f"Security Level of Password: {mange.get_level()}")