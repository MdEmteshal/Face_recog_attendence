from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql as sql
from time import strftime
from datetime import datetime

import  cv2
import os
import numpy as np

class recognize:
    def __init__(self,root):
          self.root=root
          self.root.geometry("1530x820")
          self.root.title("face recognition attendance system")

          # bt1=Button(self.root,text="click recognize ",command=self.face_recog)
          # bt1.place(x=200,y=400,width=200,height=200)
           
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

          la=Label(self.root,text="Face Recognition system",fg="red",background="white",font=("arial",25,"bold"))
          la.place(x=0,y=100,height=100,width=1530)

          ubg_img4=Image.open("recog1.jpg")
          ubg_img4=ubg_img4.resize((700,550),Image.ADAPTIVE)
          self.ubg_img4=ImageTk.PhotoImage(ubg_img4)

          ubg_lb4=Label(self.root,image=self.ubg_img4)
          ubg_lb4.place(x=0,y=200,width=700,height=550)

          ubg_img5=Image.open("recog2.jpg")
          ubg_img5=ubg_img5.resize((830,550),Image.ADAPTIVE)
          self.ubg_img5=ImageTk.PhotoImage(ubg_img5)

          ubg_lb5=Label(self.root,image=self.ubg_img5)
          ubg_lb5.place(x=700,y=200,width=830,height=550)

          bt=Button(self.root,text="Take Attendence",bg="green",fg="white",font=("arial",10,"bold"),command=self.face_recog)
          bt.place(x=900,y=450,width=420)






     # >>>>>>>>>>>>>attendence function >>>>>>>>>>>>>>>

    def mark_attendence(self,i,v,d):
         with open("ne.csv","r+",newline="\n") as f:
              mydatalist=f.readlines()
              name_list=[]
              for line in mydatalist:
                   entry=line.split((","))
                   name_list.append(entry[0])

              if((i not in name_list) and (i not in name_list) ):
                   now=datetime.now()
                   d1=now.strftime("%d/%m/%Y")
                   dtstring=now.strftime("%H:%M:%S")
                   f.writelines(f"\n{i},{v},{d},{d1},{dtstring},Present")
                   

    # >>>>>>>>>>>>>.recognition function>>>>>>>>>>>>

    def face_recog(self):
         def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,cls):
              gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
              features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

              coord=[]

              for (x,y,w,h) in features:
                   cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                   id,predict=cls.predict(gray_image[y:y+h,x:x+w])
                   confidence=int((100*(1-predict/300)))

                   conn=sql.connect(host="localhost",user="root",passwd="mysql",database="face_recognition")
                   cur=conn.cursor()

                   cur.execute("select id from student where id="+str(id))
                   i=cur.fetchone()
                   i="+".join(i)


                   cur.execute("select name from student where id="+str(id))
                   v=cur.fetchone()
                   v="+".join(v)

                 
                  

                   
                   cur.execute("select 	department from student where id="+str(id))
                   d=cur.fetchone()
                   d="+".join(d)

                   if confidence>77:
                        cv2.putText(img,f"id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Name:{v}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Department:{d}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        self.mark_attendence(i,v,d)

                   else:
                       cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3) 
                       cv2.putText(img,"unknow face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                   coord=[x,y,w,h]

              return coord
         
         def reognize(img,cls,faceCascade):
                 coord=draw_boundary(img,faceCascade,1.1,10,(255,55,255),"Face",cls)
                 return img
         faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
         cls=cv2.face.LBPHFaceRecognizer_create()
         cls.read("classifier.xml")
         

         video_cap=cv2.VideoCapture(0)

         while True:
              ret,img=video_cap.read()
              img=reognize(img,cls,faceCascade)
              cv2.imshow("welcome to face Recognition",img)

              if cv2.waitKey(1)==13:
                   break
              
         video_cap.release()
         cv2.destroyAllWindows()


if __name__=="__main__":
    root=Tk()
    obj=recognize(root)
    root.mainloop()