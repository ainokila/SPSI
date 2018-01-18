# -*- coding: utf-8 -*-
import hashlib
import sys
import random
import string
import binascii


def generate_text_random(n):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(int(n)))


def hex_to_bin_char(char):

    if char == '0':
        return "0000"
    if char == '1':
        return "0001"
    if char == '2':
        return "0010"
    if char == '3':
        return "0011"
    if char == '4':
        return "0100"
    if char == '5':
        return "0101"
    if char == '6':
        return "0110"
    if char == '7':
        return "0111"
    if char == '8':
        return "1000"
    if char == '9':
        return "1001"
    if char == 'a':
        return "1010"
    if char == 'b':
        return "1011"
    if char == 'c':
        return "1100"
    if char == 'd':
        return "1101"
    if char == 'e':
        return "1110"
    if char == 'f':
        return "1111"

def hex_to_bin(strin):
    sol = ""

    for i in range(len(strin)):
        sol = sol + hex_to_bin_char( strin[i])

    return sol

def zero_first(hash,n):

    binary_string = hex_to_bin(hash)

    for i in range(int(n)):
        if binary_string[i] != '0':
            print(binary_string+"\n")
            return False

    return True

def run(parameters):
    file = open(parameters[1],'r')
    num_bits = parameters[2]
    text = file.read()

    x = 4
    str_random = generate_text_random(x)
    identifier = text + str_random


    found = False
    tried = 0

    while not found:

        generated_hash = hashlib.sha1(identifier.encode('utf-8'))
        tried = tried + 1

        if zero_first(generated_hash.hexdigest(),num_bits):
            found = True
        else:
            x = x + 1 
            str_random = generate_text_random(x)
            identifier = text + str_random


    if found:
        print("Encontrado con " + str(num_bits) + " :")
        print("Texto: " + text)
        print("Cadena: " + str_random)
        print("Intentos: " + str(tried))


num_args = len(sys.argv)
value_args = sys.argv


if not num_args == 3:
    print("python3 hash.py <file> <n_bits>")
else:
    run(value_args)
