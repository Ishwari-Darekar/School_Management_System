import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from tkvideo import tkvideo
import customtkinter as ctk

root = Tk()
root.title('Login')
root.geometry('850x450+300+100')
root.configure(bg='#fff')
root.resizable(False, False)
####MAIN_FRAME[1]---------------
def signin():
    username=user.get()
    password=code.get()

    if username=='admin' and password=='123':
        import sms
    elif username!='admin' and password!='123':
        messagebox.showerror("Invalid","Invalid Username and Password")
    elif password!='123':
        messagebox.showerror("Invalid","Invalid password")
    elif username!='admin':
        messagebox.showerror("Invalid","Invalid username")

#photo_image=ImageTk.PhotoImage(file="loginimg.jpg")
#lbl_photo_image=Label(root,image=photo_image,bd=0).place(x=10,y=80)
lblvideo=Label(root)
lblvideo.pack(side=LEFT)
player=tkvideo("final.mp4",lblvideo,loop=1,size=(560,440))
player.play()

frame = Frame(root, width=280, height=720, bg="white")
frame.place(x=510,y=0)

heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=90, y=50)

#####--USER NAME-------------
def on_enter(e):
    user.delete(0, 'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0, 'Username')

user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light',11))
user.place(x=30, y=140)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=170)

#####--PASSWORD-------------
def on_enter(e):
    code.delete(0, 'end')
def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0, 'Password')

code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light',11))
code.place(x=30, y=190)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=220)

#####--BUTTON--------------
Button(frame, width=39, pady=7,text='sign in', bg='#57a1f8', fg='white',border=0 ,command=signin).place(x=30,y=270)
label=Label(frame, text="Don't have an account?", fg='black',bg='white', font=('Microsoft YaHei UI Light',9))
label.place(x=60, y=330)

sign_up = Button(frame, width=6, text='Sign up',border=0, bg='white',cursor='hand2', fg='#57a1f8')
sign_up.place(x=200, y=330)


root.mainloop()
