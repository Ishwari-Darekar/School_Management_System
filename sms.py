import tkinter
from tkinter import *
from PIL import ImageTk,Image
import customtkinter as ctk

#####MAIN-FRAME[2]------------------------------------
root=tkinter.Toplevel()
root.geometry('1350x700+0+0')
root.title('School Management System')
root.configure(bg="#131E3A")

Label(root,width=1350,height=3,bg='#f0687c',text='BHARATI  VIDYAPEETH  ENG.  MED  SCHOOL'+'\n'+'Sector  -  3  ,  C.B.D  ,  Belapur  ,  Navi Mumbai  -  400614  ',fg='#fff',font=('arial 20 bold'),highlightbackground='white',highlightthickness=1).pack(side=TOP)

#####--STUDENT INTERFACE--------------------
def student():
    import student
butt1=tkinter.Button(root,text="STUDENT",font=('Arial', 23, 'bold'),bd=5,width=29,pady=40,bg='#00FFFF', fg='black',command=student).place(x=50, y=340)

#####--TEACHER INTERFACE--------------------------
def teacher():
    import Teacher
butt2=tkinter.Button(root,text="TEACHER",font=('Arial', 23, 'bold'),bd=5,width=29,pady=40,bg='#FFD801', fg='black',command=teacher).place(x=650, y=340)

bvp_sym=ctk.CTkImage(Image.open('bvp-removebg-preview.png'),size=(400,200))
bvp_lbl=ctk.CTkButton(root,text="",width=2,height=10,fg_color="#131E3A",corner_radius=200,hover=False,image=bvp_sym)
bvp_lbl.pack(pady=5)
root.mainloop()