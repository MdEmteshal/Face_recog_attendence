from tkinter import*
from tkinter import ttk
import pymysql as sql

from tkinter import messagebox


root=Tk()
root.geometry("400x400")
root.configure(background="navyblue")

vr_id=StringVar()
vr_name=StringVar()

Label1=Label(root,text="Id")
Label1.grid(row=0,column=0)

er1=Entry(root,textvariable=vr_id)
er1.grid(row=0,column=1,padx=10,pady=10)

Label1=Label(root,text="name")
Label1.grid(row=1,column=0)

er1=Entry(root,textvariable=vr_name)
er1.grid(row=1,column=1,padx=10,pady=20)

def save():
                 
                   conn=sql.connect(host="localhost",user="root",passwd="mysql",database="face_recognition")
                   cur=conn.cursor()
                   try:
                       
                       
                                inf="INSERT into student2 (id,name	) values(%s,%s)"
                                data_get=(vr_id.get(),vr_name.get())
                     
                                cur.execute(inf,data_get)
                                messagebox.showinfo("message","data inserted sucessfully")
                                conn.commit()
                                
                                conn.close()
                           
                   except:
                         print("connection failed")

def updates():
            
                       
                    try:
                          
                                 
                                      conn=sql.connect(host="localhost",user="root",passwd="mysql",database="face_recognition")
                                      cur=conn.cursor()
                                      db="Update student2 Set  name=%s where id=%s"
                                      dat=(vr_name.get(),vr_id.get())
                                      cur.execute(db,dat)
                                      messagebox.showinfo("message","data updated sucessfully")
                                      conn.commit()
                    except:
                          print("error")  
                     

bt1=Button(root,text="submit",command=save)
bt1.grid(row=3,column=1,padx=10,pady=10)

bt2=Button(root,text="update",command=updates)
bt2.grid(row=3,column=2,padx=10,pady=10)



root.mainloop()


