import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import sys

import os
 
creds = 'tempfile.temp' # This just sets the variable creds to 'tempfile.temp'
 
def Signup(): # This is the signup definition, 
    global pwordE # These globals just make the variables global to the entire script, meaning any definition can use them
    global nameE
    global roots
 
    roots = Tk() # This creates the window
    roots.title('Signup') 
    intruction = Label(roots, text='Please Enter new Credentials\n') # This puts a label
    intruction.grid(row=0, column=0, sticky=E) 
 
    nameL = Label(roots, text='New Username: ') 
    pwordL = Label(roots, text='New Password: ') 
    nameL.grid(row=1, column=0, sticky=W) 
    pwordL.grid(row=2, column=0, sticky=W) 
 
    nameE = Entry(roots) 
    pwordE = Entry(roots, show='*') 
    nameE.grid(row=1, column=1) 
    pwordE.grid(row=2, column=1) 
 
    signupButton = Button(roots, text='Signup', command=FSSignup) 
    signupButton.grid(columnspan=2, sticky=W)
    roots.mainloop()
    
def browsefunc():
    filename = askopenfilename()
    pathlabel.config(text=filename)

pathlabel=Label()
pathlabel.pack()

def callback():
    messagebox.showinfo("About DocLocker","This Application helps you to encrypt each of your uploaded document with a unique password of your choice 'Created by Mannith and Ram'")
    

 
def FSSignup():
    with open(creds, 'w') as f: # Creates a document using the variable we made at the top.
        f.write(nameE.get()) # nameE is the variable we were storing the input 
        f.write('\n') # Splits the line so that username and password are in different lines
        f.write(pwordE.get()) 
        f.close() 
 
    roots.destroy() 
    Login() #this will open the login window

 
def Login():
    global nameEL
    global pwordEL 
    global rootA
 
    rootA = Tk() 
    rootA.title('Login') 
    intruction = Label(rootA, text='Please Login\n') 
    intruction.grid(sticky=E)
 
    nameL = Label(rootA, text='Username: ')
    pwordL = Label(rootA, text='Password: ') 
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=2, sticky=W)
 
    nameEL = Entry(rootA) #input the name
    pwordEL = Entry(rootA, show='*')
    nameEL.grid(row=1, column=1)
    pwordEL.grid(row=2, column=1)
 
    loginB = Button(rootA, text='Login', command=CheckLogin) # login button is created.
    loginB.grid(columnspan=2, sticky=W)
 
    rmuser = Button(rootA, text='Delete User', fg='red', command=DelUser) # delete user button is created
    rmuser.grid(columnspan=2, sticky=W)
    rootA.mainloop()
 
def CheckLogin():
    with open(creds) as f:
        data = f.readlines() #the data in the document is put in the form of variables
        uname = data[0].rstrip()
        pword = data[1].rstrip()
      
 
    if nameEL.get() == uname and pwordEL.get() == pword: 
        r = Tk() # Opens new window
        r.title('Document Locker')
        r.geometry('500x500') # Makes the window a certain size
        rlbl = Label(r, text='\nwelcome to document locker') # "logged in" label
        rlbl.pack() # Pack is like .grid(), just different
        rlbl2=Label(r,text='Everyone likes PRIVACY',font='Times 30 bold')
        rlbl2.pack()
        tabControl=ttk.Notebook(r)#created tabcontrol
        tab1=ttk.Frame(tabControl)
        tabControl.add(tab1, text='File')#creates a tab named file
        tabControl.pack()
        tab2=ttk.Frame(tabControl)
        tabControl.add(tab2, text='Profile')
        tabControl.pack(expand=1, fill='both')
        btn1t1=ttk.Button(tab1,text='Upload', command=browsefunc)
        btn1t1.pack()
        pathlabel=Label(r)
        pathlabel.pack()
        btn2t1=ttk.Button(tab1, text='Uploaded Documents')
        btn2t1.pack()
        btn3t1=ttk.Button(tab1, text='Want to know about Us?',command=callback)
        btn3t1.pack()
        btn2t2=ttk.Button(tab2, text='Signout', command=r.destroy)
        btn2t2.pack()
        
        r.mainloop()
    else:
        r = Tk()
        r.title('Document Locker')
        r.geometry('150x50')
        rlbl = Label(r, text='\n[!] Invalid Login')
        rlbl.pack()
        r.mainloop()
 
def DelUser():
    os.remove(creds) # Removes the file
    rootA.destroy() 
    Signup() 
 
if os.path.isfile(creds):
    Login()
else: # The if and else statement check if the user exists..if the user doesnot exist..the signup window is opened
    Signup()


