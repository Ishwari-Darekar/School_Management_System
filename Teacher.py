import tkinter
import tkinter as tk
from tkinter import Button, StringVar, Widget, ttk, messagebox, Frame
from tkinter.constants import END, RIGHT, BOTTOM
from tkinter.ttk import Treeview
from tkinter import PhotoImage
from PIL import Image,ImageTk
import customtkinter as ctk
from mysql.connector import cursor

###########MAIN_FRAME[4]-----------------------------------------------------------------------------------------------------------------
#root=tk.Tk()
root=tk.Toplevel()
root.title('Teacher Interface')
root.geometry('1350x700+0+0')
root.configure(bg='#131E3A')
root.resizable(True,True)

###############################--IMAGE--##############################

txt=tkinter.Label(root,text="It was a long cherished idea of the founder to have a CBSE School to cater quality education as per the growing demands of the public.Thereby followed"+'\n'+'the formation of the CBSE school in the year 2006. Where state board English Medium school was converted into a full fledged CBSE school on switch'+'\n'+'over category upto secondary level. On its successful run the authorities have aimed to upgrade the school from Secondary level to Senior Secondary level'+'\n'+'(+2) in the year 2012. The school was affiliated to CBSE successfully and continued to create a bench mark and became a feather in the cap of Bharati'+'\n'+'Vidyapeeth.The school believes in shaping its students. morally, ethically, spiritually, physically sound/fit for their success towards a better tomorrow.'+'\n'+'Inculcation of morality in the minds of its pupils is the priority as the school believes in. Students of the school have excelled at International levels in IT,'+'\n'+'Science , Maths Olympiads & National Graphics Championships Quizes etc.',font=("times new roman",15),fg="white",bg="#131E3A")
txt.place(x=20,y=100)

img1=ImageTk.PhotoImage(Image.open("school1.jpg"))
img2=ImageTk.PhotoImage(Image.open("prirncip.jpg"))
img3=ImageTk.PhotoImage(Image.open("eve1.jpg"))
img4=ImageTk.PhotoImage(Image.open("dance.jpg"))
img5=ImageTk.PhotoImage(Image.open("dance4.jpg"))
l=tkinter.Label(root)
l.pack(padx=200,pady=150,side=BOTTOM)
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

#######################################################################################################################
style=ttk.Style()
style.theme_use("default")
style.configure("Treeview",background="white",foreground="black",rowheight=25,fieldbackground="white")
style.map("Treeview",background=[("selected","darkred")])

####PYTHON_SQL_CONNECTIVITY-----------------------------------------------------------------------------------------------------------------
def home():
    import mysql.connector
    def connect():
         global mycursor
         global con
         try:
              con = mysql.connector.connect(host='localhost', user='root', passwd='admin123',database="sms",auth_plugin='mysql_native_password')
              mycursor = con.cursor()
              if con.is_connected:
                  print('connected')
              else:
                  print('error')

         except Exception as ProgrammingError:
             messagebox.showerror("error",parent=main_frame)
         con.commit()

    def insert_data():
        '''db = mysql.connector.connect(host="localhost", user="root", passwd="admin123", database="sms")'''
        cursor = con.cursor()
        ID = id_ent.get()
        NAME= name_ent.get()
        GENDER = gen_ent.get()
        AGE= age_ent.get()
        DATE_OF_BIRTH = ent_ent.get()
        PHONE_NO = mid_ent.get()
        ADDRESS= fin_ent.get()
        DATE_OF_JOINING= gpa_ent.get()
        try:
            cursor.execute("INSERT INTO sms(ID,NAME,GENDER,AGE,DATE_OF_BIRTH,PHONE_NO,ADDRESS,DATE_OF_JOINING) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(ID,NAME,GENDER,AGE,DATE_OF_BIRTH,PHONE_NO,ADDRESS,DATE_OF_JOINING))
            con.commit()
            print("data added successfully")
        except mysql.connector.Error as err:
               print(f"Eroor:{err}")
               con.rollback()

    def auto_select():
        if student_tabel.get_children():
            first_item=student_tabel.get_children()[0]
            student_tabel.selection_set(first_item)

    def delete_data_sql():
        auto_select()
        cursor = con.cursor()
        ID = id_ent.get()
        try:
            cursor.execute('DELETE FROM sms WHERE ID=%s',(ID,))
            con.commit()
            print("data deleted successfully")
        except mysql.connector.Error as err:
            print(f"Eroor:{err}")
            con.rollback()

#CONNECT_BUTTON_FOR_CONNECTION_OF_DATABASE------------------------------------------------------------------------------------------------
    connect_btn = tk.Button(head_frame, text="Connect", bg="#f0687c", fg="white", font=('Arial', 14, 'bold'), bd=2,
                            command=connect)
    connect_btn.place(x=1130, y=4)

    f2 = tk.Frame(root, bg='#131E3A', width=1500, height=900)
    f2.place(x=0, y=45)
    l2 = tk.Label(root, bg='#131E3A', font=('Arial', 30))
    l2.place(x=290, y=105)

####HOME_FRAME_LEFT_PANEL-----------------------------------------------------------------------------------------------------------------
    detail_frame = tk.LabelFrame(root, text="Student Record", font=("Arial", 14), bg="#131E3A", foreground="white", relief=tk.GROOVE)
    detail_frame.place(x=35, y=90, width=420, height=526)

    data_frame = tk.Frame(root, bg="teal", relief=tk.GROOVE)
    data_frame.place(x=490, y=98, width=760, height=526)
#----------------------ID---------------------------------------------------------
    id_lab = tk.Label(detail_frame, text="Id:", font=("Arial", 14), bg="#131E3A", foreground="white")
    id_lab.place(x=20,y=15)
    id_ent = tk.Entry(detail_frame, bd=1, font=("Arial", 14), bg="white", foreground="black")
    id_ent.place(x=110,y=17,width=290,height=30)
#------------------NAME-------------------------------------------------------------
    name_lab = tk.Label(detail_frame, text="Name:", font=("Arial", 14), bg="#131E3A", foreground="white")
    name_lab.place(x=20, y=65)
    name_ent = tk.Entry(detail_frame, bd=1, font=("Arial", 14), bg="white", foreground="black")
    name_ent.place(x=110, y=65, width=290, height=30)
#-------------------GENDER---------------------------------------------------------
    gen_lab = tk.Label(detail_frame, text="Gender:",bd=1, font=("Arial", 14), bg="#131E3A", foreground="white")
    gen_lab.place(x=18, y=120)
    gen_ent = ttk.Combobox(detail_frame, font=("ariel", 16))
    gen_ent["values"] = ("Male", "Female", "Other")
    gen_ent.place(x=110, y=120, width=290, height=30)
#----------------------------AGE-------------------------------------------------------
    age_lab = tk.Label(detail_frame, text="Age:", font=("ariel", 16), bg="#131E3A", foreground="white")
    age_lab.place(x=20, y=161)
    age_ent = tk.Entry(detail_frame, bd=1, font=("ariel", 16), bg="white", foreground="black")
    age_ent.place(x=110, y=161, width=290, height=30)
#----------------------------DOB---------------------------------------------
    ent_lab = tk.Label(detail_frame, text="DOB:", font=("ariel", 16), bg="#131E3A", foreground="white")
    ent_lab.place(x=20, y=209)
    ent_ent = tk.Entry(detail_frame, bd=1, font=("ariel", 16), bg="white", foreground="black")
    ent_ent.place(x=110, y=209, width=290, height=30)
# ---------------------------------DOJ-------------------------------------------------------------
    gpa_lab = tk.Label(detail_frame, text="DOJ:", font=("ariel", 16), bg="#131E3A", foreground="white")
    gpa_lab.place(x=20, y=353)
    gpa_ent = tk.Entry(detail_frame, bd=1, font=("ariel", 16), bg="white", foreground="black")
    gpa_ent.place(x=110, y=353, width=290, height=30)
#---------------------------------PH.NO-----------------------------------------------
    mid_lab = tk.Label(detail_frame, text="Ph.no:", font=("ariel", 16), bg="#131E3A", foreground="white")
    mid_lab.place(x=20, y=257)
    mid_ent = tk.Entry(detail_frame, bd=1, font=("ariel", 16), bg="white", foreground="black")
    mid_ent.place(x=110, y=257, width=290, height=30)
#-----------------------ADDRESS-------------------------------------------------------------------
    fin_lab = tk.Label(detail_frame, text="Address:", font=("ariel", 16), bg="#131E3A", foreground="white")
    fin_lab.place(x=20, y=305)
    fin_ent = tk.Entry(detail_frame, bd=1, font=("ariel", 16), bg="white", foreground="black")
    fin_ent.place(x=110, y=305, width=290, height=30)
###########----------------bottom_BUTTON--------------------------------------------------------
    btn_frame = tk.Frame(detail_frame, bg="#131E3A", bd=0, relief=tk.GROOVE)
    btn_frame.place(x=40, y=390, width=330, height=108)

##########RIGHT_PANEL_TREEVIEW------------------------------------------------------------------------------------------------------------
    main_frame: Frame = tk.Frame(data_frame, bg="teal", bd=2, relief=tk.GROOVE)
    main_frame.pack(fill=tk.BOTH, expand=True)

    y_scroll = tk.Scrollbar(data_frame, orient=tk.VERTICAL)
    x_scroll = tk.Scrollbar(data_frame, orient=tk.HORIZONTAL)

    student_tabel:Treeview = ttk.Treeview(main_frame, columns=(
    "ID", "NAME", "GENDER", "AGE", "DATE OF BIRTH", "PHONE.NO","ADDRESS",  "DATE OF JOINING"),
                                 yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)
    y_scroll.config(command=student_tabel.yview)
    x_scroll.config(command=student_tabel.xview)
    y_scroll.pack(side=RIGHT, fill=tk.Y)
    x_scroll.pack(side=BOTTOM, fill=tk.X)
    student_tabel.pack(fill=tk.BOTH, expand=True)

    student_tabel.heading("ID", text="ID")
    student_tabel.config(show="headings")
    student_tabel.heading("NAME", text="NAME")
    student_tabel.heading("GENDER", text="GENDER")
    student_tabel.heading("AGE", text="AGE")
    student_tabel.heading("DATE OF BIRTH", text="DATE OF BIRTH")
    student_tabel.heading("PHONE.NO", text="PHONE.NO")
    student_tabel.heading("ADDRESS", text="ADDRESS")
    student_tabel.heading("DATE OF JOINING", text="DATE OF JOINING")

    student_tabel.column("ID",width=100)
    student_tabel.column("NAME", width=100)
    student_tabel.column("GENDER", width=100)
    student_tabel.column("AGE", width=100)
    student_tabel.column("DATE OF BIRTH", width=100)
    student_tabel.column("PHONE.NO", width=100)
    student_tabel.column("ADDRESS", width=100)
    student_tabel.column("DATE OF JOINING", width=100)

    student_tabel.pack(fill=tk.BOTH, expand=True)

    #default data
    data = [["101", "abc", "Female", "12", "2009-03-23", "98870562", "cbd belapur", "2012-03-09"],
          ["102", "xyz", "Male", "13", "2010-06-210",  "988705624","cbd belapur", "2012-03-09"],
          ["103", "pqr", "Male", "12", "2007-03-23",  "123456789","cbd belapur", "2012-03-09"],
          ["104", "mno", "Female", "12", "2006-03-15",  "135791357","cbd belapur", "2012-03-09"]]

    student_tabel.tag_configure("oddrow", background="white")
    student_tabel.tag_configure("evenrow", background="#00AEAE")

    global count
    count = 0
    for record in data:
        if count % 2 == 0:
            student_tabel.insert(parent="", index="end", iid=count , text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]),tags=("evenrow"))
        else:
            student_tabel.insert(parent="", index="end", iid=count,text="",values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]),tags=("oddrow"))
        count += 1

    #add
        def add_rec():
            student_tabel.tag_configure("oddrow",background="white")
            student_tabel.tag_configure("evenrow",background="#00AEAE")

            global count
            if count % 2 == 0:
                student_tabel.insert(parent="",index="end",iid=count,text="",values=(id_ent.get(),name_ent.get(),gen_ent.get(),age_ent.get(),ent_ent.get(),mid_ent.get(),fin_ent.get(),gpa_ent.get()),tags=("evenrow"))
            else:
                student_tabel.insert(parent="",index="end",iid=count,text="",values=(id_ent.get(),name_ent.get(),age_ent.get(),gen_ent.get(),ent_ent.get(),mid_ent.get(),fin_ent.get(),gpa_ent.get()),tags=("oddrow"))

            count+=1
            insert_data()

        #Delete all function
        def delete_one():
            x=student_tabel.selection()[0]
            student_tabel.delete(x)
            delete_data_sql()

        #select record

        def select_record():
            delete_data_sql()
            id_ent.delete(0,tk.END)
            name_ent.delete(0,tk.END)
            gen_ent.delete(0,tk.END)
            age_ent.delete(0, tk.END)
            ent_ent.delete(0,tk.END)
            mid_ent.delete(0,tk.END)
            fin_ent.delete(0,tk.END)
            gpa_ent.delete(0,tk.END)

            selected = student_tabel.focus()
            values = student_tabel.item(selected,"values")

            id_ent.insert(0, values[0])
            name_ent.insert(0, values[1])
            gen_ent.insert(0, values[2])
            age_ent.insert(0, values[3])
            ent_ent.insert(0, values[4])
            mid_ent.insert(0, values[5])
            fin_ent.insert(0, values[6])
            gpa_ent.insert(0,values[7])

        def update_record():
            insert_data()
            selected =  student_tabel.focus()
            student_tabel.item(selected,text="",values=(id_ent.get(),name_ent.get(),gen_ent.get(),age_ent.get(),ent_ent.get(),mid_ent.get(),fin_ent.get(),gpa_ent.get()))

            id_ent.delete(0, END)
            name_ent.delete(0, END)
            gen_ent.delete(0, END)
            age_ent.delete(0, END)
            ent_ent.delete(0, END)
            mid_ent.delete(0, END)
            fin_ent.delete(0, END)
            gpa_ent.delete(0, END)

            #clear boxes
            id_ent.delete(0, END),
            name_ent.delete(0, END),
            gen_ent.delete(0, END),
            age_ent.delete(0, END),
            ent_ent.delete(0, END),
            mid_ent.delete(0, END),
            fin_ent.delete(0, END),
            gpa_ent.delete(0, END)

#####BUTTONS_FOR_EXECUTION_OF_COMMAND-----------------------------------------------------------------------------------------------------
    add_btn = tk.Button(btn_frame, bg="#FF007F", text="Add", bd=5, font=("arial", 13), width=15,command=add_rec)
    add_btn.grid(row=0, column=0, padx=10, pady=2)

    update_btn = tk.Button(btn_frame, bg="#B0FC38", text="Update", bd=5, font=("arial", 13), width=15,command=select_record)
    update_btn.grid(row=0, column=1, padx=3, pady=2)

    delete_btn = tk.Button(btn_frame, bg="#FBBD04", text="Delete", bd=5, font=("arial", 13), width=15,command=delete_one)
    delete_btn.grid(row=1, column=0, padx=2, pady=2)

    save_btn = tk.Button(btn_frame, bg="#63C5DA", text="Save", bd=5, font=("arial", 13), width=15, command=update_record)
    save_btn.grid(row=1, column=1, padx=3, pady=2)

########TOGGLE_FUNCTION-------------------------------------------------------------------------------------------------------------------
    toggle_menu()

########RESULT_FRAME----------------------------------------------------------------------------------------------------------------------
def result():
    f2 = tk.Frame(root, bg='#131E3A', width=1400, height=1000)
    f2.place(x=0, y=45)
    l1 = tk.Label(root, bg='#131E3A', font=('Arial', 30))
    l1.place(x=290, y=105)

#####PYTHON_MYSQL_CONNECTIVITY-------------------------------------------------------------------------------------------------------------
    import mysql.connector
    def connection():
        global mycursor
        global con
        try:
            con = mysql.connector.connect(host='localhost', user='root', passwd='admin123', database="student_result",
                                          auth_plugin='mysql_native_password')
            mycursor = con.cursor()
            if con.is_connected:
                print('connected')
            else:
                print('error')

        except Exception as ProgrammingError:
            messagebox.showerror("error", parent=main_frame)
        con.commit()

    def insert_record():
        cursorr = con.cursor()
        ID = id_ent.get()
        NAME = name_ent.get()
        ENGLISH = english_ent.get()
        COMPUTER_SCIENCE = computerscience_ent.get()
        MATHS = maths_ent.get()
        PHYSICS = physics_ent.get()
        CHEMISTRY = chemistry_ent.get()

        try:
            cursorr.execute(
                "INSERT INTO student_result(ID,NAME,ENGLISH,COMPUTER_SCIENCE,MATHS,PHYSICS,CHEMISTRY) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                (ID, NAME, ENGLISH, COMPUTER_SCIENCE, MATHS, PHYSICS, CHEMISTRY))
            con.commit()
            print("data added successfully")
        except mysql.connector.Error as err:
            print(f"Eroor:{err}")
            con.rollback()

    def auto_select():
        if student_tabel.get_children():
            first_item=student_tabel.get_children()[0]
            student_tabel.selection_set(first_item)

    def delete_data_sqll():
        auto_select()
        cursorr = con.cursor()
        ID = id_ent.get()
        try:
            cursorr.execute('DELETE FROM student_result WHERE ID=%s',(ID,))
            con.commit()
            print("data deleted successfully")
        except mysql.connector.Error as err:
            print(f"Eroor:{err}")
            con.rollback()


####LEFT_PANEL_RESULT_FRAME----------------------------------------------------------------------------------------------------------------------
    detail_frame = tk.LabelFrame(root, text="Student Result", font=("Arial", 14), bg="#131E3A", foreground="white",
                                 relief=tk.GROOVE)
    detail_frame.place(x=35, y=90, width=420, height=526)

    data_frame = tk.Frame(root, bg="teal", relief=tk.GROOVE)
    data_frame.place(x=490, y=98, width=760, height=526)
####----------------------ID---------------------------------------------------------
    id_lab = tk.Label(detail_frame, text="Id:", font=("Arial", 14), bg="#131E3A", foreground="white")
    id_lab.place(x=7, y=15)
    id_ent = tk.Entry(detail_frame, bd=1, font=("Arial", 14), bg="white", foreground="black")
    id_ent.place(x=110, y=17, width=290, height=30)
######-----------------NAME-------------------------------------------------------------
    name_lab = tk.Label(detail_frame, text="Name:", font=("Arial", 14), bg="#131E3A", foreground="white")
    name_lab.place(x=7, y=65)
    name_ent = tk.Entry(detail_frame, bd=1, font=("Arial", 14), bg="white", foreground="black")
    name_ent.place(x=110, y=65, width=290, height=30)
######-------------------GENDER---------------------------------------------------------
    english_lab = tk.Label(detail_frame, text="English:", font=("ariel", 16), bg="#131E3A",
                                   foreground="white")
    english_lab.place(x=7, y=120)
    english_ent = tk.Entry(detail_frame, bd=1, font=("ariel", 16), bg="white", foreground="black")
    #English_ent["values"] = ("Male", "Female", "Other")
    english_ent.place(x=110, y=120, width=290, height=30)
#######----------------------------AGE-------------------------------------------------------
    computerscience_lab = tk.Label(detail_frame, text="Computer "'\n'
                                                "Science:", font=("ariel", 16), bg="#131E3A", foreground="white")
    computerscience_lab.place(x=7, y=161)
    computerscience_ent = tk.Entry(detail_frame, bd=1, font=("ariel", 16), bg="white", foreground="black")
    computerscience_ent.place(x=110, y=175, width=290, height=30)
######----------------------------DOB---------------------------------------------
    maths_lab = tk.Label(detail_frame, text="Maths:", font=("ariel", 16), bg="#131E3A", foreground="white")
    maths_lab.place(x=7, y=222)
    maths_ent = tk.Entry(detail_frame, bd=1, font=("ariel", 16), bg="white", foreground="black")
    maths_ent.place(x=110, y=222, width=290, height=30)
##########---------------------------------DOJ-------------------------------------------------------------
    physics_lab = tk.Label(detail_frame, text="Physics:", font=("ariel", 16), bg="#131E3A", foreground="white")
    physics_lab.place(x=7, y=270)
    physics_ent = tk.Entry(detail_frame, bd=1, font=("ariel", 16), bg="white", foreground="black")
    physics_ent.place(x=110,y=270, width=290, height=30)
####---------------------------------PH.NO-----------------------------------------------
    chemistry_lab = tk.Label(detail_frame, text="Chemistry:", font=("ariel", 16), bg="#131E3A", foreground="white")
    chemistry_lab.place(x=7, y=318)
    chemistry_ent = tk.Entry(detail_frame, bd=1, font=("ariel", 16), bg="white", foreground="black")
    chemistry_ent.place(x=110, y=318, width=290, height=30)

###########BUTTON--------------------------------------------------------
    btn_frame = tk.Frame(detail_frame, bg="#131E3A", bd=0, relief=tk.GROOVE)
    btn_frame.place(x=40, y=390, width=330, height=108)

#RIGHT_PANEL_TREEVIEW--------------------------------------------------------------------------------------------------------------------
    main_frame: Frame = tk.Frame(data_frame, bg="teal", bd=2, relief=tk.GROOVE)
    main_frame.pack(fill=tk.BOTH, expand=True)

    y_scroll = tk.Scrollbar(data_frame, orient=tk.VERTICAL)
    x_scroll = tk.Scrollbar(data_frame, orient=tk.HORIZONTAL)

    student_tabel: Treeview = ttk.Treeview(main_frame, columns=(
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
    #student_tabel.heading("DATE OF JOINING", text="DATE OF JOINING")

    student_tabel.column("ID", width=100)
    student_tabel.column("NAME", width=100)
    student_tabel.column("ENGLISH", width=100)
    student_tabel.column("COMPUTER_SCIENCE", width=100)
    student_tabel.column("MATHS", width=100)
    student_tabel.column("PHYSICS", width=100)
    student_tabel.column("CHEMISTRY", width=100)
    #student_tabel.column("DATE OF JOINING", width=100)
    data = [['101', 'abc', '1', '2', '3', '4', '5'],
            ['102', 'xyz', '1', '2', '3', '4', '5'],
            ['103', 'pqr', '1', '2', '3', '4', '5'],
            ['104', 'mno', '1', '2', '3', '4', '5']]

    student_tabel.tag_configure("oddrow", background="white")
    student_tabel.tag_configure("evenrow", background="#00AEAE")

    global count
    count = 0
    for record in data:
        if count % 2 == 0:
            student_tabel.insert(parent="", index="end", iid=count, text="", values=(
                record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=("evenrow"))
        else:
            student_tabel.insert(parent="", index="end", iid=count, text="", values=(
                record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=("oddrow"))
        count += 1

        def add_res():
            student_tabel.tag_configure("oddrow", background="white")
            student_tabel.tag_configure("evenrow", background="#00AEAE")

            global count
            if count % 2 == 0:
                student_tabel.insert(parent="", index="end", iid=count, text="", values=(id_ent.get(), name_ent.get(), english_ent.get(), computerscience_ent.get(), maths_ent.get(),physics_ent.get(), chemistry_ent.get()), tags=("evenrow"))
            else:
                student_tabel.insert(parent="", index="end", iid=count, text="", values=(id_ent.get(), name_ent.get(), english_ent.get(), computerscience_ent.get(), maths_ent.get(),physics_ent.get(), chemistry_ent.get()), tags=("oddrow"))

            count += 1
            insert_record()

    def delete_one():
        x = student_tabel.selection()[0]
        student_tabel.delete(x)
        delete_data_sqll()

    def select_record_result():
        delete_data_sqll()
        id_ent.delete(0, tk.END)
        name_ent.delete(0, tk.END)
        english_ent.delete(0, tk.END)
        computerscience_ent.delete(0, tk.END)
        maths_ent.delete(0, tk.END)
        physics_ent.delete(0, tk.END)
        chemistry_ent.delete(0, tk.END)

        selected = student_tabel.focus()
        values = student_tabel.item(selected, "values")

        id_ent.insert(0, values[0])
        name_ent.insert(0, values[1])
        english_ent.insert(0, values[2])
        computerscience_ent.insert(0, values[3])
        maths_ent.insert(0, values[4])
        physics_ent.insert(0, values[5])
        chemistry_ent.insert(0, values[6])

    def update_record_result():
        insert_record()
        selected = student_tabel.focus()
        student_tabel.item(selected, text="", values=(
        id_ent.get(), name_ent.get(), english_ent.get(), computerscience_ent.get(), maths_ent.get(), physics_ent.get(), chemistry_ent.get()))

        id_ent.delete(0, END)
        name_ent.delete(0, END)
        english_ent.delete(0, END)
        computerscience_ent.delete(0, END)
        maths_ent.delete(0, END)
        physics_ent.delete(0, END)
        chemistry_ent.delete(0, END)

        # clear boxes
        id_ent.delete(0, END),
        name_ent.delete(0, END),
        english_ent.delete(0, END),
        computerscience_ent.delete(0, END),
        maths_ent.delete(0, END),
        physics_ent.delete(0, END),
        chemistry_ent.delete(0, END)
#######CONNECT BTN-----------------------
    connect_btn = tk.Button(head_frame, text="Connect", bg="#f0687c", fg="white", font=('Arial', 14, 'bold'), bd=2,
                            command=connection)
    connect_btn.place(x=1130, y=4)

    student_tabel.pack(fill=tk.BOTH, expand=True)
####BUTTON_FOR_EXECUTION_OF_COMMAND---------------------------------------------------------------------------------------------------------------------------
    add_btn = tk.Button(btn_frame, bg="#FF007F", text="Add", bd=5, font=("arial", 13), width=15,command=add_res)
    add_btn.grid(row=0, column=0, padx=10, pady=2)

    update_btn = tk.Button(btn_frame, bg="#B0FC38", text="Update", bd=5, font=("arial", 13), width=15,command=select_record_result)
    update_btn.grid(row=0, column=1, padx=3, pady=2)

    delete_btn = tk.Button(btn_frame, bg="#FBBD04", text="Delete", bd=5, font=("arial", 13), width=15,command=delete_one)
    delete_btn.grid(row=1, column=0, padx=2, pady=2)

    save_btn = tk.Button(btn_frame, bg="#63C5DA", text="Save", bd=5, font=("arial", 13), width=15,command=update_record_result)
    save_btn.grid(row=1, column=1, padx=3, pady=2)

    toggle_menu()

######-----TOGGLE_MENU-------------------------------------------------------------------
def toggle_menu():
    def collapse_toggle_menu():
        toggle_menu_fm.destroy()
        toggle_btn.config(text='☰')
        toggle_btn.config(command=toggle_menu)

    toggle_menu_fm = tk.Frame(root, bg='#f0687c')


    home_btn = tk.Button(toggle_menu_fm, text='Home', font=('Bold', 20), bd=0, bg='#f0687c', fg='white',
                           activebackground='#f0687c', activeforeground='white', command=home)
    home_btn.place(x=20, y=20)

    attendance_btn = tk.Button(toggle_menu_fm, text='Result', font=('Bold', 20), bd=0, bg='#f0687c', fg='white',
                               activebackground='#f0687c', activeforeground='white', command=result)
    attendance_btn.place(x=20, y=80)

######Top Label-------------

    window_height = root.winfo_height()
    toggle_menu_fm.place(x=0, y=40, height=window_height, width=200)
    toggle_btn.config(text='X')
    toggle_btn.config(command=collapse_toggle_menu)

head_frame = tk.Frame(root,bg="#f0687c", highlightbackground='white',highlightthickness=1)

toggle_btn = tk.Button(head_frame, text='☰', bg='#f0687c', fg='white', font=('Bold',20), bd=0, activebackground='#f0687c', activeforeground='white', command=toggle_menu)
toggle_btn.pack(side=tk.LEFT)

title_lb = tk.Label(head_frame, text='                                         BHARATI  VIDYAPEETH  ENG.  MED  SCHOOL',bg='#f0687c', fg='white',font=('Bold', 20))
title_lb.pack(side=tk.LEFT)

head_frame.pack(side=tk.TOP,fill=tk.X)
head_frame.pack_propagate(False)
head_frame.configure(height=50)

root.mainloop()
