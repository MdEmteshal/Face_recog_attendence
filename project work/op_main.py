from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql as sql
from hello import lal
from op2_student import student_details
from op3_train import Train
from op4_recognize import recognize
from op5_attendance import attendance_pages
import os


class attendance_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x820")
        self.root.title("face recognition attendance system")
        # f1=Frame(root)
        # f1.place(x=0,y=0,width=1530,height=750)
        # f1.configure(bg="navyblue")

      # bg  img
        img=Image.open("heading.jpg")
        img=img.resize((1530,130),Image.ADAPTIVE)
        self.photobg=ImageTk.PhotoImage(img)

        l2=Label(self.root,image=self.photobg)
        l2.place(x=0,y=0,width=1530,height=130)

    # 1st img
        img1=Image.open("logo2.png")
        img1=img1.resize((150,130),Image.ADAPTIVE)
        self.photo1=ImageTk.PhotoImage(img1)

        l1=Label(self.root,image=self.photo1)
        l1.place(x=300,y=0,width=150,height=130)

   
    # # 2rd img
        img2=Image.open("logo2.png")
        img2=img2.resize((150,130),Image.ADAPTIVE)
        self.photo2=ImageTk.PhotoImage(img2)

        l2=Label(self.root,image=self.photo2)
        l2.place(x=1120,y=0,width=150,height=130)

        l3=Label(self.root,text="FACE RECOGNITION ATENDENT SYSTEM",font=("Algerian",25),fg="yellow",background="blue")
        l3.place(x=480,y=40)

    # background img2

        imgbg2=Image.open("bg.jpg")
        imgbg2=imgbg2.resize((1530,620),Image.ADAPTIVE)
        self.photo3=ImageTk.PhotoImage(imgbg2)

        l_bg=Label(self.root,image=self.photo3)
        l_bg.place(x=0,y=130,width=1530,height=620)




    #  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<====================buttons========================>>>>>>>>>>>>>>>>>>>>>>

        bt_img1=Image.open("images\srudents.jpg")
        bt_img1=bt_img1.resize((200,200),Image.ADAPTIVE)
        self.bt_img1=ImageTk.PhotoImage(bt_img1)
 
        st_bt=Button(self.root,image=self.bt_img1,cursor="hand2",command=self.student_details )
        st_bt.place(x=250,y=150)

        st_bt1=Button(self.root,text="Student Details",cursor="hand2",background="navyblue",font=("Elephant",10),fg="yellow",command=self.student_details)
        st_bt1.place(x=250,y=350,width=204)

    # button2

        bt_img2=Image.open("traindhdh.jpg")
        bt_img2=bt_img2.resize((200,200),Image.ADAPTIVE)
        self.bt_img2=ImageTk.PhotoImage(bt_img2)

        rec_bt=Button(self.root,image=self.bt_img2,cursor="hand2",command=self.trains)
        rec_bt.place(x=550,y=150)

        rec_bt1=Button(self.root,text="Train Images",cursor="hand2",background="navyblue",font=("Elephant",10),fg="yellow",command=self.trains)
        rec_bt1.place(x=550,y=350,width=204)

    # # button3

        bt_img3=Image.open("recognition.jpg")
        bt_img3=bt_img3.resize((200,200),Image.ADAPTIVE)
        self.bt_img3=ImageTk.PhotoImage(bt_img3)

        At_bt=Button(self.root,image=self.bt_img3,cursor="hand2",command=self.face_recognition)
        At_bt.place(x=850,y=150)

        At_bt1=Button(self.root,text="Face Recognition",cursor="hand2",background="navyblue",font=("Elephant",10),fg="yellow",command=self.face_recognition)
        At_bt1.place(x=850,y=350,width=204)

    # # button4

        bt_img4=Image.open("atendences.jpg")
        bt_img4=bt_img4.resize((200,200),Image.ADAPTIVE)
        self.bt_img4=ImageTk.PhotoImage(bt_img4)

        train_bt=Button(self.root,image=self.bt_img4,cursor="hand2",command=self.attendences)
        train_bt.place(x=1150,y=150)

        train_bt1=Button(self.root,text="Attendance",cursor="hand2",background="navyblue",font=("Elephant",10),fg="yellow",command=self.attendences)
        train_bt1.place(x=1150,y=350,width=204)

    # # button5

        bt_img5=Image.open("photos.jpg")
        bt_img5=bt_img5.resize((200,200),Image.ADAPTIVE)
        self.bt_img5=ImageTk.PhotoImage(bt_img5)

        photo_bt=Button(self.root,image=self.bt_img5,cursor="hand2")
        photo_bt.place(x=300,y=410)

        photo_bt1=Button(self.root,text="Photos",cursor="hand2",background="navyblue",font=("Elephant",10),fg="yellow")
        photo_bt1.place(x=300,y=610,width=204)

    # # button 6

        bt_img6=Image.open("developer.jpg")
        bt_img6=bt_img6.resize((200,200),Image.ADAPTIVE)
        self.bt_img6=ImageTk.PhotoImage(bt_img6)

        dev_bt=Button(self.root,image=self.bt_img6,cursor="hand2")
        dev_bt.place(x=600,y=410)

        dev_bt1=Button(self.root,text="Developer",cursor="hand2",background="navyblue",font=("Elephant",10),fg="yellow")
        dev_bt1.place(x=600,y=610,width=204)

    # # button7

        bt_img7=Image.open("exit.jpg")
        bt_img7=bt_img7.resize((200,200),Image.ADAPTIVE)
        self.bt_img7=ImageTk.PhotoImage(bt_img7)

        exit_bt=Button(self.root,image=self.bt_img7,cursor="hand2")
        exit_bt.place(x=900,y=410)

        exit_bt1=Button(self.root,text="Student Details",cursor="hand2",background="navyblue",font=("Elephant",10),fg="yellow")
        exit_bt1.place(x=900,y=610,width=204)

# >>>>>>>>>>>>>>>function define  windows button
    # def open_img(self):
    #      os.startfile("data")

        #  function button other window

    def details(self):
           self.new_window=Toplevel(self.root)
           self.kuch=lal(self.new_window)

    # function for students details

    def student_details(self):
         self.new_window=Toplevel(self.root)
         self.kuch=student_details(self.new_window)

        #  function for train data

    def trains(self):
         self.new_window=Toplevel(self.root)
         self.kuch=Train(self.new_window)

    # function for face recognition 

    def face_recognition(self):
         self.new_window=Toplevel(self.root)
         self.kuch=recognize(self.new_window)

    # function for attendance details

    def attendences(self):
         self.new_window=Toplevel(self.root)
         self.kuch=attendance_pages(self.new_window)


if __name__=="__main__":
    root=Tk()
    obj=attendance_system(root)
    root.mainloop()