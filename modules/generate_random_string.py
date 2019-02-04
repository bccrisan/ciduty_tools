import string
from random import *


def generate_string():
    characters = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(characters) for x in range(randint(8, 16)))
    return password


if __name__ == "__main__":
    generate_string()