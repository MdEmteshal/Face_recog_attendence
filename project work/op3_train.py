from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql as sql



import  cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
          self.root=root
          self.root.geometry("1530x820")
          self.root.title("face recognition attendance system")

          # bt1=Button(self.root,text="click train ",command=self.train_data)
          # bt1.place(x=200,y=400,width=200,height=200)

          # bg image


          ubg_img1=Image.open("trainBg.jpg")
          ubg_img1=ubg_img1.resize((510,200),Image.ADAPTIVE)
          self.ubg_img1=ImageTk.PhotoImage(ubg_img1)

          ubg_lb1=Label(self.root,image=self.ubg_img1)
          ubg_lb1.place(x=0,y=0,width=510,height=200)

          ubg_img2=Image.open("trainbg2.jpg")
          ubg_img2=ubg_img2.resize((510,200),Image.ADAPTIVE)
          self.ubg_img2=ImageTk.PhotoImage(ubg_img2)

          ubg_lb2=Label(self.root,image=self.ubg_img2)
          ubg_lb2.place(x=510,y=0,width=510,height=200)

          ubg_img3=Image.open("trainbg2.jpg")
          ubg_img3=ubg_img3.resize((510,200),Image.ADAPTIVE)
          self.ubg_img3=ImageTk.PhotoImage(ubg_img3)

          ubg_lb3=Label(self.root,image=self.ubg_img3)
          ubg_lb3.place(x=1020,y=0,width=510,height=200)

          # train button>>>

          text1=Button(self.root,text="train data",bg="blue",fg="red",font=("arial",25,"bold"),command=self.train_data)
          text1.place(x=0,y=200,height=100,width=1530)

          # bottom image>>>>>>

          ubg_img4=Image.open("traindhdh.jpg")
          ubg_img4=ubg_img4.resize((1530,450),Image.ADAPTIVE)
          self.ubg_img4=ImageTk.PhotoImage(ubg_img4)

          ubg_lb4=Label(self.root,image=self.ubg_img4)
          ubg_lb4.place(x=0,y=300,width=1530,height=450)
         


    def train_data(self):
         data_dir=("data")
         path=[os.path.join(data_dir,file)   for file in os.listdir(data_dir)]

         faces=[]
         ids=[]

         for image in path:
              img=Image.open(image).convert('L')
              imageNp=np.array(img,'uint8')
              id=int(os.path.split(image)[1].split('.')[1])

              faces.append(imageNp)
              ids.append(id)
              cv2.imshow("train data processing",imageNp)
              cv2.waitKey(1)==13
         ids=np.array(ids)

        #  >>>>>>>>>>>>>>>>>>Train data classifier>>>>>>>>>>
         cls=cv2.face.LBPHFaceRecognizer_create()
         cls.train(faces,ids)
         cls.write("classifier.xml")

          
         cv2.destroyAllWindows()
         messagebox.showinfo("Messeage","sucessfully train",parent=self.root)


     #    function deifination for recognition button

if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()