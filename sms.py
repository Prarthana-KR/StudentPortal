from tkinter import *
from PIL import ImageTk
import ttkthemes
from tkinter import ttk, messagebox
import pymysql

con=pymysql.connect(host='localhost',user='root',password='0246813579')
mycursor=con.cursor()

def iexit():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass

def edit_student():
    def edit_data():
        query='update student Set Name=%s,Sem=%s,Program=%s,Department=%s,Fee_Amt=%s,Fee_Det=%s,Exam_Res=%s,SGPA=%s'
        mycursor.execute(query,(NameEntry.get(),SemEntry.get(),pEntry.get(),deptEntry.get(),feeaEntry.get(),feedEntry.get(),erEntry.get(),sgpaEntry.get()))
        con.commit()
        messagebox.showinfo('Success',f'Reg No. {RegNumEntry.get()} is edited successfully')
        edit_window.destroy()
        show_student()



    edit_window=Toplevel()
    edit_window.grab_set()
    edit_window.resizable(0,0)
    RegNumLabel=Label(edit_window,text='Reg No.',font=('times new roman','16'))
    RegNumLabel.grid(row=0,column=0,padx=30,pady=10)
    RegNumEntry=Entry(edit_window,font=('times new roman','15'),width=24)
    RegNumEntry.grid(row=0,column=1,pady=15,padx=10)

    NameLabel=Label(edit_window,text='Name',font=('times new roman','16'))
    NameLabel.grid(row=1,column=0,padx=30,pady=10)
    NameEntry=Entry(edit_window,font=('times new roman','15'),width=24)
    NameEntry.grid(row=1,column=1,pady=15,padx=10)   

    SemLabel=Label(edit_window,text='Semester',font=('times new roman','16'))
    SemLabel.grid(row=2,column=0,padx=30,pady=10)
    SemEntry=Entry(edit_window,font=('times new roman','15'),width=24)
    SemEntry.grid(row=2,column=1,pady=15,padx=10) 

    pLabel=Label(edit_window,text='Program',font=('times new roman','16'))
    pLabel.grid(row=3,column=0,padx=30,pady=10)
    pEntry=Entry(edit_window,font=('times new roman','15'),width=24)
    pEntry.grid(row=3,column=1,pady=15,padx=10)

    deptLabel=Label(edit_window,text='Department',font=('times new roman','16'))
    deptLabel.grid(row=4,column=0,padx=30,pady=10)
    deptEntry=Entry(edit_window,font=('times new roman','15'),width=24)
    deptEntry.grid(row=4,column=1,pady=15,padx=10)

    feeaLabel=Label(edit_window,text='Fee_Amount',font=('times new roman','16'))
    feeaLabel.grid(row=5,column=0,padx=30,pady=10)
    feeaEntry=Entry(edit_window,font=('times new roman','15'),width=24)
    feeaEntry.grid(row=5,column=1,pady=15,padx=10)

    feedLabel=Label(edit_window,text='Fee_Detail',font=('times new roman','16'))
    feedLabel.grid(row=6,column=0,padx=30,pady=10)
    feedEntry=Entry(edit_window,font=('times new roman','15'),width=24)
    feedEntry.grid(row=6,column=1,pady=15,padx=10)

    erLabel=Label(edit_window,text='Exam_Result',font=('times new roman','16'))
    erLabel.grid(row=7,column=0,padx=30,pady=10)
    erEntry=Entry(edit_window,font=('times new roman','15'),width=24)
    erEntry.grid(row=7,column=1,pady=15,padx=10)

    sgpaLabel=Label(edit_window,text='SGPA',font=('times new roman','16'))
    sgpaLabel.grid(row=8,column=0,padx=30,pady=10)
    sgpaEntry=Entry(edit_window,font=('times new roman','15'),width=24)
    sgpaEntry.grid(row=8,column=1,pady=15,padx=10)

    edit_student_button=ttk.Button(edit_window,text='EDIT',command=edit_data)
    edit_student_button.grid(row=9,columnspan=2,pady=10)

    indexing=studentTable.focus()

    content=studentTable.item(indexing)
    listdata=content['values']
    RegNumEntry.insert(0,listdata[0])
    NameEntry.insert(0,listdata[1])
    SemEntry.insert(0,listdata[2])
    pEntry.insert(0,listdata[3])
    deptEntry.insert(0,listdata[4])
    feeaEntry.insert(0,listdata[5])
    feedEntry.insert(0,listdata[6])
    erEntry.insert(0,listdata[7])
    sgpaEntry.insert(0,listdata[8])




def show_student():
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)

def delete_student():
    indexing=studentTable.focus()
    print(indexing)
    content=studentTable.item(indexing)
    content_id=content['values'][0]
    query='delete from student where RollNum=%s'
    mycursor.execute(query,(content_id))
    con.commit()
    messagebox.showinfo('Deleted',f'Register Number {content_id} details are deleted successfully')

def search_student():
    def search_data():
        query='select *from student where RollNum=%s or Name=%s'
        mycursor.execute(query,(RegNumEntry.get(),NameEntry.get()))
        fetched_data = mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        search_window.destroy()
        for data in fetched_data:
            studentTable.insert('',END,values=data)
        

    search_window=Toplevel()
    search_window.grab_set()
    search_window.resizable(False,False)
    RegNumLabel=Label(search_window,text='Search by Reg No.',font=('times new roman','16'))
    RegNumLabel.grid(row=0,column=0,padx=30,pady=10)
    RegNumEntry=Entry(search_window,font=('times new roman','15'),width=24)
    RegNumEntry.grid(row=0,column=1,pady=15,padx=10)

    NameLabel=Label(search_window,text='Search by Name',font=('times new roman','16'))
    NameLabel.grid(row=1,column=0,padx=30,pady=10)
    NameEntry=Entry(search_window,font=('times new roman','15'),width=24)
    NameEntry.grid(row=1,column=1,pady=15,padx=10)  

    search_student_button=ttk.Button(search_window,text='SEARCH', command=search_data)
    search_student_button.grid(row=2,columnspan=2,pady=10)



def add_student():
    global mycursor, con
    def add_data():
        query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        mycursor.execute(query,(RegNumEntry.get(),NameEntry.get(),SemEntry.get(),pEntry.get(),
                                deptEntry.get(),feeaEntry.get(),feedEntry.get(),erEntry.get(),sgpaEntry.get()))
        con.commit()
        reply=messagebox.showinfo('Work Complete','Data added successfully.')
        add_window.destroy()


    
    add_window=Toplevel()
    add_window.grab_set()
    add_window.resizable(0,0)
    RegNumLabel=Label(add_window,text='Reg No.',font=('times new roman','16'))
    RegNumLabel.grid(row=0,column=0,padx=30,pady=10)
    RegNumEntry=Entry(add_window,font=('times new roman','15'),width=24)
    RegNumEntry.grid(row=0,column=1,pady=15,padx=10)

    NameLabel=Label(add_window,text='Name',font=('times new roman','16'))
    NameLabel.grid(row=1,column=0,padx=30,pady=10)
    NameEntry=Entry(add_window,font=('times new roman','15'),width=24)
    NameEntry.grid(row=1,column=1,pady=15,padx=10)   

    SemLabel=Label(add_window,text='Semester',font=('times new roman','16'))
    SemLabel.grid(row=2,column=0,padx=30,pady=10)
    SemEntry=Entry(add_window,font=('times new roman','15'),width=24)
    SemEntry.grid(row=2,column=1,pady=15,padx=10) 

    pLabel=Label(add_window,text='Program',font=('times new roman','16'))
    pLabel.grid(row=3,column=0,padx=30,pady=10)
    pEntry=Entry(add_window,font=('times new roman','15'),width=24)
    pEntry.grid(row=3,column=1,pady=15,padx=10)

    deptLabel=Label(add_window,text='Department',font=('times new roman','16'))
    deptLabel.grid(row=4,column=0,padx=30,pady=10)
    deptEntry=Entry(add_window,font=('times new roman','15'),width=24)
    deptEntry.grid(row=4,column=1,pady=15,padx=10)

    feeaLabel=Label(add_window,text='Fee_Amount',font=('times new roman','16'))
    feeaLabel.grid(row=5,column=0,padx=30,pady=10)
    feeaEntry=Entry(add_window,font=('times new roman','15'),width=24)
    feeaEntry.grid(row=5,column=1,pady=15,padx=10)

    feedLabel=Label(add_window,text='Fee_Detail',font=('times new roman','16'))
    feedLabel.grid(row=6,column=0,padx=30,pady=10)
    feedEntry=Entry(add_window,font=('times new roman','15'),width=24)
    feedEntry.grid(row=6,column=1,pady=15,padx=10)

    erLabel=Label(add_window,text='Exam_Result',font=('times new roman','16'))
    erLabel.grid(row=7,column=0,padx=30,pady=10)
    erEntry=Entry(add_window,font=('times new roman','15'),width=24)
    erEntry.grid(row=7,column=1,pady=15,padx=10)

    sgpaLabel=Label(add_window,text='SGPA',font=('times new roman','16'))
    sgpaLabel.grid(row=8,column=0,padx=30,pady=10)
    sgpaEntry=Entry(add_window,font=('times new roman','15'),width=24)
    sgpaEntry.grid(row=8,column=1,pady=15,padx=10)

    add_student_button=ttk.Button(add_window,text='ADD',command=add_data)
    add_student_button.grid(row=9,columnspan=2,pady=10)



def connect_database():
    def connect():
        global mycursor,con
        try:
            con=pymysql.connect(host='localhost',user='root',password='0246813579')
            mycursor=con.cursor()
            messagebox.showinfo('Success','Database is connected',parent=connectWindow)
            connectWindow.destroy()
        except:
            messagebox.showerror('ERROR','Invalid Details',parent=connectWindow)
            return

        try:
            query='create database studentmanagementsystem'
            mycursor.execute(query)
            query='use studentmanagementsystem'
            mycursor.execute(query)
            query='create table student(RollNum int(5) not null primary key,Name char(10),Sem int(2),'\
                'Program char(10),Department char(5),Fee_Amt int(10),Fee_Det char(10),Exam_Res char(10),SGPA int(5));'
            mycursor.execute(query)
        except:
            query='use studentmanagementsystem'
            mycursor.execute(query)

            

    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)

    hostnameLabel=Label(connectWindow,text='Host Name',font=('comic sans ms',16))
    hostnameLabel.grid(row=1,column=0,padx=5,pady=15)

    hostEntry=Entry(connectWindow,font=('comic sans ms',16),bd=2)
    hostEntry.grid(row=1,column=1,padx=5,pady=15)

    usernameLabel=Label(connectWindow,text='Username',font=('comic sans ms',16))
    usernameLabel.grid(row=2,column=0,padx=5,pady=15)

    usernameEntry=Entry(connectWindow,font=('comic sans ms',16),bd=2)
    usernameEntry.grid(row=2,column=1,padx=5,pady=15)

    passwordLabel=Label(connectWindow,text='Password',font=('comic sans ms',16))
    passwordLabel.grid(row=3,column=0,padx=5,pady=15)

    passwordEntry=Entry(connectWindow,font=('comic sans ms',16),bd=2)
    passwordEntry.grid(row=3,column=1,padx=5,pady=15)

    connectButton=ttk.Button(connectWindow,text='Connect',width=15,command=connect)
    connectButton.grid(row=4,column=1,columnspan=2)


root=Tk()

backgroundImage=ImageTk.PhotoImage(file="w1.jpg")
bgLabel=Label(root,image=backgroundImage)
bgLabel.place(x=0,y=0)

root.geometry('1280x700+0+0')
root.title("Home Page")
root.resizable(False,False)

s="Student Management"
nameLabel=Label(root,text=s,font=('times new roman',24,'bold'),bg='white')
nameLabel.place(x=500,y=25)

connectButton=Button(root,text="Connect to database",font=('arial',10),bg='light blue',width=20,command=connect_database)
connectButton.place(x=1100,y=10)

leftFrame=Frame(root,bg='black')
leftFrame.place(x=50,y=80,width=300,height=600)

searchstudentButton=Button(leftFrame,text="Search Student info",font=('times new roman',14),width=20,bg='light blue',command=search_student)
searchstudentButton.grid(row=0,column=0,padx=40,pady=27)

addstudentButton=Button(leftFrame,text="Add Student info",font=('times new roman',14),width=20,bg='light blue',command=add_student)
addstudentButton.grid(row=1,column=0,padx=40,pady=27)


editstudentButton=Button(leftFrame,text="Edit Student info",font=('times new roman',14),width=20,bg='light blue',command=edit_student)
editstudentButton.grid(row=2,column=0,padx=40,pady=27)

deletestudentButton=Button(leftFrame,text="Delete Student info",font=('times new roman',14),width=20,bg='light blue',command=delete_student)
deletestudentButton.grid(row=3,column=0,padx=40,pady=27)

showstudentButton=Button(leftFrame,text="Display all students info",font=('times new roman',14),width=20,bg='light blue',command=show_student)
showstudentButton.grid(row=4,column=0,padx=40,pady=27)

exitButton=Button(leftFrame,text="Exit",font=('times new roman',14),width=20,bg='light blue',command=iexit)
exitButton.grid(row=5,column=0,padx=40,pady=27)

rightFrame=Frame(root)
rightFrame.place(x=400,y=80,width=820,height=600)

scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)

studentTable=ttk.Treeview(rightFrame,columns=('Roll No.','Name','Sem','Program','Department','Fee_Amount','Fee_Det','Exam_Result','SGPA')
                          ,xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)
scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

studentTable.heading('Roll No.',text='Roll No.')
studentTable.heading('Name',text='Name')
studentTable.heading('Sem',text='Sem')
studentTable.heading('Program',text='Program')
studentTable.heading('Department',text='Department')
studentTable.heading('Fee_Amount',text='Fee_Amount')
studentTable.heading('Fee_Det',text='Fee_Det')
studentTable.heading('Exam_Result',text='Exam_Result')
studentTable.heading('SGPA',text='SGPA')

style=ttk.Style()

style.configure('Treeview',rowheight=40,font=('times new roman',12))
style.configure('Treeview.Heading',font=('times new roman',14,'bold'))

studentTable.config(show='headings')

studentTable.pack(fill=BOTH,expand=1)

root.mainloop()


