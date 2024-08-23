from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql as sql

class table:
    def __init__(self,root):
       self.root=root
       self.root.geometry("1530x750")
       self.root.title("face recognition attendance system")

           # upper pic1
       tab_img=Image.open("table_up (1).jpg")
       tab_img=tab_img.resize((765,100))
       self.tab_img=ImageTk.PhotoImage(tab_img)

       tab_lb=Label(self.root,image=self.tab_img)
       tab_lb.place(x=0,y=0,width=765,height=100)

      
      # uper pic2
       tab2_img=Image.open("table_up (2).jpg")
       tab2_img=tab2_img.resize((765,100))
       self.tab2_img=ImageTk.PhotoImage(tab2_img)

       tab2_lb=Label(self.root,image=self.tab2_img)
       tab2_lb.place(x=765,y=0,width=765,height=100)

      # back ground pic
       back_img=Image.open("table_up (2).jpg")
       back_img=back_img.resize((1530,650))
       self.back_img=ImageTk.PhotoImage(back_img)

       back_lb=Label(self.root,image=self.back_img)
       back_lb.place(x=0,y=100,width=1530,height=650)

       tab_lable=Label(self.root,text="Student Details",font=("elephant",25,"bold"),fg="green")
       tab_lable.place(x=0,y=105,width=1530)

       table_fam=LabelFrame(self.root,bd=2)
       table_fam.place(x=5,y=150,height=400,width=1000)

       scroll_x=ttk.Scrollbar(table_fam,orient=HORIZONTAL)
       scroll_y=ttk.Scrollbar(table_fam,orient=VERTICAL)

       col=("Course","Department","Session","Semester","year","Name","Id","Class_roll","Age","Dob","Address","Gender","MObile","Email","Password","Take_photo")
       self.table_data=ttk.Treeview(table_fam,columns=col,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
      
       scroll_x.pack(side=BOTTOM,fill=X)
       scroll_y.pack(side=RIGHT,fill=Y)
       scroll_x.config(command=self.table_data.xview)
       scroll_y.config(command=self.table_data.yview)

       self.table_data.column("Course",width=100,anchor=CENTER)
       self.table_data.column("Department",width=100,anchor=CENTER)
       self.table_data.column("Semester",width=100,anchor=CENTER)
       self.table_data.column("Session",width=100,anchor=CENTER)
       self.table_data.column("year",width=100,anchor=CENTER)
       self.table_data.column("Name",width=100,anchor=CENTER)
       self.table_data.column("Id",width=100,anchor=CENTER)
       self.table_data.column("Class_roll",width=100,anchor=CENTER)
       self.table_data.column("Age",width=100,anchor=CENTER)
       self.table_data.column("Dob",width=100,anchor=CENTER)
       self.table_data.column("Address",width=100,anchor=CENTER)
       self.table_data.column("Gender",width=100,anchor=CENTER)
       self.table_data.column("MObile",width=100,anchor=CENTER)
       self.table_data.column("Email",width=100,anchor=CENTER)
       self.table_data.column("Password",width=100,anchor=CENTER)
       self.table_data.column("Take_photo",width=100,anchor=CENTER)
       


       self.table_data.heading("Course",text="Course")
       self.table_data.heading("Department",text="Department")
       self.table_data.heading("Semester",text="Semester")
       self.table_data.heading("Session",text="Session")
       self.table_data.heading("year",text="year")
       self.table_data.heading("Name",text="Name")
       self.table_data.heading("Id",text="Id")
       self.table_data.heading("Class_roll",text="Class_roll")
       self.table_data.heading("Age",text="Age")
       self.table_data.heading("Dob",text="Dob")
       self.table_data.heading("Address",text="Address")
       self.table_data.heading("Gender",text="Gender")
       self.table_data.heading("MObile",text="Mobile")
       self.table_data.heading("Email",text="Email")
       self.table_data.heading("Password",text="Password")
       self.table_data.heading("Take_photo",text="Take_photo")
       fetch_data()
      
                           
       self.table_data.pack(side=TOP,fill=BOTH)
        #  fetch  data  from table>>>>>>>>
       def fetch_data(self):
         conn=sql.connect(host="localhost",user="root",passwd="",database="face_recognition")
         cur=conn.cursor()
         cur.execute("select * from student")
         data=cur.fetchall()               
          
                 
         if len(data)!=0:
          self.table_data.delete(self.table_data.get_children())
              
          for i in data:
              self.table_data.insert("",END,values=i)
              conn.commit()
          conn.close() 
            
          














if __name__=="__main__":
    root=Tk()
    obj=table(root)
    root.mainloop()