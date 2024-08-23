

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





          bt=Button(self.root,text="click",bg="yellow",width=50,command=self.face_recog)
          bt.place(x=300,y=300)











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

                #    cur.execute("select id from student where id="+str(id))
                #    i=cur.fetchone()
                #    i="+".join(i)


                   cur.execute("select name from student where id="+str(id))
                   v=cur.fetchone()
                   v="h".join(v)

                 
                  

                   
                   cur.execute("select 	department from student where id="+str(id))
                   d=cur.fetchone()
                   d="+".join(d)

                   if confidence>77:
                        # cv2.putText(img,f"id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Name:{v}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Department:{d}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        self.mark_attendence(v,d)

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