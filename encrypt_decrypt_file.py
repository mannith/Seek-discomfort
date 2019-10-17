# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 19:15:00 2019

@author:ganesh
"""

from cryptography.fernet import Fernet
key = Fernet.generate_key()
print ("Ram key=", key)

file = open('c:\ganesh\key.key', 'wb')
file.write(key) # The key is type bytes still
file.close()

file = open('c:\ganesh\key.key', 'rb')
key = file.read() # The key will be type bytes
print("Ram the Key inside the file=",key)
file.close()

#getting the file to be encrypted
input_file='c:\ganesh\secretfile.txt'
output_file='c:\ganesh\encryptedfile.txt'

with open(input_file, 'rb') as f:
    data = f.read()
    
    print("Secret file data =", data)

f = Fernet(key)
encrypted = f.encrypt(data)

with open(output_file, 'wb') as f:
     f.write(encrypted)

print ("Ram the file has been encrypted, please check the file encryptedfile.txt")

with open(output_file, 'rb') as f:
    data = f.read()
print("Encyrpted file contents=",data.decode())

e = Fernet(key)

decrypted_file=e.decrypt(data)
print("the decrypted file content=",decrypted_file.decode())


