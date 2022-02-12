# Password Generator

## Import Lib


```python
from PasswordGenerator import PasswordGenerator as pwg
```

## Use Password Generator


```python
pw = pwg()
```

### Reset to default if needed


```python
pw.reset_chars()
```

### optional: change / customize symbols


```python
pw.set_symbols("!-_.,")
```

### Exclude characters from using

- lower "L" looks like capital "i": lI
- Zero sometimes look like capital "o": O0
- this is optional, too 


```python
pw.set_exclude_chars("I1lO0")
```

### change password length


```python
pw.set_length(20)
```

### create new Password


```python
print(pw.password_generator())
```

    i3hBB3l4bcN69cKvCInH
    

### if you want to create PW without symbols


```python
pw.reset_chars()
pw.set_symbols("")
pw.set_length(20)
print(pw.password_generator())
```

    YGJDBiLGntFRLBKpg1Fy
    

### add german / non german characters

- use symbols to add these chars
- e.g.   pw.set_symbols(pw.get_standard_symbols() + "ÄÜÖöäüéáí±")
- or use pw.set_hardcore_symbols()


```python
pw.reset_chars()
pw.set_hardcore_symbols()
pw.set_length(20)
print(pw.password_generator())
```

    zW#"[hJÜp[0vy\{`v"]!
    

# Blocked Passwords

### Blocked PW

Used for better typing and good entropy

- 1 Upper Char
- 1 lower vowel
- 1 lower char
- 1 Number
- optional 1 spezial symbol like '!?,.-#*'
- 1 separator e.g. "-"


```python
pw.reset_chars()
pw.set_symbols("")
pw.set_block_counts(4)
print(pw.blocked_password_generator())
```

    Muo0-Wuo4-Zoa0-Los8
    


```python
pw.set_block_counts(4)
pw.set_symbols("!-_,.#*")
pw.set_block_separator("-")
pw.set_exclude_chars("I1lO0")

print(pw.blocked_password_generator())
```

    Xge78N-Pni42U-Rti94F-Cqa98Q
    


```python
pw.reset_chars()
pw.set_block_counts(4)
pw.set_symbols("")
pw.set_block_separator("_")
pw.set_exclude_chars("I1lO0")
print(pw.blocked_password_generator())
```

    Ezo78C_Fce99N_Bjo39R_Zhe53D
    


```python
pw.reset_chars()
pw.set_block_counts(6)
pw.set_block_separator("-")
print(pw.blocked_password_generator())
```

    Zeo78Y-Eaa42A-Zlu28H-Kni41B-Ryu69A-Saa35I
    

## Customize blocked password ordering


```python
pw.reset_chars()
```

use _pw.set_block_character_order(str)_ to change the symbol / charactertype ordering

- U or u: upper character
- V or v: lower vovel
- L or l: lower character
- N or n: number
- S or s: symbol

e.g. "UlvnnU": upper, Lower, lower vovel, number, numer, upper



```python
pw.set_block_character_order("UlvnnU")
```


```python
print(pw.blocked_password_generator())
```

    Cvi40I-Vmo06J-Jwo12P-Yqi82R-Rqe80Y-Jda99F
    


```python

```

### Show available / active Symbols


```python
print("symbols: " + pw.get_standard_symbols())
pw.set_hardcore_symbols()
print("symbols: " + pw.symbols)
```

    symbols: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    symbols: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ÄÜÖöäüéáí±
    
