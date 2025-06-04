import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ctk
from tkinter import ttk, messagebox, Frame
from tkinter.constants import RIGHT,BOTTOM
from tkinter.ttk import Treeview


####MAIN_FRAME[3]----------------------------------------------------------------------------------------------------------------------------
root = tk.Toplevel()
root.title('Student Interface')
root.geometry('1350x700+0+0')
root.configure(bg='#131E3A')

head_frame = tk.Frame(root,bg="#f0687c", highlightbackground='white',highlightthickness=1)

title_lb = tk.Label(head_frame, text='                                         BHARATI  VIDYAPEETH  ENG.  MED  SCHOOL',bg='#f0687c', fg='white',font=('Bold', 20))
title_lb.pack(side=tk.LEFT)

head_frame.pack(side=tk.TOP,fill=tk.X)
head_frame.pack_propagate(False)
head_frame.configure(height=50)
#####_INSERTION_OF_VIDEO-------------------------

img1=ImageTk.PhotoImage(Image.open("school1.jpg"))
img2=ImageTk.PhotoImage(Image.open("prirncip.jpg"))
img3=ImageTk.PhotoImage(Image.open("eve1.jpg"))
img4=ImageTk.PhotoImage(Image.open("dance.jpg"))
img5=ImageTk.PhotoImage(Image.open("dance4.jpg"))
l=Label(root)
l.pack(pady=150,padx=100)
l.pack()
x=1
def move():
    global x

    if l==4:
        x=1
    if x==1:
        l.config(image=img1)
    elif x==2:
        l.config(image=img2)
    elif x == 3:
        l.config(image=img3)
    elif x==4:
        l.config(image=img4)
    elif x==5:
        l.config(image=img5)
    elif x==6:
        l.config(image=img1)
    elif x==7:
        l.config(image=img2)
    elif x == 8:
        l.config(image=img3)
    elif x==9:
        l.config(image=img4)
    elif x==10:
        l.config(image=img5)
    elif x==11:
        l.config(image=img1)
    x+=1
    root.after(2000,move)
move()


txt=Label(root,text="It was a long cherished idea of the founder to have a CBSE School to cater quality education as per the growing demands of the public.Thereby followed"+'\n'+'the formation of the CBSE school in the year 2006. Where state board English Medium school was converted into a full fledged CBSE school on switch'+'\n'+'over category upto secondary level. On its successful run the authorities have aimed to upgrade the school from Secondary level to Senior Secondary level'+'\n'+'(+2) in the year 2012. The school was affiliated to CBSE successfully and continued to create a bench mark and became a feather in the cap of Bharati'+'\n'+'Vidyapeeth.The school believes in shaping its students. morally, ethically, spiritually, physically sound/fit for their success towards a better tomorrow.'+'\n'+'Inculcation of morality in the minds of its pupils is the priority as the school believes in. Students of the school have excelled at International levels in IT,'+'\n'+'Science , Maths Olympiads & National Graphics Championships Quizes etc.',font=("times new roman",15),fg="white",bg="#131E3A")
txt.place(x=20,y=468)

#####HEADER-------------------------------------------------------------------------------------------------------------------------------
s="                                                                       Education   is   the   passport   to   the   future,  for   tommorow   belongs   to   those   who   prepare   for   it   today                                                                           "
sliderLabel=tk.Label(root,text=s,font=("Bistro",10,"bold"),fg="black")
sliderLabel.place(x=0,y=51)

menu_frame= LabelFrame(root,text="Menu",font=("times new roman",15),fg="white",bg="#131E3A")
menu_frame.place(x=20,y=90,width=1230,height=75)

######SUB_FARME----------------------------------------------------------------------------------------------------------------------------
######ABOUT_BUTTON------------------------------------------------------------------------------------------------------------------------
def aboutus_fm():
    def exit():
        bvp_lbl.destroy()
        btn_exit.destroy()

    btn_exit = tk.Button(root, text="  x  ", bg="red", fg="white", font=("Arial", 10, "bold"), command=exit)
    btn_exit.place(x=1215, y=167)

    bvp_sym = ctk.CTkImage(Image.open('about-fin.PNG'), size=(1200, 430))
    bvp_lbl = ctk.CTkButton(root, text="", width=900, height=60, fg_color="#131E3A", corner_radius=200, hover=False,
                            image=bvp_sym)
    bvp_lbl.place(x=0, y=190)

#####EVENT_BUTTON------------------------------------------------------------------------------------------------------------------------
def event_fm():
    def exit():

        btn_exit.destroy()
        bvp_lbl.destroy()
    btn_exit = tk.Button(root, text="  x  ", bg="red", fg="white", font=("Arial", 10, "bold"), command=exit)
    btn_exit.place(x=1215, y=167)

    bvp_sym = ctk.CTkImage(Image.open('event-fin.png'), size=(1200, 430))
    bvp_lbl = ctk.CTkButton(root, text="", width=900, height=60, fg_color="#131E3A", corner_radius=200, hover=False,
                            image=bvp_sym)
    bvp_lbl.place(x=0,y=190)

####RESULT_BUTTION------------------------------------------------------------------------------------------------------------------------
def result_fm():
    sub_frame=tk.Toplevel()
    sub_frame.title('Result')
    sub_frame.geometry('1250x400+10+230')
    sub_frame.configure(bg="#AFEEEE")
    sub_frame.resizable(False, False)
    l1=tk.Label(sub_frame,text='Enter student ID:',width=25,bg="#AFEEEE", foreground="black")
    l1.grid(row=10,column=2)
    e1=tk.Entry(sub_frame,width=10,bg='#F2F2F2',font=22)
    e1.grid(row=10,column=10,padx=10)

####PYTHON_SQL_CONNECTIVITY-----------------------------------------------------------------------------------------------------------------
    from mysql.connector import cursor
    import mysql.connector
    def connection():
        global mycursor
        global con
        global connection
        try:
            con = mysql.connector.connect(host='localhost', user='root', passwd='admin123', database="student_result",
                                          auth_plugin='mysql_native_password')
            mycursor = con.cursor()
            if con.is_connected:
                print('connected')
            else:
                print('error')

        except Exception as ProgrammingError:
            messagebox.showerror("error", parent=sub_frame)
        con.commit()
    def show_result():
        cursorr = con.cursor()
        ID = e1.get()
        try:
            cursorr.execute(
                'SELECT * FROM student_result where ID=%s',(ID,))
            result=cursorr.fetchone()
            if result:
                student_tabel.delete(*student_tabel.get_children())
                student_tabel.insert("","end",values=result)
                print("data found successfully")
            con.commit()

        except mysql.connector.Error as err:
            print(f"Eroor:{err}")
            con.rollback()

    def final_show_result():
        connection()
        show_result()

    b1 = tk.Button(sub_frame, text='Show result', width=15, bg='red',
                   command=final_show_result)
    b1.grid(row=10, column=60, padx=100, pady=20)

####TREEVIEW_OF_RESULT_TABLE--------------------------------------------------------------------------------------------------------------
    sub_frame: Frame = tk.Label(sub_frame, bg="teal", bd=2, relief=tk.GROOVE)
    sub_frame.place(x=100,y=100)

    y_scroll = tk.Scrollbar(sub_frame, orient=tk.VERTICAL)
    x_scroll = tk.Scrollbar(sub_frame, orient=tk.HORIZONTAL)

    student_tabel: Treeview = ttk.Treeview(sub_frame, columns=(
        "ID", "NAME", "ENGLISH", "COMPUTER_SCIENCE", "MATHS", "PHYSICS", "CHEMISTRY"),
                                           yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)
    y_scroll.config(command=student_tabel.yview)
    x_scroll.config(command=student_tabel.xview)
    y_scroll.pack(side=RIGHT, fill=tk.Y)
    x_scroll.pack(side=BOTTOM, fill=tk.X)
    student_tabel.pack(fill=tk.BOTH, expand=True)

    student_tabel.heading("ID", text="ID")
    student_tabel.config(show="headings")
    student_tabel.heading("NAME", text="NAME")
    student_tabel.heading("ENGLISH", text="ENGLISH")
    student_tabel.heading("COMPUTER_SCIENCE", text="COMPUTER_SCIENCE")
    student_tabel.heading("MATHS", text="MATHS")
    student_tabel.heading("PHYSICS", text="PHYSICS")
    student_tabel.heading("CHEMISTRY", text="CHEMISTRY")

    student_tabel.column("ID", width=150)
    student_tabel.column("NAME", width=150)
    student_tabel.column("ENGLISH", width=150)
    student_tabel.column("COMPUTER_SCIENCE", width=150)
    student_tabel.column("MATHS", width=150)
    student_tabel.column("PHYSICS", width=150)
    student_tabel.column("CHEMISTRY", width=150)

def notice_fm():
    def exit():
        btn_exit.destroy()
        bvp_lbl.destroy()
    btn_exit = tk.Button(root, text="  x  ", bg="red", fg="white", font=("Arial", 10, "bold"), command=exit)
    btn_exit.place(x=1215, y=167)

    bvp_sym = ctk.CTkImage(Image.open('holiday.jpg'), size=(1200, 430))
    bvp_lbl = ctk.CTkButton(root, text="", width=900, height=60, fg_color="#131E3A", corner_radius=200, hover=False,
                            image=bvp_sym)
    bvp_lbl.place(x=0,y=190)

#####CONTACT_BUTTON-----------------------------------------------------------------------------------------------------------------------
def contact_fm():
    def exit():
        bvp_lbl.destroy()
        btn_exit.destroy()

    btn_exit = tk.Button(root, text="  x  ", bg="red", fg="white", font=("Arial", 10, "bold"), command=exit)
    btn_exit.place(x=1215, y=167)

    bvp_sym = ctk.CTkImage(Image.open('contact-fin.PNG'), size=(1200, 430))
    bvp_lbl = ctk.CTkButton(root, text="", width=900, height=60, fg_color="#131E3A", corner_radius=200, hover=False,
                            image=bvp_sym)
    bvp_lbl.place(x=0, y=190)

#######################MAIN_FRAME BUTTONS-------------------------------------------------------------------------------------------------
btn_course=tk.Button(menu_frame,text="About Us",font=("Arial",15),bg="#00CCFF",fg="White",command=aboutus_fm)
btn_course.place(x=40,y=2,width=210,height=40)

btn_events=tk.Button(menu_frame,text="Events",font=("Arial",15),bg="#FEE123",fg="White",command=event_fm)
btn_events.place(x=275,y=2,width=210,height=40)

btn_result=tk.Button(menu_frame,text="Result",font=("Arial",15),bg="#FC46AA",fg="White",command=result_fm)
btn_result.place(x=514,y=2,width=210,height=40)

btn_notice=tk.Button(menu_frame,text="Notice",font=("Arial",15),bg="#A7F432",fg="White",command=notice_fm)
btn_notice.place(x=750,y=2,width=210,height=40)

btn_contact=tk.Button(menu_frame,text="Contact",font=("Arial",15),bg="#A32CC4",fg="White",command=contact_fm)
btn_contact.place(x=985,y=2,width=200,height=40)

root.mainloop()