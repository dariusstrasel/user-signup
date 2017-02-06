import re

def verify_password(pswd_one, pswd_two):
    if pswd_one == pswd_two:
        return True
    else:
        return False


def valid_username(username):
    USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    return USER_RE.match(username)


def valid_password(password):
    PASSWORD_RE = re.compile(r"^.{3,20}$")
    return PASSWORD_RE.match(password)


def valid_email(email):
    EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
    return EMAIL_RE.match(email)


def valid_input(username, password, verify_pswd, email):
    valid_username(username)
    valid_password(password)
    verify_password(password, verify_pswd)
    valid_email(email)