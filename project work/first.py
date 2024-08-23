from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql as sql


root=Tk()

root.geometry("1530x750")
root.resizable(0,0)
root.title("face recognition system")

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Table frame>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def table():
       table_frame=Frame()
       table_frame.place(x=0,y=0,width=1530,height=750)

      # upper pic1
       tab_img=Image.open("table_up (1).jpg")
       tab_img=tab_img.resize((765,100))
       table_frame.tab_img=ImageTk.PhotoImage(tab_img)

       tab_lb=Label(table_frame,image=table_frame.tab_img)
       tab_lb.place(x=0,y=0,width=765,height=100)

      
      # uper pic2
       tab2_img=Image.open("table_up (2).jpg")
       tab2_img=tab2_img.resize((765,100))
       table_frame.tab2_img=ImageTk.PhotoImage(tab2_img)

       tab2_lb=Label(table_frame,image=table_frame.tab2_img)
       tab2_lb.place(x=765,y=0,width=765,height=100)

      # back ground pic
       back_img=Image.open("table_up (2).jpg")
       back_img=back_img.resize((1530,650))
       table_frame.back_img=ImageTk.PhotoImage(back_img)

       back_lb=Label(table_frame,image=table_frame.back_img)
       back_lb.place(x=0,y=100,width=1530,height=650)

       tab_lable=Label(table_frame,text="Student Details",font=("elephant",25,"bold"),fg="green")
       tab_lable.place(x=0,y=105,width=1530)

       table_fam=LabelFrame(table_frame,bd=2)
       table_fam.place(x=5,y=150,height=400,width=1000)

       scroll_x=ttk.Scrollbar(table_fam,orient=HORIZONTAL)
       scroll_y=ttk.Scrollbar(table_fam,orient=VERTICAL)

       col=("Course","Department","Session","Semester","year","Name","Id","Class_roll","Age","Dob","Address","Gender","MObile","Email","Password","Take_photo")
       table_data=ttk.Treeview(table_fam,columns=col,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
      
       scroll_x.pack(side=BOTTOM,fill=X)
       scroll_y.pack(side=RIGHT,fill=Y)
       scroll_x.config(command=table_data.xview)
       scroll_y.config(command=table_data.yview)

       table_data.column("Course",width=100,anchor=CENTER)
       table_data.column("Department",width=100,anchor=CENTER)
       table_data.column("Semester",width=100,anchor=CENTER)
       table_data.column("Session",width=100,anchor=CENTER)
       table_data.column("year",width=100,anchor=CENTER)
       table_data.column("Name",width=100,anchor=CENTER)
       table_data.column("Id",width=100,anchor=CENTER)
       table_data.column("Class_roll",width=100,anchor=CENTER)
       table_data.column("Age",width=100,anchor=CENTER)
       table_data.column("Dob",width=100,anchor=CENTER)
       table_data.column("Address",width=100,anchor=CENTER)
       table_data.column("Gender",width=100,anchor=CENTER)
       table_data.column("MObile",width=100,anchor=CENTER)
       table_data.column("Email",width=100,anchor=CENTER)
       table_data.column("Password",width=100,anchor=CENTER)
       table_data.column("Take_photo",width=100,anchor=CENTER)
       


       table_data.heading("Course",text="Course")
       table_data.heading("Department",text="Department")
       table_data.heading("Semester",text="Semester")
       table_data.heading("Session",text="Session")
       table_data.heading("year",text="year")
       table_data.heading("Name",text="Name")
       table_data.heading("Id",text="Id")
       table_data.heading("Class_roll",text="Class_roll")
       table_data.heading("Age",text="Age")
       table_data.heading("Dob",text="Dob")
       table_data.heading("Address",text="Address")
       table_data.heading("Gender",text="Gender")
       table_data.heading("MObile",text="Mobile")
       table_data.heading("Email",text="Email")
       table_data.heading("Password",text="Password")
       table_data.heading("Take_photo",text="Take_photo")

      
                           
       table_data.pack(side=TOP,fill=BOTH)
        #  fetch  data  from table>>>>>>>>
       def fetch_data():
         conn=sql.connect(host="localhost",user="root",passwd="",database="face_recognition")
         cur=conn.cursor()
         cur.execute("select * from student")
         data=cur.fetchall()               
          
                 
         if len(data)!=0:
          table_data.delete(table_data.get_children())
              
          for i in data:
              table_data.insert("",END,values=i)
              conn.commit()
          conn.close() 
            
    

       




    #  <<<<<<<<<<<<<<<<<<<<<<<<++++++++function def for students details===============================>>>>>>>>>>>>>>>>>>>>

def show():
          f2=Frame()
          f2.place(x=0,y=0,width=1530,height=750)
         


        # uper background

          ubg_img=Image.open("upper.jpg")
          ubg_img=ubg_img.resize((1530,100))
          f2.ubg_img=ImageTk.PhotoImage(ubg_img)

          ubg_lb=Label(f2,image=f2.ubg_img)
          ubg_lb.place(x=0,y=0,width=1530,height=100)



        #   bacground image
          bg_img=Image.open("studentbg.jpg")
          bg_img=bg_img.resize((1530,650))
          f2.bg_img=ImageTk.PhotoImage(bg_img)

          bg_lb=Label(f2,image=f2.bg_img)
          bg_lb.place(x=0,y=100,width=1530,height=650)

          heading=Label(f2,text="University polytechnic JAMIA MILLIA ISLAMIA " ,font=("elephant",25),background="white",foreground="red")
          heading.place(x=400,y=10)

          heading=Label(f2,text="Student Manegment system " ,font=("elephant",25),background="white",foreground="Green")
          heading.place(x=0,y=100,width=1530)

      

        # student data------>>>>>



          Left_frame=LabelFrame(f2,bd=3,text="student current details",relief=RIDGE,font=("elephant",12),fg="green")
          Left_frame.place(x=10,y=150,width=800,height=250)

        # varial declare>>>>>>>>>
          course=StringVar()
          dep=StringVar()
          session=StringVar()
          semester=StringVar()
          year1=StringVar()
          name=StringVar()
          id=StringVar()
          class_roll=StringVar()
          age=StringVar()
          dob=StringVar()
          address=StringVar()
          gender=StringVar()
          mob=StringVar()
          email=StringVar()
          password=StringVar()
          radio1=StringVar()
          
          # database connection>>>>>>>>>>
          
          def save():
                 
                   conn=sql.connect(host="localhost",user="root",passwd="",database="face_recognition")
                   cur=conn.cursor()
                   try:
                       if course.get()=="Select Course" or dep.get()=="Select Department" or session.get()=="Select Session" or semester.get()=="Select Semester" or year1.get()=="Select year" or id.get()=="":
                                messagebox.showerror("Error message","all fields are reqired")
                       else:
                                inf="INSERT into student (course,	department,	session,	semester,	year,	name,	id,	class_roll,	age,	dob,	address,	gender,	mob,	email,	password,	take_photo	) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                data_get=(course.get(),dep.get(),session.get(),semester.get(),year1.get(),name.get(),id.get(),class_roll.get(),age.get(),dob.get(),address.get(),gender.get(),mob.get(),email.get(),password.get(),radio1.get())
                     
                                cur.execute(inf,data_get)
                                messagebox.showinfo("message","data inserted sucessfully")
                                conn.commit()
                                
                                conn.close()
                           
                   except:
                         print("connection failed")
                
      
                              
                         

         

        #  course

          cur_labl=Label(Left_frame,text="Course :",font=("calibri",15,"bold"))
          cur_labl.grid(row=0,column=0,padx=10,pady=10)

          cur_com=ttk.Combobox(Left_frame,font=("arial",10,"bold"),foreground="red",state="readonly",textvariable=course)
          cur_com['value']=("Select Course","B.tech","Diploma","BE","M.A","P.H.D")
          cur_com.current(0)
          cur_com.grid(row=0,column=1,padx=10,pady=10)
          

        #    department
          dep_labl=Label(Left_frame,text="Department :",font=("calibri",15,"bold"))
          dep_labl.grid(row=0,column=2,padx=10,pady=10)

          dep_com=ttk.Combobox(Left_frame,font=("arial",10,"bold"),foreground="red",state="readonly",textvariable=dep)
          dep_com['value']=("Select Department","computer science","civil engg","mechnical Engg","Electronics Engg","Electrical Engg")
          dep_com.current(0)
          dep_com.grid(row=0,column=3,padx=10,pady=10)


        # session

          ses_labl=Label(Left_frame,text="Session :",font=("calibri",15,"bold"))
          ses_labl.grid(row=1,column=0,padx=10,pady=10)

          ses_com=ttk.Combobox(Left_frame,font=("arial",10,"bold"),foreground="red",state="readonly",textvariable=session)
          ses_com['value']=("Select Session","2015-16","2016-17","2017-18","2018-19","2019-20")
          ses_com.current(0)
          ses_com.grid(row=1,column=1,padx=10,pady=10)


        # semester

          sem_labl=Label(Left_frame,text="Semester :",font=("calibri",15,"bold"))
          sem_labl.grid(row=1,column=2,padx=10,pady=10)

          sem_com=ttk.Combobox(Left_frame,font=("arial",10,"bold"),foreground="red",state="readonly",textvariable=semester)
          sem_com['value']=("Select Semester","semester-1","semester-2","semester-3","semester-4","semester-5","semester-6")
          sem_com.current(0)
          sem_com.grid(row=1,column=3,padx=10,pady=10)


        # year
          yer_labl=Label(Left_frame,text="year :",font=("calibri",15,"bold"))
          yer_labl.grid(row=3,column=0,padx=10,pady=10)

          yer_com=ttk.Combobox(Left_frame,font=("arial",10,"bold"),foreground="red",state="readonly",textvariable=year1)
          yer_com['value']=("Select year","2015","2016","2017","2018","2019","2020")
          yer_com.current(0)
          yer_com.grid(row=3,column=1,padx=10,pady=10)


        #   student information

          botom_frame=LabelFrame(f2,bd=2,relief=RIDGE,text="student information",font=("elephant",15,"bold"),fg="green")
          botom_frame.place(x=10,y=405,width=800,height=340)

        # name
          lb_name=Label(botom_frame,text="Name :",font=("calibari",15,"bold"))
          lb_name.grid(row=0,column=0,padx=10,pady=10)

          er_name=ttk.Entry(botom_frame,   font=("Arial",10,"bold"),foreground="red",textvariable=name)
          er_name.grid(row=0,column=1,padx=10,pady=10)

        # id
          lb_id=Label(botom_frame,text="st_Id :",font=("calibari",15,"bold"))
          lb_id.grid(row=0,column=2,padx=4,pady=10)

          er_id=ttk.Entry(botom_frame,   font=("Arial",10,"bold"),foreground="red",textvariable=id)
          er_id.grid(row=0,column=3,padx=10,pady=10)
        # class roll
          lb_roll=Label(botom_frame,text="Class_Roll :",font=("calibari",15,"bold"))
          lb_roll.grid(row=2,column=0,padx=10,pady=10)

          er_roll=ttk.Entry(botom_frame,   font=("Arial",10,"bold"),foreground="red",textvariable=class_roll)
          er_roll.grid(row=2,column=1,padx=10,pady=10)
        # age
          lb_age=Label(botom_frame,text="Age :",font=("calibari",15,"bold"))
          lb_age.grid(row=2,column=2,pady=10)

          er_age=ttk.Entry(botom_frame,   font=("Arial",10,"bold"),foreground="red",textvariable=age)
          er_age.grid(row=2,column=3,padx=10,pady=10)
        # dob
          lb_dob=Label(botom_frame,text="DOB :",font=("calibari",15,"bold"))
          lb_dob.grid(row=3,column=0,padx=10,pady=10)

          er_dob=ttk.Entry(botom_frame,   font=("Arial",10,"bold"),foreground="red",textvariable=dob)
          er_dob.grid(row=3,column=1,padx=10,pady=10)
        # address
          lb_address=Label(botom_frame,text="Address :",font=("calibari",15,"bold"))
          lb_address.grid(row=3,column=2,padx=10,pady=10)

          er_address=ttk.Entry(botom_frame,   font=("Arial",10,"bold"),foreground="red",textvariable=address)
          er_address.grid(row=3,column=3,padx=10,pady=10)
        # gender
          lb_gender=Label(botom_frame,text="Gender :",font=("calibari",15,"bold"))
          lb_gender.grid(row=4,column=0,padx=10,pady=10)

          er_gender=ttk.Entry(botom_frame,   font=("Arial",10,"bold"),foreground="red",textvariable=gender)
          er_gender.grid(row=4,column=1,padx=10,pady=10)
        # mobile no
          lb_mob=Label(botom_frame,text="Mobile_no :",font=("calibari",15,"bold"))
          lb_mob.grid(row=4,column=2,padx=10,pady=10)

          er_mob=ttk.Entry(botom_frame,   font=("Arial",10,"bold"),foreground="red",textvariable=mob)
          er_mob.grid(row=4,column=3,padx=10,pady=10)
        # emial id
          lb_email=Label(botom_frame,text="Email_Id :",font=("calibari",15,"bold"))
          lb_email.grid(row=5,column=0,padx=10,pady=10)

          er_email=ttk.Entry(botom_frame,   font=("Arial",10,"bold"),foreground="red",textvariable=email)
          er_email.grid(row=5,column=1,padx=10,pady=10)
        # password
          lb_pass=Label(botom_frame,text="Password :",font=("calibari",15,"bold"))
          lb_pass.grid(row=5,column=2,padx=10,pady=10)

          er_pass=ttk.Entry(botom_frame,   font=("Arial",10,"bold"),foreground="red",textvariable=password)
          er_pass.grid(row=5,column=3,padx=10,pady=10)

        # radio button

          bt_radio=ttk.Radiobutton(botom_frame,text="Take Photo Sample", value="yes",variable=radio1)
          bt_radio.grid(row=6,column=0)

          bt2_radio=ttk.Radiobutton(botom_frame,text="No Photo sample", value="no",variable=radio1)
          bt2_radio.grid(row=6,column=1)

          bt_photo=Button(botom_frame,text="Take photo",font=("calibari",12,"bold"),bg="navyblue",fg="white",width=10)
          bt_photo.grid(row=6,column=3,padx=10)

          # save button

          bt_save=Button(botom_frame,text="Save",font=("calibari",12,"bold"),bg="navyblue",fg="white",command=save)
          bt_save.grid(row=6,column=4,padx=10)

          # resset
          bt_reset=Button(botom_frame,text="Reset",font=("calibari",12,"bold"),bg="navyblue",fg="white")
          bt_reset.grid(row=6,column=5,padx=10)

        
                 

        # curd operation>>>>>>>>


          right_frame=LabelFrame(f2,bd=2,text="Edit details",relief=RIDGE,font=("elephant",12),fg="navyblue")
          right_frame.place(x=820,y=150,width=700,height=595)


          # button take photo sample

          take_img=Image.open("heading.jpg")
          take_img=take_img.resize((200,200))
          right_frame.take_img=ImageTk.PhotoImage(take_img)

          take_img=Button(right_frame,image=right_frame.take_img,cursor="hand2")
          take_img.grid(row=0,column=0,padx=40,pady=40) 

          bt_take=Button(right_frame,text="Take photo sample",cursor="hand2",background="navyblue",font=("Elephant",10),fg="yellow")
          bt_take.grid(row=0,column=0,padx=40,pady=40) 

          # update photo sample

          upd_img=Image.open("heading.jpg")
          upd_img=upd_img.resize((200,200))
          right_frame.upd_img=ImageTk.PhotoImage(upd_img)

          upd_img=Button(right_frame,image=right_frame.upd_img,cursor="hand2")
          upd_img.grid(row=0,column=1) 

          bt_upd=Button(right_frame,text="Update photo sample",cursor="hand2",background="navyblue",font=("Elephant",10),fg="yellow")
          bt_upd.grid(row=0,column=1) 

          # update button

          bt_upd=Button(right_frame,text="Update",font=("Arial",12,"bold"),fg="white",background="navyblue",width=20)
          bt_upd.grid(row=1,column=0)

          bt_del=Button(right_frame,text="Delete",font=("Arial",12,"bold"),fg="white",background="navyblue",width=20)
          bt_del.grid(row=1,column=1)

          bt_home=Button(right_frame,text="<--- Home",font=("Arial",12,"bold"),fg="white",background="navyblue",width=20,command=home)
          bt_home.grid(row=2,column=0,pady=10)

          bt_save2=Button(right_frame,text="Save2",font=("Arial",12,"bold"),fg="white",background="navyblue",width=20)
          bt_save2.grid(row=2,column=1,pady=10)

          bt_save2=Button(right_frame,text="check Details",font=("Arial",12,"bold"),fg="white",background="navyblue",width=20,command=table)
          bt_save2.grid(row=3,column=0,pady=10)

          

         





    #  <<<<<<<<<<<<<<<<<<<<<<<<++++++++function def for home page===============================>>>>>>>>>>>>>>>>>>>>


def home():
    f1=Frame(root)
    f1.place(x=0,y=0,width=1530,height=750)
    f1.configure(bg="navyblue")

      # bg  img
    img=Image.open("heading.jpg")
    img=img.resize((1530,130))
    f1.photobg=ImageTk.PhotoImage(img)

    l2=Label(f1,image=f1.photobg)
    l2.place(x=0,y=0,width=1530,height=130)

    # 1st img
    img1=Image.open("logo2.png")
    img1=img1.resize((150,130))
    f1.photo1=ImageTk.PhotoImage(img1)

    l1=Label(f1,image=f1.photo1)
    l1.place(x=300,y=0,width=150,height=130)

   
    # # 2rd img
    img2=Image.open("logo2.png")
    img2=img2.resize((150,130))
    f1.photo2=ImageTk.PhotoImage(img2)

    l2=Label(f1,image=f1.photo2)
    l2.place(x=1120,y=0,width=150,height=130)

    l3=Label(f1,text="FACE RECOGNITION ATENDENT SYSTEM",font=("Algerian",25),fg="yellow",background="blue")
    l3.place(x=480,y=40)

    # background img2

    imgbg2=Image.open("bg.jpg")
    imgbg2=imgbg2.resize((1530,620))
    f1.photo3=ImageTk.PhotoImage(imgbg2)

    l_bg=Label(f1,image=f1.photo3)
    l_bg.place(x=0,y=130,width=1530,height=620)




    #  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<====================buttons========================>>>>>>>>>>>>>>>>>>>>>>

    bt_img1=Image.open("images\srudents.jpg")
    bt_img1=bt_img1.resize((200,200))
    f1.bt_img1=ImageTk.PhotoImage(bt_img1)
 
    st_bt=Button(f1,image=f1.bt_img1,cursor="hand2", command=show)
    st_bt.place(x=150,y=150)

    st_bt1=Button(f1,text="Student Details",cursor="hand2",background="navyblue",font=("Elephant",10),fg="yellow",command=show)
    st_bt1.place(x=150,y=350,width=204)

    # button2

    bt_img2=Image.open("recognition.jpg")
    bt_img2=bt_img2.resize((200,200))
    f1.bt_img2=ImageTk.PhotoImage(bt_img2)

    rec_bt=Button(f1,image=f1.bt_img2,cursor="hand2")
    rec_bt.place(x=384,y=150)

    rec_bt1=Button(f1,text="Face Recognition",cursor="hand2",background="navyblue",font=("Elephant",10),fg="yellow")
    rec_bt1.place(x=384,y=350,width=204)

    # # button3

    bt_img3=Image.open("atendences.jpg")
    bt_img3=bt_img3.resize((200,200))
    f1.bt_img3=ImageTk.PhotoImage(bt_img3)

    At_bt=Button(f1,image=f1.bt_img3,cursor="hand2")
    At_bt.place(x=614,y=150)

    At_bt1=Button(f1,text="Attendance",cursor="hand2",background="navyblue",font=("Elephant",10),fg="yellow")
    At_bt1.place(x=614,y=350,width=204)

    # # button4

    bt_img4=Image.open("traindhdh.jpg")
    bt_img4=bt_img4.resize((200,200))
    f1.bt_img4=ImageTk.PhotoImage(bt_img4)

    train_bt=Button(f1,image=f1.bt_img4,cursor="hand2")
    train_bt.place(x=844,y=150)

    train_bt1=Button(f1,text="Train data",cursor="hand2",background="navyblue",font=("Elephant",10),fg="yellow")
    train_bt1.place(x=844,y=350,width=204)

    # # button5

    bt_img5=Image.open("photos.jpg")
    bt_img5=bt_img5.resize((200,200))
    f1.bt_img5=ImageTk.PhotoImage(bt_img5)

    photo_bt=Button(f1,image=f1.bt_img5,cursor="hand2")
    photo_bt.place(x=150,y=410)

    photo_bt1=Button(f1,text="Photos",cursor="hand2",background="navyblue",font=("Elephant",10),fg="yellow")
    photo_bt1.place(x=150,y=610,width=204)

    # # button 6

    bt_img6=Image.open("developer.jpg")
    bt_img6=bt_img6.resize((200,200))
    f1.bt_img6=ImageTk.PhotoImage(bt_img6)

    dev_bt=Button(f1,image=f1.bt_img6,cursor="hand2")
    dev_bt.place(x=384,y=410)

    dev_bt1=Button(f1,text="Developer",cursor="hand2",background="navyblue",font=("Elephant",10),fg="yellow")
    dev_bt1.place(x=384,y=610,width=204)

    # # button7

    bt_img7=Image.open("exit.jpg")
    bt_img7=bt_img7.resize((200,200))
    f1.bt_img7=ImageTk.PhotoImage(bt_img7)

    exit_bt=Button(f1,image=f1.bt_img7,cursor="hand2")
    exit_bt.place(x=614,y=410)

    exit_bt1=Button(f1,text="Student Details",cursor="hand2",background="navyblue",font=("Elephant",10),fg="yellow")
    exit_bt1.place(x=614,y=610,width=204)

                 
home()




root.mainloop()