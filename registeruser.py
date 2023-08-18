# Importing Libraries
from tkinter import *
from tkinter import messagebox as ms
import tkinter as tk
import sqlite3
from PIL import ImageTk, Image


# Creating register function
def Registeruser():
    
    # Creating a new window
    Reg = tk.Tk()
    Reg.title(' ثبت نام کاربر')
    Reg.geometry('1000x1000')

    # Background Colors
    Reg.configure(background='#3B2C35')

    # Locking the window size

    # Creating Frame
    frame = LabelFrame(Reg, padx=30, pady=30, bg='white')
    frame.place(relx = 0.5, rely = 0.45, anchor = CENTER)
    

    # Connecting to database with registration form
    def database(arg=None):
      
        # Getting entries
        fname=firstname_entry.get()
        goods1=goods_entry.get()
        weight=var_entry.get()
        origin=origin_entry.get()
        distination=distination_entry.get()
        hire=hire_entry.get()
        Comission1=Comission_entry.get()
        transportType=c_entry.get()
        distance=distance_entry.get()
        meli_c = meli_code_entry.get()
        try:
            meli_c = int(meli_c)
        except:
            ms.showerror('Error', 'کد ملی را صحیح وارد کنید!!!')

        noe_user = type_user_entry.get()
        if noe_user == "راننده" or noe_user == "صاحب بار":
            pass
        else:
            ms.showerror('Error', 'نوع کاربر باید راننده یا صاحب بار باشد')
        # Mobile Number converting to Integer
        mobile = mobile_entry.get()
        try:
            mobile = int(mobile)
        except:
            ms.showerror('error', 'شماره تلفن را اصلاح کنید!')

        username = username_entry.get()
        password = password_entry.get()
        #confirm = confirm_entry.get()

        # Validating Entries
        validation = []

        # Adding information to the list
        validation.append(username)
        validation.append(password)
        validation.append(fname)
        validation.append(meli_c)
        validation.append(weight)
        validation.append(origin)
        validation.append(distination)
        validation.append(distance)
        validation.append(noe_user)
        validation.append(mobile)
        validation.append(hire)
        validation.append(transportType)
        validation.append(Comission1)
        validation.append(goods1)







        # Boolean for condition
        condition = True
        
        # Looping and checking conditions

        if condition:
            
            # Checking for password match
            #if password != confirm:
             #   ms.showerror('Oops', 'Password Does Not Match!!!')
                

                # Making connection
                con = sqlite3.connect('data1.db', check_same_thread=False, isolation_level=None)
                cur = con.cursor()




                # Inserting Data into Table
                cur.execute('INSERT INTO goods_information(username ,password,firstname,meli_c,noe_user,mobile, goods ,weight ,Origin ,Destination ,hire , Commission, Typeofvehicle, distance  ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(username,password,fname,str(meli_c),noe_user,str(mobile),goods1,weight ,origin,distination,hire , Comission1,transportType,distance ,))
                con.commit()

                # Showing success message
                ms.showinfo('Successful', 'ثبت نام با موفقیت انجام شد.')

                # Closing the window
                Reg.destroy()
            
        else:
            ms.showerror('Oops', 'Please Fill All The Input Fields')
    
    
    # creating a label for username and password using Label
    fname = tk.Label(frame, text = 'نام کامل', font=('Arial',5, 'bold'), bg='white', fg='green')
    origin = tk.Label(frame, text = 'مبدا', font=('Arial',5, 'bold'), bg='white', fg='green')
    distination = tk.Label(frame, text ='مقصد', font=('Arial',8, 'bold'), bg='white', fg='green')
    distance= tk.Label(frame, text = 'مسافت', font=('Arial',8, 'bold'), bg='white', fg='green')
    goods1= tk.Label(frame, text = 'بارها', font=('Arial',8, 'bold'), bg='white', fg='green')
    weight = tk.Label(frame, text = 'وزن بارها', font=('Arial',8, 'bold'), bg='white', fg='green')
    hire= tk.Label(frame, text = 'کرایه حمل', font=('Arial',8, 'bold'), bg='white', fg='green')
    Comission1 = tk.Label(frame, text = 'حق کمیسیون', font=('Arial',8, 'bold'), bg='white', fg='green')
    transportType = tk.Label(frame, text = 'نوع وسیله نقلیه', font=('Arial',8, 'bold'), bg='white', fg='green')
    type_user = tk.Label(frame, text='نوع کاربر', font=('Arial', 8, 'bold'), bg='white', fg='green')
    meli_code = tk.Label(frame, text='کد ملی', font=('Arial', 8, 'bold'), bg='white', fg='green')
    mobile = tk.Label(frame, text = 'شماره تلفن', font=('Arial',8, 'bold'), bg='white', fg='green')
    username = tk.Label(frame, text = 'نام کاربری', font=('Arial',8, 'bold'), bg='white', fg='green')
    password = tk.Label(frame, text = 'رمز کاربری', font = ('Arial',8,'bold'), bg='white', fg='green')



    
 
   
    #confirm = tk.Label(frame, text = 'تکرار رمز کاربری', font=('Arial',12, 'bold'), bg='white', fg='green')

    # creating a entry for elements and returning values to the databse function

    firstname_entry = tk.Entry(frame ,font=('Arial',8,'normal'), bg='#FBB13C')
    firstname_entry.bind("<Return>", database)
    goods_entry = tk.Entry(frame,font=('Arial',8,'normal'), bg='#FBB13C')
    goods_entry.bind("<Return>",database)
    var_entry = tk.Entry(frame ,font=('Arial',8,'normal'), bg='#FBB13C')
    var_entry.bind("<Return>", database)
    origin_entry = tk.Entry(frame,font=('Arial',8,'normal'), bg='#FBB13C')
    origin_entry.bind("<Return>",database)
    distination_entry = tk.Entry(frame,font=('Arial',8,'normal'), bg='#FBB13C')
    distination_entry.bind("<Return>",database)
    hire_entry = tk.Entry(frame,font=('Arial',8,'normal'), bg='#FBB13C')
    hire_entry.bind("<Return>",database)
    Comission_entry = tk.Entry(frame,font=('Arial',8,'normal'), bg='#FBB13C')
    Comission_entry.bind("<Return>",database)
    c_entry = tk.Entry(frame,font=('Arial',8,'normal'), bg='#FBB13C')
    c_entry.bind("<Return>",database)
    distance_entry= tk.Entry(frame,font=('Arial',8,'normal'), bg='#FBB13C')
    distance_entry.bind("<Return>",database)
    mobile_entry = tk.Entry(frame,font=('Arial',8,'normal'), bg='#FBB13C')
    mobile_entry.bind("<Return>",database)
    username_entry = tk.Entry(frame,font=('Arial',8,'normal'), bg='#FBB13C')
    username_entry.bind("<Return>",database)
    password_entry=tk.Entry(frame, font = ('Arial',8,'normal'), show = '*', bg='#FBB13C')
    password_entry.bind("<Return>",database)
    #confirm_entry=tk.Entry(frame, font = ('Arial',12,'normal'), show = '*', bg='#FBB13C')
    #confirm_entry.bind("<Return>",database)
    type_user_entry = tk.Entry(frame, font=('Arial', 8, 'normal'), bg='#FBB13C')
    type_user_entry.bind("<Return>", database)
    meli_code_entry = tk.Entry(frame, font=('Arial', 8, 'normal'), bg='#FBB13C')
    meli_code_entry.bind("<Return>", database)

       
    # Button that will call the submit function  
    submit=tk.Button(frame,text = 'Register', command = database, width="10",bd = '3',  font = ('Times', 8, 'bold'),bg='#581845', fg='white',relief='groove', justify = 'center', pady='5'  ) 
    # Placing the label and entry
    fname.pack()
    firstname_entry.focus_set()
    firstname_entry.pack()
    goods1.pack()
    goods_entry.focus_set()
    goods_entry.pack()
    weight.pack()
    var_entry.focus_set()
    var_entry.pack()
    origin.pack()
    origin_entry.focus_set()
    origin_entry.pack()
    distination.pack()
    distination_entry.focus_set()
    distination_entry.pack()
    distance.pack()
    distance_entry.focus_set()
    distance_entry.pack()
    transportType.pack()
    c_entry.focus_set()
    c_entry.pack()
    hire.pack()
    hire_entry.focus_set()
    hire_entry.pack()
    Comission1.pack()
    Comission_entry.focus_set()
    Comission_entry.pack()
    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()

    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    mobile.pack()
    mobile_entry.pack()
    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    type_user.pack()
    type_user_entry.pack()
    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    meli_code.pack()
    meli_code_entry.pack()
    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    username.pack() 
    username_entry.pack()
    password.pack() 
    password_entry.pack()
    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    #confirm.pack()
    #confirm_entry.pack()
    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    submit.pack()
    # Quit Button
    Quit = tk.Button(Reg, text = "خروج", width="10", command = Reg.destroy, bd = '3',  font = ('Times', 12, 'bold'), bg='#133038', fg='white',relief='groove', justify = 'center', pady='5')
    Quit.place(anchor ='sw',rely=0.9,relx=0.0)
