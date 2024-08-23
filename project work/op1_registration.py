from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql as sql


import os

class registration:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x820")
        self.root.title("face recognition attendance system")

        img=Image.open("registration/bg1.jpg")
        img=img.resize((1530,820),Image.ADAPTIVE)
        self.photobg=ImageTk.PhotoImage(img)

        l2=Label(self.root,image=self.photobg)
        l2.place(x=0,y=0,width=1530,height=820)

        heading=Label(self.root,text="Registration Form",background="white",fg="green",font=("elephant",25,"bold"))
        heading.place(x=0,y=100,width=1530)

        # define varialbles>>>>>>>>>>>>>>>>>>>>

        self.u_name=StringVar()
        self.var_id=StringVar()
        self.var_class_roll=StringVar()
        self.var_dep=StringVar()
        self.var_year=StringVar()
        self.var_age=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_conf_pass=StringVar()
        self.var_phone=StringVar()

# frame label
        f1=LabelFrame(self.root,text="Requrements")
        f1.place(x=400,y=150,width=800,height=500)

        # username>>>>>>>>>

        user=Label(f1,text="User Name :",font=("elephant",15),fg="red")
        user.grid(row=0,column=0,padx=10,pady=10)

        en1=ttk.Entry(f1,font=("arial",10),foreground="blue",width=30,textvariable=self.u_name)
        en1.grid(row=0,column=1,padx=10,pady=10)

        # id>>>>>

        id=Label(f1,text="Id :",font=("elephant",15),fg="red")
        id.grid(row=0,column=2,padx=10,pady=10)

        en2=ttk.Entry(f1,font=("arial",10),foreground="blue",width=30,textvariable=self.var_id)
        en2.grid(row=0,column=3,padx=10,pady=10)

        # Class roll
        user=Label(f1,text="Class_Roll :",font=("elephant",15),fg="red")
        user.grid(row=1,column=0,padx=10,pady=10)

        en1=ttk.Entry(f1,font=("arial",10),foreground="blue",width=30,textvariable=self.var_class_roll)
        en1.grid(row=1,column=1,padx=10,pady=10)
        # Department
        id=Label(f1,text="Department :",font=("elephant",15),fg="red")
        id.grid(row=1,column=2,padx=10,pady=10)

        en2=ttk.Entry(f1,font=("arial",10),foreground="blue",width=30,textvariable=self.var_dep)
        en2.grid(row=1,column=3,padx=10,pady=10)
        # year
        user=Label(f1,text="Year :",font=("elephant",15),fg="red")
        user.grid(row=2,column=0,padx=10,pady=10)

        en1=ttk.Entry(f1,font=("arial",10),foreground="blue",width=30,textvariable=self.var_year)
        en1.grid(row=2,column=1,padx=10,pady=10)
        # age
        id=Label(f1,text="Age :",font=("elephant",15),fg="red")
        id.grid(row=2,column=2,padx=10,pady=10)

        en2=ttk.Entry(f1,font=("arial",10),foreground="blue",width=30,textvariable=self.var_age)
        en2.grid(row=2,column=3,padx=10,pady=10)
        # Email Id
        user=Label(f1,text="Email :",font=("elephant",15),fg="red")
        user.grid(row=3,column=0,padx=10,pady=10)

        en1=ttk.Entry(f1,font=("arial",10),foreground="blue",width=30,textvariable=self.var_email)
        en1.grid(row=3,column=1,padx=10,pady=10)
        # Password
        id=Label(f1,text="Password :",font=("elephant",15),fg="red")
        id.grid(row=3,column=2,padx=10,pady=10)

        en2=ttk.Entry(f1,font=("arial",10),foreground="blue",width=30,textvariable=self.var_pass)
        en2.grid(row=3,column=3,padx=10,pady=10)
        # Conform Password
        user=Label(f1,text="Confirm_pass :",font=("elephant",15),fg="red")
        user.grid(row=4,column=0,padx=10,pady=10)

        en1=ttk.Entry(f1,font=("arial",10),foreground="blue",width=30,textvariable=self.var_conf_pass)
        en1.grid(row=4,column=1,padx=10,pady=10)
        # Phone No
        id=Label(f1,text="Phone_no :",font=("elephant",15),fg="red")
        id.grid(row=4,column=2,padx=10,pady=10)

        en2=ttk.Entry(f1,font=("arial",10),foreground="blue",width=30,textvariable=self.var_phone)
        en2.grid(row=4,column=3,padx=10,pady=10)
       

        # button resitred>>>>>>


        bt1=Button(f1,text="Registerd",background="navyblue",foreground="yellow",width=20,command=self.dat)
        bt1.grid(row=5,column=1,padx=10)

        # login button>>>>>>>>>

        bt2=Button(f1,text="Login",background="orange",foreground="navyblue",width=20)
        bt2.grid(row=5,column=2,padx=10)


        # define function for database >>>>>>>>>>>>>>

    def dat(self):

        try:
           if self.u_name.get()=="" or self.var_id.get()=="" or self.var_class_roll.get()=="" or self.var_age.get()=="" or self.var_conf_pass.get()=="" or self.var_dep.get()=="" or self.var_email.get()=="" or self.var_pass.get()=="" or self.var_year.get()=="" or self.var_phone.get()=="":
               messagebox.showerror("Message","All fields are requred")


           else:
              if self.var_pass.get()!=self.var_conf_pass.get():
                messagebox.showerror("conform","invalid conform password") 
              else:
               con=sql.connect(host="localhost",user="root",passwd="mysql",database="face_recognition")
               cur=con.cursor()
               db="insert into st_registration (username , id, class_roll ,department, year, age, email, password, conf_pass,phone) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
               get_data1=(self.u_name.get(),self.var_id.get(),self.var_class_roll.get(),self.var_dep.get(),self.var_year.get(),self.var_age.get(),self.var_email.get(),self.var_pass.get(),self.var_conf_pass.get(),self.var_phone.get())
      
               cur.execute(db,get_data1)
               con.commit()
               con.close()

               messagebox.showinfo("mess","successfully registred",parent=self.root)

        except:
            messagebox.showerror("error"," connection failed")
          















if __name__=="__main__":
    root=Tk()
    obj=registration(root)
    root.mainloop()