# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 17:20:55 2019

@author: Ram
"""

from cryptography.fernet import Fernet
file=open("key.key",'wb')
key=file.read()
file.close()
message="ram"
encode=message.encode()
f=Fernet(key)
encrypted=f.encrypt(encode)
print(encrypted)
file=open('key.key','rb')
key2=file.read()
file.close()
f2=Fernet(key)
decrypted=f2.decrypt(encode)
print(decrypted)