import re


def is_name_valid(name):
    if re.match(r'[a-z]{5,}$', name):
        return True
    else:
        return False


def is_username_valid(username):
    if re.match(r'[0-9]{2}[@|&][A-Z]{4}$', username):
        return True
    else:
        return False


print(is_name_valid('febria'))
print(is_username_valid('29@PASS'))
print(is_username_valid('234 & Agan'))
