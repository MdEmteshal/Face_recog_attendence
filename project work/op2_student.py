from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql as sql
from op3_table import table
import  cv2

class student_details:
    def __init__(self,root):
          self.root=root
          self.root.geometry("1530x820")
          self.root.title("face recognition attendance system")
          # f2=Frame()
          # f2.place(x=0,y=0,width=1530,height=750)
       

         

        # uper background

          ubg_img=Image.open("upper.jpg")
          ubg_img=ubg_img.resize((1530,100),Image.ADAPTIVE)
          self.ubg_img=ImageTk.PhotoImage(ubg_img)

          ubg_lb=Label(self.root,image=self.ubg_img)
          ubg_lb.place(x=0,y=0,width=1530,height=100)



        #   bacground image
          bg_img=Image.open("studentbg.jpg")
          bg_img=bg_img.resize((1530,650),Image.ADAPTIVE)
          self.bg_img=ImageTk.PhotoImage(bg_img)

          bg_lb=Label(self.root,image=self.bg_img)
          bg_lb.place(x=0,y=100,width=1530,height=650)

          heading=Label(self.root,text="University polytechnic JAMIA MILLIA ISLAMIA " ,font=("elephant",25),background="white",foreground="red")
          heading.place(x=400,y=10)

          heading=Label(self.root,text="Student Manegment system " ,font=("elephant",25),background="white",foreground="Green")
          heading.place(x=0,y=100,width=1530)

      

        # student data------>>>>>



          Left_frame=LabelFrame(self.root,bd=3,text="student current details",relief=RIDGE,font=("elephant",12),fg="green")
          Left_frame.place(x=10,y=150,width=800,height=250)

        # varial declare>>>>>>>>>
          self.course=StringVar()
          self.dep=StringVar()
          self.session=StringVar()
          self.semester=StringVar()
          self.year1=StringVar()
          self.name=StringVar()
          self.id=StringVar()
          self.class_roll=StringVar()
          self.age=StringVar()
          self.dob=StringVar()
          self.address=StringVar()
          self.gender=StringVar()
          self.mob=StringVar()
          self.email=StringVar()
          self.password=StringVar()
          self.radio1=StringVar()
          
           
                 
       
                              
                         

         

        #  course

          cur_labl=Label(Left_frame,text="Course :",font=("calibri",15,"bold"))
          cur_labl.grid(row=0,column=0,padx=10,pady=10)

          cur_com=ttk.Combobox(Left_frame,font=("arial",10,"bold"),foreground="red",state="readonly",textvariable=self.course)
          cur_com['value']=("Select Course","B.tech","Diploma","BE","M.A","P.H.D")
          cur_com.current(0)
          cur_com.grid(row=0,column=1,padx=10,pady=10)
          

        #    department
          dep_labl=Label(Left_frame,text="Department :",font=("calibri",15,"bold"))
          dep_labl.grid(row=0,column=2,padx=10,pady=10)

          dep_com=ttk.Combobox(Left_frame,font=("arial",10,"bold"),foreground="red",state="readonly",textvariable=self.dep)
          dep_com['value']=("Select Department","computer science","civil engg","mechnical Engg","Electronics Engg","Electrical Engg")
          dep_com.current(0)
          dep_com.grid(row=0,column=3,padx=10,pady=10)


        # session

          ses_labl=Label(Left_frame,text="Session :",font=("calibri",15,"bold"))
          ses_labl.grid(row=1,column=0,padx=10,pady=10)

          ses_com=ttk.Combobox(Left_frame,font=("arial",10,"bold"),foreground="red",state="readonly",textvariable=self.session)
          ses_com['value']=("Select Session","2015-16","2016-17","2017-18","2018-19","2019-20")
          ses_com.current(0)
          ses_com.grid(row=1,column=1,padx=10,pady=10)


        # semester

          sem_labl=Label(Left_frame,text="Semester :",font=("calibri",15,"bold"))
          sem_labl.grid(row=1,column=2,padx=10,pady=10)

          sem_com=ttk.Combobox(Left_frame,font=("arial",10,"bold"),foreground="red",state="readonly",textvariable=self.semester)
          sem_com['value']=("Select Semester","semester-1","semester-2","semester-3","semester-4","semester-5","semester-6")
          sem_com.current(0)
          sem_com.grid(row=1,column=3,padx=10,pady=10)


        # year
          yer_labl=Label(Left_frame,text="year :",font=("calibri",15,"bold"))
          yer_labl.grid(row=3,column=0,padx=10,pady=10)

          yer_com=ttk.Combobox(Left_frame,font=("arial",10,"bold"),foreground="red",state="readonly",textvariable=self.year1)
          yer_com['value']=("Select year","2015","2016","2017","2018","2019","2020")
          yer_com.current(0)
          yer_com.grid(row=3,column=1,padx=10,pady=10)


        #   student information

          botom_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="student information",font=("elephant",15,"bold"),fg="green")
          botom_frame.place(x=10,y=405,width=800,height=340)

        # name
          lb_name=Label(botom_frame,text="Name :",font=("calibari",15,"bold"))
          lb_name.grid(row=0,column=0,padx=10,pady=10)

          er_name=ttk.Entry(botom_frame,   font=("Arial",10,"bold"),foreground="red",textvariable=self.name)
          er_name.grid(row=0,column=1,padx=10,pady=10)

        # id
          lb_id=Label(botom_frame,text="st_Id :",font=("calibari",15,"bold"))
          lb_id.grid(row=0,column=2,padx=4,pady=10)

          er_id=ttk.Entry(botom_frame,   font=("Arial",10,"bold"),foreground="red",textvariable=self.id)
          er_id.grid(row=0,column=3,padx=10,pady=10)
        # class roll
          lb_roll=Label(botom_frame,text="Class_Roll :",font=("calibari",15,"bold"))
          lb_roll.grid(row=2,column=0,padx=10,pady=10)

          er_roll=ttk.Entry(botom_frame,   font=("Arial",10,"bold"),foreground="red",textvariable=self.class_roll)
          er_roll.grid(row=2,column=1,padx=10,pady=10)
        # age
          lb_age=Label(botom_frame,text="Age :",font=("calibari",15,"bold"))
          lb_age.grid(row=2,column=2,pady=10)

          er_age=ttk.Entry(botom_frame,   font=("Arial",10,"bold"),foreground="red",textvariable=self.age)
          er_age.grid(row=2,column=3,padx=10,pady=10)
        # dob
          lb_dob=Label(botom_frame,text="DOB :",font=("calibari",15,"bold"))
          lb_dob.grid(row=3,column=0,padx=10,pady=10)

          er_dob=ttk.Entry(botom_frame,   font=("Arial",10,"bold"),foreground="red",textvariable=self.dob)
          er_dob.grid(row=3,column=1,padx=10,pady=10)
        # address
          lb_address=Label(botom_frame,text="Address :",font=("calibari",15,"bold"))
          lb_address.grid(row=3,column=2,padx=10,pady=10)

          er_address=ttk.Entry(botom_frame,   font=("Arial",10,"bold"),foreground="red",textvariable=self.address)
          er_address.grid(row=3,column=3,padx=10,pady=10)
        # gender
          lb_gender=Label(botom_frame,text="Gender :",font=("calibari",15,"bold"))
          lb_gender.grid(row=4,column=0,padx=10,pady=10)

          er_gender=ttk.Entry(botom_frame,   font=("Arial",10,"bold"),foreground="red",textvariable=self.gender)
          er_gender.grid(row=4,column=1,padx=10,pady=10)
        # mobile no
          lb_mob=Label(botom_frame,text="Mobile_no :",font=("calibari",15,"bold"))
          lb_mob.grid(row=4,column=2,padx=10,pady=10)

          er_mob=ttk.Entry(botom_frame,   font=("Arial",10,"bold"),foreground="red",textvariable=self.mob)
          er_mob.grid(row=4,column=3,padx=10,pady=10)
        # emial id
          lb_email=Label(botom_frame,text="Email_Id :",font=("calibari",15,"bold"))
          lb_email.grid(row=5,column=0,padx=10,pady=10)

          er_email=ttk.Entry(botom_frame,   font=("Arial",10,"bold"),foreground="red",textvariable=self.email)
          er_email.grid(row=5,column=1,padx=10,pady=10)
        # password
          lb_pass=Label(botom_frame,text="Password :",font=("calibari",15,"bold"))
          lb_pass.grid(row=5,column=2,padx=10,pady=10)

          er_pass=ttk.Entry(botom_frame,   font=("Arial",10,"bold"),foreground="red",textvariable=self.password)
          er_pass.grid(row=5,column=3,padx=10,pady=10)

        # radio button

          bt_radio=ttk.Radiobutton(botom_frame,text="Take Photo Sample", value="yes",variable=self.radio1)
          bt_radio.grid(row=6,column=0)

          bt2_radio=ttk.Radiobutton(botom_frame,text="No Photo sample", value="no",variable=self.radio1)
          bt2_radio.grid(row=6,column=1)

          bt_photo=Button(botom_frame,text="Take photo",font=("calibari",12,"bold"),bg="navyblue",fg="white",width=10,command=self.generate_pic)
          bt_photo.grid(row=6,column=3,padx=10)

          # save button

          bt_save=Button(botom_frame,text="Save",font=("calibari",12,"bold"),bg="navyblue",fg="white",command=self.save)
          bt_save.grid(row=6,column=4,padx=10)

          # resset
          bt_reset=Button(botom_frame,text="Reset",font=("calibari",12,"bold"),bg="navyblue",fg="white",command=self.resets)
          bt_reset.grid(row=6,column=5,padx=10)

        
                 

        # curd operation>>>>>>>>


          right_frame=LabelFrame(self.root,bd=2,text="Edit details",relief=RIDGE,font=("elephant",12),fg="navyblue")
          right_frame.place(x=820,y=150,width=700,height=595)


          # button take photo sample

          take_img=Image.open("heading.jpg")
          take_img=take_img.resize((100,100),Image.ADAPTIVE)
          self.take_img=ImageTk.PhotoImage(take_img)

          take_img=Button(right_frame,image=self.take_img,cursor="hand2")
          take_img.grid(row=0,column=0,padx=5,pady=5) 

          bt_take=Button(right_frame,text="Take photo sample",cursor="hand2",background="navyblue",font=("Elephant",10),fg="yellow")
          bt_take.grid(row=0,column=0,padx=45,pady=5) 

          # update photo sample

          upd_img=Image.open("heading.jpg")
          upd_img=upd_img.resize((100,100),Image.ADAPTIVE)
          self.upd_img=ImageTk.PhotoImage(upd_img)

          upd_img=Button(right_frame,image=self.upd_img,cursor="hand2")
          upd_img.grid(row=0,column=1) 

          bt_upd=Button(right_frame,text="Update photo sample",cursor="hand2",background="navyblue",font=("Elephant",10),fg="yellow")
          bt_upd.grid(row=0,column=1) 

    

          # update button

          bt_upd=Button(right_frame,text="Update",font=("Arial",12,"bold"),fg="white",background="navyblue",width=20,command=self.updates)
          bt_upd.grid(row=1,column=0)
          # delete
          bt_del=Button(right_frame,text="Delete",font=("Arial",12,"bold"),fg="white",background="navyblue",width=20 ,command=self.deletes)
          bt_del.grid(row=1,column=1)
          # .home button
          bt_home=Button(right_frame,text="<--- Home",font=("Arial",12,"bold"),fg="white",background="navyblue",width=20)
          bt_home.grid(row=2,column=0,pady=10)
          # save2 button
          bt_save2=Button(right_frame,text="Save2",font=("Arial",12,"bold"),fg="white",background="navyblue",width=20)
          bt_save2.grid(row=2,column=1,pady=10)
          # check button
          bt_check=Button(right_frame,text="check Details",font=("Arial",12,"bold"),fg="white",background="navyblue",width=20,command=self.tables)
          bt_check.grid(row=3,column=0,pady=10)





        # table frame>>>>>>>>>>>>>>>>>>>>>>>>


          table_fam=LabelFrame(right_frame,bd=2,text="student table")
          table_fam.place(x=5,y=250,height=300,width=600)

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

          self.table_data['show']="headings"
          
      
                           
          self.table_data.pack(side=TOP,fill=BOTH)
          self.table_data.bind("<ButtonRelease>",self.get_cursure)
          self.fetch_data()
          
         
             # database connection>>>>>>>>>>
          
    def save(self):
                 
                   conn=sql.connect(host="localhost",user="root",passwd="mysql",database="face_recognition")
                   cur=conn.cursor()
                   try:
                       if self.course.get()=="Select Course" or self.dep.get()=="Select Department" or self.session.get()=="Select Session" or self.semester.get()=="Select Semester" or self.year1.get()=="Select year" or self.id.get()=="":
                                messagebox.showerror("Message","All fields are Reqired",parent=self.root)
                       else:
                                inf="INSERT into student (course,	department,	session,	semester,	year,	name,	id,	class_roll,	age,	dob,	address,	gender,	mob,	email,	password,	take_photo	) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                data_get=(self.course.get(),self.dep.get(),self.session.get(),self.semester.get(),self.year1.get(),self.name.get(),self.id.get(),self.class_roll.get(),self.age.get(),self.dob.get(),self.address.get(),self.gender.get(),self.mob.get(),self.email.get(),self.password.get(),self.radio1.get())
                     
                                cur.execute(inf,data_get)
                                messagebox.showinfo("message","data inserted sucessfully",parent=self.root)
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                           
                   except:
                         messagebox.showerror("Message","Connection Failed",parent=self.root)


            #  fetch  data  from table>>>>>>>>
    def fetch_data(self):
                 conn=sql.connect(host="localhost",user="root",passwd="mysql",database="face_recognition")
                 cur=conn.cursor()
                 cur.execute("select * from student")
                 data=cur.fetchall()               
          
                 
                 if len(data)!=0:
                    self.table_data.delete(*self.table_data.get_children())
              
                    for i in data:
                         self.table_data.insert("",END,values=i)
                         conn.commit()
                 conn.close() 


  #  get cursure focus

    def get_cursure(self,event=""):
            cursure_focus=self.table_data.focus()
            content=self.table_data.item(cursure_focus)
            data=content["values"]

            self.course.set(data[0]),
            self.dep.set(data[1]),
            self.semester.set(data[2]),
            self.session.set(data[3]),
            self.year1.set(data[4]),
            self.name.set(data[5]),
            self.id.set(data[6]),
            self.class_roll.set(data[7]), 
            self.age.set(data[8]),
            self.dob.set(data[9]),
            self.address.set(data[10]),
            self.gender.set(data[11]), 
            self.mob.set(data[12]),
            self.email.set(data[13]),
            self.password.set(data[14]),
            self.radio1.set(data[15]) 

    # update data
    def updates(self):
            
                       if self.course.get()=="Select Course" or self.dep.get()=="Select Department" or self.session.get()=="Select Session" or self.semester.get()=="Select Semester" or self.year1.get()=="Select year" or self.id.get()=="":
                                messagebox.showerror("Message","Please select proper fields",parent=self.root)
                       else:
                          try:
                                  update=messagebox.askyesno("Message","Do you want to Update this details",parent=self.root)
                                  if update>0:
                                      conn=sql.connect(host="localhost",user="root",passwd="mysql",database="face_recognition")
                                      cur=conn.cursor()
                                      self.db="update student set course=%s,department=%s , session=%s, semester=%s,year=%s,name=%s,class_roll=%s,age=%s,dob=%s,address=%s,gender=%s,mob=%s,email=%s,password=%s,take_photo=%s where id=%s"
                                      self.dat=(self.course.get(),self.dep.get(),self.session.get(),self.semester.get(),self.year1.get(),self.name.get(),self.class_roll.get(),self.age.get(),self.dob.get(),self.address.get(),self.gender.get(),self.mob.get(),self.email.get(),self.password.get(),self.radio1.get(),self.id.get())
                                      cur.execute(self.db,self.dat)
                                      conn.commit()
                                      self.fetch_data()
                                      messagebox.showinfo("Message","Details is Updated Sucessfully",parent=self.root)

                          except:
                                  messagebox.showerror("Message","No Updates",parent=self.root)
# delete function
    def deletes(self):
                   if self.course.get()=="Select Course" or self.dep.get()=="Select Department" or self.session.get()=="Select Session" or self.semester.get()=="Select Semester" or self.year1.get()=="Select year" or self.id.get()=="":
                       messagebox.showerror("Message","Please select proper fields",parent=self.root)
                   else:
                          try:
                                  delete=messagebox.askyesno("Delete","Do you want to delete this deatails",parent=self.root)
                                  if delete>0:
                                          conn=sql.connect(host="localhost",user="root",passwd="mysql",database="face_recognition")
                                          cur=conn.cursor()
                                          self.query="delete from student where id=%s"
                                          self.value=(self.id.get())
                                          cur.execute(self.query,self.value)
                                          
                                  else:
                                          if not delete:
                                              return
                                  conn.commit()
                                  self.fetch_data()
                                  conn.close()
                                  messagebox.showinfo("Message","Deleted successfully",parent=self.root)
                          except:
                                 messagebox.showerror("Message"," NO Deleted",parent=self.root) 

    # reset function

    def resets(self):
          # mess= messagebox.askyesno("Message","Do you want to reset details",parent=self.root)
          # if  mess>0: 
            self.course.set("Select Course"),
            self.dep.set("Select Department"),
            self.semester.set("Select Session"),
            self.session.set("Select Semester"),
            self.year1.set("Select year"),
            self.name.set(""),
            self.id.set(""),
            self.class_roll.set(""), 
            self.age.set(""),
            self.dob.set(""),
            self.address.set(""),
            self.gender.set(""), 
            self.mob.set(""),
            self.email.set(""),
            self.password.set(""),
            self.radio1.set("") 

          #   messagebox.showinfo("Message","Reset sucessfully",parent=self.root)
          # else:
          #     messagebox.showinfo("Message","No Reset Data",parent=self.root)


       # take picture and update details>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def generate_pic(self):
             if self.course.get()=="Select Course" or self.dep.get()=="Select Department" or self.session.get()=="Select Session" or self.semester.get()=="Select Semester" or self.year1.get()=="Select year" or self.id.get()=="":
                        messagebox.showerror("Message","Please select proper fields",parent=self.root)
             else:
                             try:
                                conn=sql.connect(host="localhost",user="root",passwd="mysql",database="face_recognition")
                                cur=conn.cursor()
                                cur.execute("select * from student")
                                result=cur.fetchall()
                                id=0

                                                              
                                for i in result:
                                        id+=1
                                        
                                self.db="update student set course=%s,department=%s , session=%s, semester=%s,year=%s,name=%s,class_roll=%s,age=%s,dob=%s,address=%s,gender=%s,mob=%s,email=%s,password=%s,take_photo=%s where id=%s"
                                self.dat=(self.course.get(),self.dep.get(),self.session.get(),self.semester.get(),self.year1.get(),self.name.get(),self.class_roll.get(),self.age.get(),self.dob.get(),self.address.get(),self.gender.get(),self.mob.get(),self.email.get(),self.password.get(),self.radio1.get(),self.id.get())
                                cur.execute(self.db,self.dat)
                                conn.commit()
                                self.fetch_data()
                                self.resets()
                                conn.close()

                              # opencv predefine face detection object >>>>>>>>>>>>>>>>>>>

                                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                                def face_croped(img):
                                                gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                                                faces=face_classifier.detectMultiScale(gray,1.3,5)
                                                # scale factor=1.3
                                                # minimum neighbour=5

                                                for (x,y,w,h) in faces:
                                                          face_croped=img[y:y+h,x:x+w]
                                                          return face_croped
    
                                cap=cv2.VideoCapture(0)
                                img_id=0
                                while True:
                                               ret,my_frame=cap.read()
                                               if face_croped(my_frame) is not None:
                                                       img_id+=1
                                                       face=cv2.resize(face_croped(my_frame),(450,450))
                                                       face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                                                       file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                                                       cv2.imwrite(file_name_path,face)
                                                       cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                                                       cv2.imshow("croped face",face)

                                                       if cv2.waitKey(1)==13 or int(img_id)==100:
                                                              break
                                cap.release()
                                cv2.destroyAllWindows() 
                                messagebox.showinfo("Message","Completed 100 img samples ",parent=self.root)
                             except:
                                     messagebox.showerror("Message","Conection failds",parent=self.root)



    #  function for table data>>>>>>>>>>>
    def tables(self):
                self.new_window=Toplevel(self.root)
                self.new=table(self.new_window)


    



if __name__=="__main__":
    root=Tk()
    obj=student_details(root)
    root.mainloop()