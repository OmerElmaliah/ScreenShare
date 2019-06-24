"""Encrypt and Decrypt functions stored here"""


def encrypt(data, key):
    new_str = []
    for s in range(len(data)):
        new_str.append(chr(ord(data[s]) + int(key[s % 4])))

    return "".join(new_str)


def decrypt(data, key):
    new_str = []
    print(data)
    for s in range(len(data)):
        new_str.append(chr(ord(data[s]) - int(key[s % 4])))

    return "".join(new_str)

# check multiple times for changes in b'c/, INFO IS SENT AS BYTES
