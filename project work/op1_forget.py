from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql as sql
import os


class forget_pass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x820")
        self.root.title("face recognition attendance system")

        # varibles declaiers>>>>>>>>>>

        self.var_way=StringVar()
        self.var_securit=StringVar()
        self.new_pass=StringVar()



        # forget frame>>>>>>>>>>
        f1=LabelFrame(self.root,text="Get Renued",bg="black")
        f1.place(x=565,y=100,width=400,height=600)

        getway=Label(f1,text="Choose way",foreground="red",font=("arial",22),background="black")
        getway.grid(row=0,column=0,padx=10,pady=10)

        la=ttk.Combobox(f1,text="select way",state="readonly",font=("arial",12),textvariable=self.var_way)
        la['value']=("select","Birthday","Country")
        la.current(0)
        la.grid(row=1,column=0,padx=10,pady=10)

        sec=Label(f1,text="Sequrity code Enter age",foreground="red",font=("arial",22),background="black")
        sec.grid(row=2,column=0,padx=10,pady=10)

        er1=ttk.Entry(f1,font=("arial",12),foreground="black",textvariable=self.var_securit)
        er1.grid(row=3,column=0)

        news=Label(f1,text="New Password",foreground="red",font=("arial",22),background="black")
        news.grid(row=4,column=0,padx=10,pady=10)

        er2=ttk.Entry(f1,font=("arial",12),foreground="black",textvariable=self.new_pass)
        er2.grid(row=5,column=0)

        bt=Button(f1,text="Save",background="green",foreground="black",width=20,command=self.forget)
        bt.grid(row=6,column=0,padx=0,pady=10)

        data=Label(f1,text="your details",foreground="red",font=("arial",22),background="black")
        data.grid(row=7,column=0,padx=50)

        self.var_data=StringVar()

        er2=ttk.Entry(f1,font=("arial",12),foreground="black",textvariable=self.var_data)
        er2.grid(row=8,column=0,pady=10)

    def forget(self):
        if self.var_way.get()=="select" :
            messagebox.showerror("message","please select other fields")


       

        elif self.var_way.get()=="Birthday":
                         con=sql.connect(host="localhost",user="root",passwd="mysql",database="face_recognition")
                         cur=con.cursor()
                         query="select password from st_registration where  age=%s"
                         db=(self.var_securit.get())

                         cur.execute(query,db)

                         row=cur.fetchone()

                         self.var_data.set(row)
                




if __name__=="__main__":
    root=Tk()
    obj=forget_pass(root)
    root.mainloop()