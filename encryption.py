"""Encrypt and Decrypt functions stored here"""
import os
import pickle


def encrypt(data, key):
    new_str = []
    for s in range(len(data)):
        new_str.append(chr(ord(data[s]) + int(key[s % 4])))

    return "".join(new_str)


def decrypt(data, key):
    new_str = []
    for s in range(len(data)):
        new_str.append(chr(ord(data[s]) - int(key[s % 4])))

    return "".join(new_str)


with open('img.png', 'rb') as screen_image:
    rewrite_data = None
    if os.path.isfile('imgfalse.png'):
        os.remove('imgfalse.png')
    imgf = open('imgfalse.png', 'wb')

    img_data = pickle.dumps(encrypt(screen_image.read(8192).decode('ISO-8859-1'), '1234'))
    img_data = decrypt(pickle.loads(img_data), '1234').encode('ISO-8859-1')
    while img_data:
        if rewrite_data is None:
            rewrite_data = img_data
        else:
            rewrite_data = rewrite_data + img_data

        img_data = screen_image.read(8192)

    imgf.write(rewrite_data)
    imgf.close()