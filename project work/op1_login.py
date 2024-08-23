from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql as sql

from op1_registration import registration
from op_main import attendance_system
from op1_forget import forget_pass
import os


class login:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x820")
        self.root.title("face recognition attendance system")

        img=Image.open("loginimg/bg4.jpg")
        img=img.resize((1530,820),Image.ADAPTIVE)
        self.photobg=ImageTk.PhotoImage(img)

        l2=Label(self.root,image=self.photobg)
        l2.place(x=0,y=0,width=1530,height=820)

        # text variabls define >>>>>>>>>>>>>


        self.user1=StringVar()

        self.pass2=StringVar()

        # login frame>>>>>>>>>>

        f1=LabelFrame(self.root,bg="black")
        f1.place(x=565,y=100,width=400,height=600)

        img2=Image.open("loginimg/bg2.jpg")
        img2=img2.resize((400,200),Image.ADAPTIVE)
        self.photobg2=ImageTk.PhotoImage(img2)

        l22=Label(f1,image=self.photobg2)
        l22.place(x=0,y=0,width=400,height=200)

        img1=Image.open("loginimg/user.png")
        img1=img1.resize((100,80),Image.ADAPTIVE)
        self.photobg1=ImageTk.PhotoImage(img1)

        l21=Label(f1,image=self.photobg1)
        l21.place(x=150,y=0,width=100,height=80)


        # text frame>>>>>>>>>>>>

        f2=LabelFrame(f1,bg="black")
        f2.place(x=0,y=200,width=400,height=400)
        # user name

        user=Label(f2,text="User Name",fg="white",font=("elephant",18,"bold"),bg="black")
        user.place(x=10,y=10)

        en1=ttk.Entry(f2,font=("arial",10,"bold"),textvariable=self.user1)
        en1.place(x=18,y=50,width=250)

        pass1=Label(f2,text="Password",fg="white",font=("elephant",18,"bold"),bg="black")
        pass1.place(x=10,y=80)

        en2=ttk.Entry(f2,font=("arial",10,"bold"),textvariable=self.pass2)
        en2.place(x=18,y=120,width=250)


        # button

        bt=Button(f2,text="Login",font=("arial",10,"bold"),width=20,bg="orange",command=self.loginbase)
        bt.place(x=50,y=160)

        newus=Button(f2,text="New User ?",fg="Orange",background="black",font=("arial",15),cursor="hand2",command=self.regis)
        newus.place(x=18,y=200)


        # forget password button>>>>>>>>>>

        newus=Button(f2,text="Forget password!",fg="Orange",background="black",font=("arial",15),cursor="hand2",command=self.forgetpass)
        newus.place(x=18,y=250)


    def forgetpass(self):
        if self.user1.get()=="":
            messagebox.showerror("message","Please Enter user name")
        else:
                con=sql.connect(host="localhost",user="root",passwd="mysql",database="face_recognition")
                cur=con.cursor()
                query=("select * from st_registration where    username=%s")
                db=(self.user1.get())

                cur.execute(query,db)

                row=cur.fetchone()

                

                if row==None:
                     messagebox.showerror("error","no data found")

                else:
                    messagebox.showinfo("message","your data")
                    self.forgetp()
              
                    

    
         


        # database for login page>>>>>>>>>>>>>>>>>>>..

    def loginbase(self):
        try:
            if self.user1.get()=="" or self.pass2.get()=="":
                messagebox.showerror("message","required fields")

            else:
                con=sql.connect(host="localhost",user="root",passwd="mysql",database="face_recognition")
                cur=con.cursor()
                query="select * from st_registration where password=%s and username=%s"
                db=(self.user1.get(),self.pass2.get())
                cur.execute(query,db)

                row=cur.fetchone()

                if row!=None:
                    messagebox.showerror("error","data does not match")

                else:
                    messagebox.showinfo("message","successfully login")
                    self.home()

                  



        except:       
                messagebox.showerror("message","data base failds")

        #<<<<<<<<<<<< registration class>>>>>>>>>>>>>>>>>>>>>>>





    # function define for forget password>>>>>>>>>>>>>>

    def forgetp(self):
         self.new_window=Toplevel(self.root)
         self.kuc=forget_pass(self.new_window)

    #  function define  for home page

    def home(self):
         self.new_window=Toplevel(self.root)
         self.kuc=attendance_system(self.new_window)



    # function define for register page


    def regis(self):
         self.new_window=Toplevel(self.root)
         self.kuc=registration(self.new_window)



if __name__=="__main__":
    root=Tk()
    obj=login(root)
    root.mainloop()