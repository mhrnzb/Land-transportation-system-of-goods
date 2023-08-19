from tkinter import *
import sqlite3
from tkinter import ttk
#making a window instance

conn = sqlite3.connect('data1.db')




# def delete_goods():
    
    
#     # name_entry = Entry(window ,font=('Arial',12,'normal'), bg='#FBB13C')
#     # name = name_entry.get()
#     # name_entry.bind("<Return>",  delete_goods)
#     # name_entry.focus_set()
#     # name_entry.pack()
#     # name_entry.place(x=100 , y=9)
#     a=int(input("ldkfodk: "))
#     with conn:
#         cursorObj = conn.cursor()
#     cursorObj.execute(f'UPDATE  Driver_information SET goods=" " where username = {a}')
#     conn.commit()



def all():
    window = Tk()
    #creating a title for window
    window.title("icc-aria gui app")
    #making a button inside the window 
    window.geometry('700x700')
    window.configure(background='#225360')
    window.title('your profile!')
    window.resizable(width=False, height=False)
    Label(window,text="________به پروفایل کاربری خود خوش آمدید________" , font=(" Caslon",32 ) , foreground="white" , background="#225360").pack()
    a=Label(window,text="_._._._._._._._._._._._._You entered as a driver_._._._._._._._._._._._._" , font=(" Caslon",25 ) , foreground="white" , background="#225360").pack()
    b=Label(window,text="شما به بخش های زیر دسترسی دارید" , font=(" Caslon",25 ) , foreground="white" , background="#225360").pack()
    showallgoods= Button(window)
    def show_goods():

        jobOppotunities=Label(window)
        jobOppotunities.pack()
        jobOppotunities.place (x=240, y=150)
    
        with conn:
                cursorObj = conn.cursor() 
        all_goods=cursorObj.execute('SELECT mobile, goods ,weight ,Origin ,Destination ,hire , Commission , Typeofvehicle , distance   FROM  goods_information')
        rows = cursorObj.fetchall()
        
        jobOppotunities.configure(text=" {}".format(rows) , bg='white')


    showallgoods.configure(text="مشاهده ی کالاهای ثبت شده",font=("Brandon Grotesque",15 ),bg="orange2",fg="black" , command=show_goods)
    showallgoods.pack()
    showallgoods.place (x=3, y=170)

    goodsblank=Label(window,text="    "*30, font=("Brandon Grotesque",70 ) , foreground="white" , background="white")
    goodsblank.pack()
    goodsblank.place(x=240, y=145)
    window.mainloop()
