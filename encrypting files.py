# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 17:20:55 2019

@author: Ram
"""

from cryptography.fernet import Fernet
file=open("key.key",'wb')
key=file.read()
file.close()
with open('test.txt','rb') as f:
    data=f.read
f=Fernet(key)
encrypted=f.encrypt(data)
print(encrypted)
with open('test.txt.encrypted','wb') as f:
    f.write(encrypted)
    