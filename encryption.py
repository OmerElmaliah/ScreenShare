"""Encrypt and Decrypt functions stored here"""


def encrypt(data, key):
    """Takes input and encrypts it with a given key

    ARGS:
        data(string) - Data to be encrypt
        key(string) - Key used to encrypt the data
    """
    new_str = []
    for s in range(len(data)):
        new_str.append(chr(ord(data[s]) + int(key[s % 4])))

    return "".join(new_str)


def decrypt(data, key):
    """Takes input and decrypts it with a given key

        ARGS:
            data(string) - Data to be decrypt
            key(string) - Key used to decrypt the data
        """
    new_str = []
    for s in range(len(data)):
        new_str.append(chr(ord(data[s]) - int(key[s % 4])))

    return "".join(new_str)
