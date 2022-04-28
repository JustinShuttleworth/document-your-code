import random
import string


def generate_password(chars, punctuation, invalid_chars=None):
    valid_chars = string.ascii_letters + string.digits

    if punctuation:
        valid_chars += string.punctuation

    for invalid_char in invalid_chars:
        valid_chars = valid_chars.replace(invalid_char, "")

    password_chars = random.choices(valid_chars, k=chars)
    return "".join(password_chars)
