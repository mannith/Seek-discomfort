# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 11:04:03 2019

@author: Ram
"""

def encrypt(text,s):
    result = ""

   # transverse the plain text
    for i in range(len(text)):
      char = text[i]
      # Encrypt uppercase characters in plain text
      
      if (char.isupper()):
         result += chr((ord(char) + s-65) % 26 + 65)
      # Encrypt lowercase characters in plain text
      else:
         result += chr((ord(char) + s - 97) % 26 + 97)
      return result
#check the above function
text = "ram and mannith"
s = 4 

print(str(("Plain Text : ") + str(text)))
print( str(("Shift pattern : ") + str(s)))
print (("Cipher: ") + encrypt(text,s))
