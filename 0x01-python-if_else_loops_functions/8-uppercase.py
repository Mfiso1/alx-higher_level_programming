#!/usr/bin/python3
def uppercase(str):
    charectorz = ""
    for j in str:
        if ord('a') <= ord(j) <= ord('z'):
            charetorz += chr(ord(j) - 32)
        else:
            charectorz += j
    print("{}".format(charectorz))
