import string
import random
import secrets
import re


def drop_exclude_chars_from_string(string_list, exclude_chars) -> str:
    if len(exclude_chars) > 0:
        return re.sub('[' + exclude_chars + ']', '', string_list)
    else:
        return string_list


class PasswordGenerator:

    def __init__(self):
        self.lower = ""
        self.upper = ""
        self.num = ""
        self.symbols = ""
        self.length = 12
        self.block_counts = 4
        self.block_character_order = "Uvlns"
        self.block_separator = "-"
        self._set_lower_()
        self._set_upper_()
        self._set_numbers_()
        self.set_symbols()
        self.standard_symbols = string.punctuation
        self.exclude_chars = ""
        self._hardcore_symbols_preset_ = "ÄÜÖöäüéáí±"

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
        self.symbols = self.get_standard_symbols() + self._hardcore_symbols_preset_

    def set_block_character_order(self, order = "Uvlns") -> None:
        '''
            U or u: upper character
            V or v: lower vovel
            L or l: lower character
            N or n: number
            S or s: symbol
        :param order: str
        :return:
        '''
        available = "uvlns"
        allowed = "U or u: upper character\n" + \
                  "V or v: lower vovel\n" + \
                  "L or l: lower character\n" + \
                  "N or n: number\n" + \
                  "S or s: symbol"
        if order == "":
            order = "Uvlns"
        for each in order:
            if not each.lower() in available:
                print("Wrong character set. '{}' is not allowed. use:\n{}\n{} will be skipped".format(each, allowed,
                                                                                                       each))
        self.block_character_order = order

    def get_standard_symbols(self) -> str:
        return self.standard_symbols

    def set_block_separator(self, separator="-") -> None:
        self.block_separator = separator

    def set_exclude_chars(self, exclude_chars) -> None:
        self.exclude_chars = exclude_chars
        self._drop_chars_()

    def set_length(self, length=12) -> None:
        self.length = max([length, 8])

    def set_block_counts(self, counts=4) -> None:
        self.block_counts = max([counts, 2])

    def _drop_chars_(self) -> None:
        self.lower = drop_exclude_chars_from_string(string.ascii_lowercase, self.exclude_chars)
        self.upper = drop_exclude_chars_from_string(string.ascii_uppercase, self.exclude_chars)
        self.num = drop_exclude_chars_from_string(string.digits, self.exclude_chars)
        if len(self.symbols) > 0:
            self.symbols = drop_exclude_chars_from_string(self.symbols, self.exclude_chars)

    def password_generator(self) -> str:
        """ Function that generates a password given a length
        minimum length = 8
        """

        # this is to ensure there is at least one upper, lower, symbol and number
        uppercase_loc = 1
        symbol_loc = 2
        number_loc = 3
        lowercase_loc = 4

        password = ''  # empty string for password
        pool = self.lower + self.upper + self.symbols + self.num  # the selection of characters used

        for element in range(0, self.length):
            if uppercase_loc == element:  # this is to ensure there is at least one uppercase
                password += secrets.choice(self.upper)
            elif lowercase_loc == element:  # this is to ensure there is at least one uppercase
                password += secrets.choice(self.lower)
            elif symbol_loc == element:  # this is to ensure there is at least one symbol
                if len(self.symbols) > 0:
                    password += secrets.choice(self.symbols)
                else:
                    password += secrets.choice(pool)
            elif number_loc == element:  # this is to ensure there is at least one number
                password += secrets.choice(self.num)
            else:  # adds a random character from pool
                password += secrets.choice(pool)
        password = list(password)
        random.shuffle(password)
        return ''.join(password)  # returns the string

    def blocked_password_generator(self) -> str:
        lower_vovels = "eaiou"

        def get(corpus):
            if len(corpus) > 0:
                return secrets.choice(corpus)
            else:
                return ""

        def block():
            '''
            U or u: upper character
            V or v: lower vovel
            L or l: lower character
            N or n: number
            S or s: symbol

            :return: random character symbol block as str
            '''
            pw_block = ""

            for each in self.block_character_order:
                if each.lower() == "u":
                    pw_block += get(self.upper)
                if each.lower() == "v":
                    pw_block += get(lower_vovels)
                if each.lower() == "l":
                    pw_block += get(self.lower)
                if each.lower() == "n":
                    pw_block += get(self.num)
                if each.lower() == "s":
                    pw_block += get(self.symbols)

            return pw_block

        def join_password():
            return self.block_separator.join([block() for _ in range(self.block_counts)])

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
    pw.set_block_counts(4)
    for i in range(10):
        print(pw.blocked_password_generator())
    print("_________________")
    pw.set_block_counts(20)
    pw.set_symbols("!-_,.#*")
    pw.set_block_separator("_")
    pw.set_exclude_chars("I1lO0")
    for _ in range(5):
        print(pw.blocked_password_generator())
    print("_________________")
    print("change block order")
    pw.set_block_character_order("luuvvnn")
    print(pw.blocked_password_generator())
