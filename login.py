from pymongo import MongoClient
from tkinter import *
from tkinter import messagebox
import bcrypt
import re


# MONGODB CONNECTION.
client = MongoClient('mongodb+srv://yashdave307:yashdave307@cluster0.qd3g00c.mongodb.net/test');
print("Connection Successful")
# print(client)
db = client['sentimental_analysis']
collection = db['users']



# FUNCTION TO LOGIN.
def log() :
    details = collection.find_one({'email' : emailEntry.get()})
    print(details)
  
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if emailEntry.get() == '' or passEntry.get()=='' :
        messagebox.showerror('Invalid', 'Please fill all the fields.')
    elif re.fullmatch(pattern, emailEntry.get()) is None:
        messagebox.showerror('Invalid','Email is not valid')
    elif details == None :
        messagebox.showerror('Invalid','Email id not registered, Please Signup.')


    # password entered by user while login.
    password = passEntry.get()

    # Database password.
    DBpassword = details['password']

    # encoding user password
    userBytes = password.encode('utf-8')

    # checking password
    result = bcrypt.checkpw(userBytes, DBpassword)
    print(result)

    if result == True :
        login.destroy()
        import homepage    
    else :
        messagebox.showerror('Invalid','Incorrect Password.')


# FUNCTION TO GO TO SIGNUP.
def gosign():
    login.destroy()
    import signup



# GUI
login = Tk()
login.title("Login")
login.geometry("800x450+250+100")
# login.minsize(790, 512)
login.resizable(False, False)
login.configure(bg="#fff")
login.title('Sentiment Analysis - Login')

# IMAGE.
photo=PhotoImage(file=r"Images/sentiment-image.png")
l0=Label(login,image=photo)
l0.place(x=0,y=0,width=450,height=450)

# SENTIMENT ANALYSIS HEADING.
head = Label(login, text="Sentiment Analysis", fg="#57a1f8", bg="white", font=("Microsoft Yahei UI Light", 23, "bold"))
head.place(x=70, y=20)

# Login heading.
heading = Label(login, text="Login", fg="#57a1f8", bg="white", font=("Microsoft Yahei UI Light", 23, "bold"))
heading.place(x=560, y=110)

# Email field.
l1=Label(login,text="Email:",bg="white",font=("black",10,"bold")).place(x=480,y=185)
emailEntry = Entry(login, width=20, fg="black", border=2, bg="white", font=("Microsoft Yahei UI Light", 11, "bold"))
emailEntry.place(x=560, y=185)

# Password field.
l2=Label(login,text="Password:",bg="white",font=("black",10,"bold")).place(x=480,y=225)
passEntry = Entry(login, width=20, show="*", fg="black", border=2, bg="white", font=("Microsoft Yahei UI Light", 11, "bold"))
passEntry.place(x=560, y=225)


# Login Button.
b=Button(login,width=8,pady=3,font='Bold' ,text='Login',bg="#57a1f8", fg="white",command=log).place(x=600,y=260)

# Signup Button.
lx=Label(login,text="Don't have an account?",fg="black",bg="white",font=("Microsoft Yahei UI Light", 10))
lx.place(x=500,y=330)
signUp=Button(login,width=8,text="Sign Up",bd=2,bg="#57a1f8",cursor="hand2",fg="white",command=gosign).place(x=660,y=330)

login.mainloop()