from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

def login():
    if usernameEntry.get()=="Admin" and passwordEntry.get()=="123456":
        messagebox.showinfo("Login Success","Welcome")
        window.destroy()
        import sms
        
    else :
        messagebox.showerror("Error","Please enter correct details")

window=Tk()

window.geometry('1280x700+0+0')
window.title("Login Page")
window.resizable(False,False)

loginFrame=Frame(window)
loginFrame.place(x=450,y=200)
logoImage=ImageTk.PhotoImage(file="ruas.jpg")

logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)

usernameLabel=Label(loginFrame,text="Username: ",font=("arial",20,"bold"))
usernameLabel.grid(row=1,column=0,pady=10,padx=20)
usernameEntry=Entry(loginFrame,font=("arial",20),bd=10)
usernameEntry.grid(row=1,column=1,pady=2,padx=5)

passwordLabel=Label(loginFrame,text="Password: ",font=("arial",20,"bold"))
passwordLabel.grid(row=2,column=0,pady=10,padx=20)
passwordEntry=Entry(loginFrame,font=("arial",20),bd=10)
passwordEntry.grid(row=2,column=1,pady=5,padx=5)

loginButton=Button(loginFrame,text="Login",font=("arial",14,"bold"),width=15,fg="white",bg="black",command=login)
loginButton.grid(row=3,column=0,columnspan=2,pady=10)
window.mainloop()
