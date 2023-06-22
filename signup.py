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


# FUNCTION TO GO TO LOGIN PAGE.
def log() :
    signup.destroy()
    import login


regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
# FUNCTION ON CLICK SIGNUP.
def signup1() :
    details = collection.find_one({'email' : emailEntry.get()})
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if emailEntry.get() == '' or passEntry.get()=='' or  cpassEntry.get()=='' :
        messagebox.showerror('Invalid', 'Please fill all the fields.')
    elif re.fullmatch(pattern, emailEntry.get()) is None:
        messagebox.showerror('Invalid', 'Email is not valid.')
    elif  passEntry.get() != cpassEntry.get() :
        messagebox.showerror('Invalid', 'Passwords do not match.')
    elif details != None :
        messagebox.showerror('Invalid', 'User already exist, Please Login.')
    else :
        messagebox.showinfo('Signup','Successfully signed up')
        password = passEntry.get()

        # converting password to array of bytes
        bytes = password.encode('utf-8')

        # generating the salt
        salt = bcrypt.gensalt()

        # hashing the password.
        hashedPassword = bcrypt.hashpw(bytes, salt)
        insert = {'email': emailEntry.get(), 'password': hashedPassword}
        print(insert)
        collection.insert_one(insert)

    emailEntry.delete(0,END)
    passEntry.delete(0,END)
    cpassEntry.delete(0,END)


# GUI.
signup = Tk()
signup.title("signup")
signup.geometry("800x450+250+100")
signup.resizable(False, False)
signup.configure(bg="#fff")
signup.title('Sentiment Analysis - Signup')

# IMAGE.
photo=PhotoImage(file=r"Images/sentiment-image.png")
l0=Label(signup,image=photo)
l0.place(x=0,y=0,width=450,height=450)

# SENTIMENT ANALYSIS HEADING.
head = Label(signup, text="Sentiment Analysis", fg="#57a1f8", bg="white", font=("Microsoft Yahei UI Light", 23, "bold"))
head.place(x=70, y=20)


# SIGNUP HEADING.
heading = Label(signup, text="Sign up", fg="#57a1f8", bg="white", font=("Microsoft Yahei UI Light", 23, "bold"))
heading.place(x=550, y=70)

# EMAIL FIELD.
l1=Label(signup,text="Email:",bg="white",font=("black",10,"bold")).place(x=480,y=150)
emailEntry = Entry(signup, width=20, fg="black", border=2, bg="white", font=("Microsoft Yahei UI Light", 11, "bold"))
emailEntry.place(x=560, y=145)

# PASSWORD FIELD.
l2=Label(signup,text="Password:",bg="white",font=("black",10,"bold")).place(x=480,y=190)
passEntry = Entry(signup, width=20, show="*", fg="black", border=2, bg="white", font=("Microsoft Yahei UI Light", 11, "bold"))
passEntry.place(x=560, y=185)


# CONFIRM PASSWORD FIELD.
l3=Label(signup,text="Confirm :\n Password",bg="white",font=("black",10,"bold")).place(x=480,y=225)
cpassEntry = Entry(signup, width=20, show="*", fg="black", border=2, bg="white", font=("Microsoft Yahei UI Light", 11, "bold"))
cpassEntry.place(x=560, y=225)


# SIGNUP BUTTON.
b=Button(signup,width=8,pady=3,font='Bold' ,text='Sign Up',bg="#57a1f8", fg="white",command=signup1).place(x=600,y=260)

# lOGIN BUTTON.
lx=Label(signup,text="Already have an account?",fg="black",bg="white",font=("Microsoft Yahei UI Light", 10))
lx.place(x=500,y=330)
login=Button(signup,width=8,text="Login",bd=2,bg="#57a1f8",cursor="hand2",fg="white",command=log).place(x=660,y=330)
signup.mainloop()





