import string
import random
import secrets
import re


class PasswordGenerator():

    def __init__(self):
        self.lower = ""
        self.upper = ""
        self.num = ""
        self.symbols = ""
        self.length = 12
        self.block_length = 4
        self.block_separator = "-"
        self._set_lower_()
        self._set_upper_()
        self._set_numbers_()
        self.set_symbols()
        self.exclude_chars = ""

    def reset_chars(self) -> None:
        self._set_lower_()
        self._set_upper_()
        self._set_numbers_()
        self.set_symbols()

    def reset_symbols(self) -> None:
        self.set_symbols()

    def _set_lower_(self, chars=string.ascii_lowercase) -> None:
        self.lower = chars

    def _set_upper_(self, chars=string.ascii_uppercase) -> None:
        self.upper = chars

    def _set_numbers_(self, chars=string.digits) -> None:
        self.num = chars

    def set_symbols(self, symbols=string.punctuation) -> None:
        self.symbols = symbols

    def set_hardcore_symbols(self) -> None:
        self.symbols = self.get_standard_symbols() + "ÄÜÖöäüéáí±"

    def get_standard_symbols(self) -> str:
        return string.punctuation

    def set_block_separator(self, separator="-") -> None:
        self.block_separator = separator

    def set_exclude_chars(self, excludeschars) -> None:
        self.exclude_chars = excludeschars
        self._drop_chars_()

    def set_length(self, length=12) -> None:
        self.length = max([length, 8])

    def set_block_length(self, length=4) -> None:
        self.block_length = max([length, 1])

    def _drop_char_(self, string_list, exclude_chars) -> str:
        if len(exclude_chars) > 0:
            return re.sub('[' + exclude_chars + ']', '', string_list)
        else:
            return string_list

    def _drop_chars_(self) -> None:
        self.lower = self._drop_char_(string.ascii_lowercase, self.exclude_chars)
        self.upper = self._drop_char_(string.ascii_uppercase, self.exclude_chars)
        self.num = self._drop_char_(string.digits, self.exclude_chars)
        if len(self.symbols) > 0:
            self.symbols = self._drop_char_(self.symbols, self.exclude_chars)

    def password_generator(self) -> str:
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

        for i in range(0, self.length):
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

    def blocked_password_generator(self) -> str:
        lower_vovels = "eaiou"

        def get(corpus):
            return secrets.choice(corpus)

        def block():
            if len(self.symbols) > 0:
                return get(self.upper) + get(lower_vovels) + get(self.lower) + get(self.num) + get(self.symbols)
            else:
                return get(self.upper) + get(lower_vovels) + get(self.lower) + get(self.num)

        def join_password():
            return self.block_separator.join([block() for _ in range(self.block_length)])

        return join_password()


if __name__ == '__main__':
    pw = PasswordGenerator()
    print("_________________")
    print("password_generator")
    print("_________________")
    pw.reset_chars()
    pw.set_symbols("!-_.,")
    pw.set_exclude_chars("I1lO0")
    pw.set_length(20)
    for i in range(10):
        print(pw.password_generator())

    print("_________________")
    pw.reset_chars()
    pw.set_symbols("")
    pw.set_exclude_chars("I1lO0")
    pw.set_length(30)
    for i in range(10):
        print(pw.password_generator())

    print("____Hardcore______")
    pw.reset_chars()
    pw.set_hardcore_symbols()
    pw.set_length(30)
    for i in range(10):
        print(pw.password_generator())

    print("_________________")
    print("blocked_password_generator")
    print("_________________")
    pw.reset_chars()
    pw.set_symbols("")
    pw.set_exclude_chars("I1lO0")
    pw.set_block_length(4)
    for i in range(10):
        print(pw.blocked_password_generator())
    print("_________________")
    pw.set_block_length(20)
    pw.set_symbols("!-_,.#*")
    pw.set_block_separator("_")
    pw.set_exclude_chars("I1lO0")
    for _ in range(5):
        print(pw.blocked_password_generator())
