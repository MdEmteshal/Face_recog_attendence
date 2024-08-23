from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql as sql



class lal:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x750")
        self.root.title("face recognition attendance system")

        l=Label(self.root,text="hello")
        l.pack()
















if __name__=="__main__":
    root=Tk()
    obj=lal(root)
    root.mainloop()