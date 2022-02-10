import string
import random
import secrets
import re


class password_generator():

    def __init__(self):
        self.length = 12
        self.block_length = 4
        self.block_separator = "-"
        self.set_lower()
        self.set_upper()
        self.set_numbers()
        self.set_symbols()
        self.exclude_chars = ""

    def reset_chars(self):
        self.set_lower()
        self.set_upper()
        self.set_numbers()
        self.set_symbols()

    def reset_symbols(self):
        self.set_symbols()

    def set_lower(self, chars=string.ascii_lowercase):
        self.lower = chars

    def set_upper(self, chars=string.ascii_uppercase):
        self.upper = chars

    def set_numbers(self, chars=string.digits):
        self.num = chars

    def set_symbols(self, symbols=string.punctuation):
        self.symbols = symbols

    def set_hardcoresymbols(self):
        self.symbols = self.get_standard_symbols() + "ÄÜÖöäüéáí±"

    def get_standard_symbols(self):
        return string.punctuation

    def set_block_separator(self, separator="-"):
        self.block_separator = separator

    def set_excludeschars(self, excludeschars):
        self.exclude_chars = excludeschars
        self.dorp_chars()

    def drop_char(self, stringlist, excludeschars):
        if len(excludeschars) > 0:
            return re.sub('[' + excludeschars + ']', '', stringlist)
        else:
            return stringlist

    def set_length(self, length = 12):
        self.length = max([length, 8])

    def set_block_length(self, length = 4):
        self.block_length = max([length, 1])

    def dorp_chars(self):
        self.lower = self.drop_char(string.ascii_lowercase, self.exclude_chars)
        self.upper = self.drop_char(string.ascii_uppercase, self.exclude_chars)
        self.num = self.drop_char(string.digits, self.exclude_chars)
        if len(self.symbols) > 0:
            self.symbols = self.drop_char(self.symbols, self.exclude_chars)

    def password_generator(self):
        """ Function that generates a password given a length
        minimum leght = 8
        """

        # this is to ensure there is at least one upper, lower, symbol and number
        uppercase_loc = 1
        symbol_loc = 2
        number_loc = 3
        lowercase_loc = 4

        password = ''  # empty string for password
        pool = self.lower + self.upper + self.symbols + self.num  # the selection of characters used

        for i in range(self.length):
            if i == uppercase_loc:  # this is to ensure there is at least one uppercase
                password += secrets.choice(self.upper)
            elif i == lowercase_loc:  # this is to ensure there is at least one uppercase
                password += secrets.choice(self.lower)
            elif i == symbol_loc:  # this is to ensure there is at least one symbol
                if len(self.symbols) > 0:
                    password += secrets.choice(self.symbols)
                else:
                    password += secrets.choice(pool)
            elif i == number_loc:  # this is to ensure there is at least one number
                password += secrets.choice(self.num)
            else:  # adds a random character from pool
                password += secrets.choice(pool)
        password = list(password)
        random.shuffle(password)
        return ''.join(password)  # returns the string

    def blocked_password_generator(self):
        lower_vovels = "eaiou"

        def get(corpus):
            return secrets.choice(corpus)

        def block():
            if len(self.symbols) > 0:
                return get(self.upper) + get(lower_vovels) + get(self.lower) + get(self.num) + get(self.symbols)
            else:
                return get(self.upper) + get(lower_vovels) + get(self.lower) + get(self.num)

        def join_password():
            return self.block_separator.join([block() for i in range(self.block_length)])

        return join_password()

if __name__ == '__main__':
    pw = password_generator()
    print("_________________")
    print("password_generator")
    print("_________________")
    pw.reset_chars()
    pw.set_symbols("!-_.,")
    pw.set_excludeschars("I1lO0")
    pw.set_length(20)
    for i in range(10):
        print(pw.password_generator())

    print("_________________")
    pw.reset_chars()
    pw.set_symbols("")
    pw.set_excludeschars("I1lO0")
    pw.set_length(30)
    for i in range(10):
        print(pw.password_generator())

    print("____Hardcore______")
    pw.reset_chars()
    pw.set_hardcoresymbols()
    pw.set_length(30)
    for i in range(10):
        print(pw.password_generator())

    print("_________________")
    print("blocked_password_generator")
    print("_________________")
    pw.reset_chars()
    pw.set_symbols("")
    pw.set_excludeschars("I1lO0")
    pw.set_block_length(4)
    for i in range(10):
        print(pw.blocked_password_generator())
    print("_________________")
    pw.set_block_length(20)
    pw.set_symbols("!-_,.#*")
    pw.set_block_separator("_")
    pw.set_excludeschars("I1lO0")
    for _ in range(5):
        print(pw.blocked_password_generator())
