import string


def alphabet_position(text):
    alphabet = string.ascii_lowercase
    return " ".join([str(alphabet.find(c) + 1) for c in text.lower() if c in alphabet])
