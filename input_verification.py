import re

def verify_password(pswd_one, pswd_two):
    if pswd_one == pswd_two:
        return True
    else:
        return False


def valid_username(username):
    USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    if USER_RE.match(username):
        return True
    return False


def valid_password(password):
    PASSWORD_RE = re.compile(r"^.{3,20}$")
    if PASSWORD_RE.match(password):
        return True
    return False


def valid_email(email):
    EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
    if EMAIL_RE.match(email):
        return True
    return False