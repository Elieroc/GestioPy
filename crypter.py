#!/usr/bin/python3

# A python File crypter
# Developed by Elieroc
# Start of project : 19/10/2020
# Actual version : 1.1

import pyAesCrypt
import os

def encrypt(file, password, bufferSize=64*1024):
    pyAesCrypt.encryptFile(file, "Locked - " + file, password, bufferSize)
    # Remove original file
    os.remove(file)

def decrypt(file, password, bufferSize=64*1024):
    pyAesCrypt.decryptFile(file, "Unlocked - " + file, password, bufferSize)
