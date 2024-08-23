from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql as sql


import os
import csv
from tkinter import filedialog

mydata=[]
class attendance_pages:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x820")
        self.root.title("face recognition attendance system")

        ubg_img1=Image.open("trainBg.jpg")
        ubg_img1=ubg_img1.resize((510,100),Image.ADAPTIVE)
        self.ubg_img1=ImageTk.PhotoImage(ubg_img1)

        ubg_lb1=Label(self.root,image=self.ubg_img1)
        ubg_lb1.place(x=0,y=0,width=510,height=100)

        ubg_img2=Image.open("trainbg2.jpg")
        ubg_img2=ubg_img2.resize((510,100),Image.ADAPTIVE)
        self.ubg_img2=ImageTk.PhotoImage(ubg_img2)

        ubg_lb2=Label(self.root,image=self.ubg_img2)
        ubg_lb2.place(x=510,y=0,width=510,height=100)

        ubg_img3=Image.open("trainbg2.jpg")
        ubg_img3=ubg_img3.resize((510,100),Image.ADAPTIVE)
        self.ubg_img3=ImageTk.PhotoImage(ubg_img3)

        ubg_lb3=Label(self.root,image=self.ubg_img3)
        ubg_lb3.place(x=1020,y=0,width=510,height=100)     

        la=Label(self.root,text="Attendance Manegment system",fg="red",background="white",font=("arial",25,"bold"))
        la.place(x=0,y=100,height=100,width=1530)

        # text variable>>>>>>>>>>>>

        self.att_id=StringVar()
        self.nam=StringVar()
        self.roll=StringVar()
        self.depart=StringVar()
        self.time=StringVar()
        self.date=StringVar()
        self.status=StringVar()

        # left frame>>>>

        f1=LabelFrame(self.root,text="student details")
        f1.place(x=10,y=200,height=540,width=700)

       

        ubg_imgs=Image.open("trainbg2.jpg")
        ubg_imgs=ubg_imgs.resize((700,100),Image.ADAPTIVE)
        self.ubg_imgs=ImageTk.PhotoImage(ubg_imgs)

        ubg_lbs=Label(f1,image=self.ubg_imgs)
        ubg_lbs.place(x=0,y=0,width=700,height=100) 
# frame 2in left

        f2=LabelFrame(f1,text="student details")
        f2.place(x=10,y=100,height=420,width=670)
# attendence id
        attd_id=Label(f2,text="Attendance_id :",font=("arial",10,"bold"),fg="green")
        attd_id.grid(row=0,column=0,padx=10,pady=10)

        en_attd=ttk.Entry(f2,font=("arial",10,"bold"),foreground="blue",justify=CENTER,textvariable=self.att_id)
        en_attd.grid(row=0,column=1,padx=10,pady=10)

# name
        name=Label(f2,text="Name :",font=("arial",10,"bold"),fg="green")
        name.grid(row=0,column=2,padx=10,pady=10)

        en_name=ttk.Entry(f2,font=("arial",10,"bold"),foreground="blue",justify=CENTER,textvariable=self.nam)
        en_name.grid(row=0,column=3,padx=10,pady=10)
# roll
        roll=Label(f2,text="Roll :",font=("arial",10,"bold"),fg="green")
        roll.grid(row=1,column=0,padx=10,pady=10)

        en_roll=ttk.Entry(f2,font=("arial",10,"bold"),foreground="blue",justify=CENTER,textvariable=self.roll)
        en_roll.grid(row=1,column=1,padx=10,pady=10)
# department
        department=Label(f2,text="Department :",font=("arial",10,"bold"),fg="green")
        department.grid(row=1,column=2,padx=10,pady=10)

        en_depatment=ttk.Entry(f2,font=("arial",10,"bold"),foreground="blue",justify=CENTER,textvariable=self.depart)
        en_depatment.grid(row=1,column=3,padx=10,pady=10)
# time
        time=Label(f2,text="Time :",font=("arial",10,"bold"),fg="green")
        time.grid(row=2,column=0,padx=10,pady=10)

        en_time=ttk.Entry(f2,font=("arial",10,"bold"),foreground="blue",justify=CENTER,textvariable=self.time)
        en_time.grid(row=2,column=1,padx=10,pady=10)
# date
        date=Label(f2,text="Date :",font=("arial",10,"bold"),fg="green")
        date.grid(row=2,column=2,padx=10,pady=10)

        en_date=ttk.Entry(f2,font=("arial",10,"bold"),foreground="blue",justify=CENTER,textvariable=self.date)
        en_date.grid(row=2,column=3,padx=10,pady=10)
# attd_status
        attd_status=Label(f2,text="Attendance status :",font=("arial",10,"bold"),fg="green")
        attd_status.grid(row=3,column=0,padx=10,pady=10)

        en_status=ttk.Combobox(f2,font=("arial",10,"bold"),foreground="blue",justify=CENTER,state="readonly",textvariable=self.status)
        en_status['value']=("select status","Prsent","Absent")
        en_status.current(0)
        en_status.grid(row=3,column=1,padx=10,pady=10)


        bt1=Button(f2,text="Import CSV file",fg="red",bg="navyblue",width=20,command=self.importcsv)
        bt1.grid(row=4,column=0,pady=40,padx=5)

        bt1=Button(f2,text="Export CSV file",fg="red",bg="navyblue",width=20,command=self.exportcsv)
        bt1.grid(row=4,column=1,pady=40,padx=5)

        bt1=Button(f2,text="Update",fg="red",bg="navyblue",width=20)
        bt1.grid(row=4,column=2,pady=40,padx=5)

        bt1=Button(f2,text="Reset",fg="red",bg="navyblue",width=20,command=self.reset_data)
        bt1.grid(row=4,column=3,pady=40,padx=5)


        # right frame

        rightf=LabelFrame(self.root,text="CSV files")
        rightf.place(x=710,y=200,height=550,width=810)

        table_fam=LabelFrame(rightf,bd=2,text="student table")
        table_fam.place(x=5,y=10,height=500,width=800)

        scroll_x=ttk.Scrollbar(table_fam,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_fam,orient=VERTICAL)

        col=("Attendance_id","Name","Roll","Department","Time","Date","Attendance status")
        self.table_data=ttk.Treeview(table_fam,columns=col,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
      
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.table_data.xview)
        scroll_y.config(command=self.table_data.yview)

        self.table_data.column("Attendance_id",width=100,anchor=CENTER)
        self.table_data.column("Name",width=100,anchor=CENTER)
        self.table_data.column("Roll",width=100,anchor=CENTER)
        self.table_data.column("Department",width=100,anchor=CENTER)
        self.table_data.column("Time",width=100,anchor=CENTER)
        self.table_data.column("Date",width=100,anchor=CENTER)
        self.table_data.column("Attendance status",width=100,anchor=CENTER)
        
       


        self.table_data.heading("Attendance_id",text="Attendance_id")
        self.table_data.heading("Name",text="Name")
        self.table_data.heading("Roll",text="Roll")
        self.table_data.heading("Department",text="Department")
        self.table_data.heading("Time",text="Time")
        self.table_data.heading("Date",text="Date")
        self.table_data.heading("Attendance status",text="Attendance")

       
          
      
        self.table_data['show']='headings'                 
        self.table_data.pack(side=TOP,fill=BOTH)
        self.table_data.bind("<ButtonRelease>",self.get_cur)


        # >>>>>>>>>fetch data >>>>>>>>>>

    def fetchdata(self,rows):
            self.table_data.delete(*self.table_data.get_children())

            for i in rows:
                self.table_data.insert("",END,values=i)

                # import csv file>>>>>>>>>>>

    def importcsv(self):
            global mydata
            mydata.clear()
            fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open Csv",filetypes=(("csv file","*csv"),("ALl file",".")),parent=self.root)
            with open(fln) as myfile:
                csvread=csv.reader(myfile,delimiter=",")
                for i in csvread:
                    mydata.append(i)
                self.fetchdata(mydata)

                # export csv file >>>>>>>

    def exportcsv(self):
         try:
                if len(mydata)<1:
                     messagebox.showinfo("No Data","No data found to export file",parent=self.root)
                     return False
                fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open csv",filetypes=(("csv file","*csv"),("ALl file",".")),parent=self.root)
                with open(fln,mode="w",newline="") as myfile:
                     exp_write=csv.writer(myfile,delimiter=",")
                     for i in mydata:
                          exp_write.writerow(i)

                     messagebox.showinfo("data Export","your data exported to " +os.path.basename(fln)+ "sucessfully")

         except EXCEPTION as es:
              messagebox.showerror("error",f"Due To : {str(es)}",parent=self.root)


# get cursor function>>>>>>>>>>>>>
    def get_cur(self,event=""):
         cursor_row=self.table_data.focus()
         content=self.table_data.item(cursor_row)
         rows=content['values']
         self.att_id.set(rows[0])
         self.nam.set(rows[1])
         self.roll.set(rows[2])
         self.depart.set(rows[3])
         self.date.set(rows[4])
         self.time.set(rows[5])
         self.status.set(rows[6])

# get reset function >>>>>>>>>>>>>>>

    def reset_data(self):
         
         
         self.att_id.set("")
         self.nam.set("")
         self.roll.set("")
         self.depart.set("")
         self.date.set("")
         self.time.set("")
         self.status.set("")
          

if __name__=="__main__":
    root=Tk()
    obj=attendance_pages(root)
    root.mainloop()