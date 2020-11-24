from tkinter import *
import os

def delete1():
    screenLS.destroy()
    
def delete2():
    screenLf.destroy()
    
def delete3():
    screenLu.destroy()

def login_success():
    global screenLS
    screenLS=Toplevel(screenL)
    screenLS.title("Success")
    screenLS.geometry("200x100")
    Label(screenLS, text="Login Success",fg="green",font="calibri").pack()
    Button(screenLS,text="OK",command=delete1).pack(pady=10)

def login_failed():
    global screenLf
    screenLf=Toplevel(screenL)
    screenLf.title("Invalid")
    screenLf.geometry("200x100")
    Label(screenLf, text="Login Failed",fg="red",font="calibri").pack()
    Button(screenLf,text="OK",command=delete2).pack(pady=10)

def user_not_found():
    global screenLu
    screenLu=Toplevel(screenL)
    screenLu.title("Invalid")
    screenLu.geometry("200x100")
    Label(screenLu, text="User not found",fg="red",font="calibri").pack()
    Button(screenLu,text="OK",command=delete3).pack(pady=10)

def new_user():
    username_info= username.get()
    password_info= password.get()

    file=open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    u_entry.delete(0,END)
    p_entry.delete(0,END)

    Label(screenR, text="Registration success", fg="green", font="calibri").pack()

def login_user():
    username_info= username1.get()
    password_info= password1.get()

    list_of_files=os.listdir()
    if username_info in list_of_files:
        file1=open(username_info,"r")
        verify=file1.read().splitlines()
        if password_info in verify:
            login_success()
        else:
            login_failed()
    else:
        user_not_found()


    u_verify.delete(0,END)
    p_verify.delete(0,END)

def Register():
    global screenR
    screenR=Toplevel(screen)
    screenR.title("Register")
    screenR.geometry("500x400")
    global username
    global password
    global u_entry
    global p_entry

    username = StringVar()
    password = StringVar()

    Label(screenR, text="REGISTRATION", bg="grey", font=("calibri",13),width="150",height="3").pack()
    Label(screenR, text="").pack()
    Label(screenR, text="Username*").pack()
    u_entry = Entry(screenR, textvariable=username)
    u_entry.pack(pady=10)
    Label(screenR, text="Password*").pack()
    p_entry = Entry(screenR, textvariable=password)
    p_entry.pack(pady=10)
    Button(screenR,text="Register",command=new_user,width="50",height="2").pack(pady=10)
    return(u_entry,p_entry)


def Login():
    global screenL
    screenL=Toplevel(screen)
    screenL.title("Login")
    screenL.geometry("500x400")
    global username1
    global password1
    global u_verify
    global p_verify

    username1 = StringVar()
    password1 = StringVar()

    Label(screenL, text="LOGIN", bg="grey", font=("calibri",13),width="150",height="3").pack()
    Label(screenL, text="").pack()
    Label(screenL, text="Username*").pack()
    u_verify = Entry(screenL, textvariable=username1)
    u_verify.pack(pady=10)
    Label(screenL, text="Password*").pack()
    p_verify = Entry(screenL, textvariable=password1)
    p_verify.pack(pady=10)
    Button(screenL,text="LOGIN",command=login_user,width="50",height="2").pack(pady=10)
    return(u_verify,p_verify)




def main_screen():
    global screen
    screen=Tk()
    screen.title("FORM")
    screen.geometry("500x400")
    Label(text="FORM", bg="grey", font=("calibri",13),width="150",height="3").pack()
    Label(screen, text="").pack()
    Button(text="Login",command=Login,width="50",height="2").pack(pady=10)
    Button(text="Register",command=Register,width="50",height="2").pack(pady=10)

    screen.mainloop()

main_screen()
