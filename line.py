import tkinter as tk
from tkinter import *
import sqlite3
from sqlite3 import Error
from tkinter import messagebox as ms
from adminsentry import ADMIN
from registerDriver import  Registerdriver
from registeruser import Registeruser
from driverEnter import DRIVER
from userentry import user
system = tk.Tk()

system.geometry('500x500')
system.configure(background='#225360')
system.title('سامانه حمل و نقل زمینی کالای آنلاین')


try:
    con = sqlite3.connect('data1.db', check_same_thread=False, isolation_level=None)
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS admins(username TEXT PRIMARY KEY,password TEXT)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS Driver_information (username TEXT ,password TEXT,firstname TEXT ,meli_c TEXT,noe_user TEXT,email TEXT,mobile TEXT,gender TEXT,age TEXT ,transportNumber TEXT,AccountCredict TEXT,c,Commission TEXT,goods TEXT)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS goods_information(username TEXT,password TEXT,firstname TEXT,meli_c TEXT,noe_user TEXT ,mobile TEXT, goods TEXT,weight TEXT,Origin TEXT,Destination TEXT,hire TEXT, Commission TEXT, Typeofvehicle TEXT, distance  TEXT)''')
    #cur.execute('''CREATE TABLE IF NOT EXISTS driver_users(username TEXT PRIMARY KEY,password TEXT)''')
    #cur.execute('''CREATE TABLE IF NOT EXISTS product_users(username TEXT PRIMARY KEY,password TEXT)''')
except Error:
    print(Error)

cur.execute("INSERT OR IGNORE INTO admins(username,password) VALUES('owner','1234a')")
con.commit()


# Top Frame
top_frame = Label(system, text='به سامانه حمل و نقل آنلاین خوش امدید',font = ('Cosmic', 13, 'bold'),bd='5', bg='#3d90a0',relief='groove',padx=500, pady=10)
top_frame.pack(side='top')




# Creating Frame
frame = LabelFrame(system,text='ورود و ثبت نام', padx=30, pady=40, bg='white', bd='5', relief='groove')
frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)


# Creating login button and positioning it
login1 = tk.Button(frame, text = "ورود ادمین", width="12", bd = '2',command=ADMIN, font = ('Times', 12, 'bold'), bg='#7268A6',relief='groove', justify = 'center', pady='2')
login1.pack()

# Label for seperating Buttons
label = Label(frame, bg='white').pack()


login2 = tk.Button(frame, text ="ورود راننده", width="12", bd = '2',command=DRIVER, font = ('Times', 12, 'bold'), bg='#7268A6',relief='groove', justify = 'center', pady='2')
login2.pack()


login3 = tk.Button(frame, text = "ورود صاحبان بار", width="12", bd = '2',command=user,font = ('Times', 12, 'bold'), bg='#7268A6',relief='groove', justify = 'center', pady='2')
login3.pack()




# Label for seperating Buttons
label2 = Label(frame, bg='white').pack()

# Creating and Positioning Button in Main Frame
register1 = tk.Button(frame, text = " ثبت نام راننده", width="12", bd = '3',command=Registerdriver, font = ('Times', 12, 'bold'), bg='#2A1F2D',fg='white', relief='groove', justify = 'center', pady='2')
register1.pack()


register2 = tk.Button(frame, text = "ثبت نام کاربر معمولی", width="12", bd = '3',command=Registeruser, font = ('Times', 12, 'bold'), bg='#2A1F2D',fg='white', relief='groove', justify = 'center', pady='2')
register2.pack()



# Quit Button of main frame

def Quit():
    response = ms.askokcancel('Exit!', 'Do you really want to exit ?')
    if response == 1:
        system.destroy()
    else:
        pass


Quit = tk.Button(system, text="خروج", width="10", command=Quit, bd='3', font=('Times', 12, 'bold'), bg='#133038',
                 fg='white', relief='groove', pady='5')
Quit.place(anchor='sw', rely=1.0, relx=0.0)








# Displyaing Widget to Screen
system.mainloop()