# Solution file
class PasswordError(Exception):
    pass

pwd = input()

if len(pwd) < 8:
    raise PasswordError("Length less than 8")

if not any(c.isupper() for c in pwd):
    raise PasswordError("No uppercase letter")

if not any(c.isdigit() for c in pwd):
    raise PasswordError("No number")

print("Valid Password")