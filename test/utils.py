import string
import random


def mac_generator():
    valid_chars = string.hexdigits[:-6]
    mac_address = []
    for x in range(6):
        mac_address.append(random.sample(valid_chars, 2))
    return ":".join(''.join(octet) for octet in mac_address)
