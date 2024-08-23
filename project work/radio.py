from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image


root=Tk()

root.geometry("1530x750")
root.resizable(0,0)

f1=Frame()
f1.place(x=60,y=60,width=600,height=600)


scroll_x=ttk.Scrollbar(f1,orient=HORIZONTAL)
scroll_y=ttk.Scrollbar(f1,orient=VERTICAL)
col=("name","class","department","dkjhfkj","dkhkjhjds","dkjfhkjhue")

treeview=ttk.Treeview(f1,columns=col,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=treeview.xview)
scroll_y.config(command=treeview.yview)
treeview.heading("name",text="Name")
treeview.heading("class",text="Class")
treeview.heading("department",text="go")



treeview.pack(side=TOP,fill=BOTH)



root.mainloop()