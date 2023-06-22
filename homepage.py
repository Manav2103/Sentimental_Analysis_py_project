from tkinter import *
from GradiantFrame import GradientFrame
#from PIL import Image, ImageTk


# GUI.
homePage=Tk()
homePage.geometry("770x450+250+100")
homePage.resizable(False,False)
homePage.configure(bg="#6096B4")
homePage.title('Sentiment Analysis')

gf = GradientFrame(homePage, colors = ("darkblue", "lightblue"), width = 800, height = 600)
gf.config(direction = gf.left2right)
gf.pack()

# UPPER FRAME. 
# frame=Frame(homePage,bg="#146C94",width=770,height=60).place(x=0,y=0)

#left frame
# frame2 = Frame(homePage,bg="#146C94",width=150,height=450)
# frame2.place(x=0)

# FUNCTION TO TEXT PAGE.
def to_text():
    homePage.destroy()
    import b_text

# FUNCTION TO CSV PAGE.
def to_csv():
    homePage.destroy()
    import b_csv

# FUNCTION TO AUDIO PAGE.
def to_audio():
    homePage.destroy()
    import b_audio

# FUNCTION TO VIDEO PAGE.
def to_video():
    homePage.destroy()
    import b_video


def to_login():
    homePage.destroy()
    import login

# PHOTO.
imag=PhotoImage(file='Images/words.png')
imagelabel=Label(image=imag).place(x=2,y=200)

# SENTIMENT ANALYSIS TEXT.

gf.create_text(380,40,text ="SENTIMENTAL ANALYSIS",font=("",22,"bold"),fill="aqua")

#selection of the method through which analyze has to be done
gf.create_text(380,90,text ="CLICK THE BUTTON THROUGH WHICH YOU WANT TO ANALYZE REVIEWS/SENTIMENTS ",font=("",12,"bold"),fill="aqua")

# BUTTON FOR GOING TO HOME PAGE.
btn2 = Button(gf,text="Text",bg="#146C94",command=to_text ,font='Bold',width=8,height=1)
btn2.place(x=90,y=120)

# BUTTON FOR GOING TO CSV PAGE.
btn3 = Button(gf,text="CSV",bg="#146C94",command=to_csv ,font='Bold',width=8)
btn3.place(x=240,y=120)

# BUTTON FOR GOING TO AUDIO PAGE.
btn4 = Button(gf,text="Audio",bg="#146C94",command=to_audio ,font='Bold',width=8)
btn4.place(x=390,y=120)

# BUTTON FOR GOING TO VIDEO PAGE.
btn5 = Button(gf,text="Video",bg="#146C94",command=to_video ,font='Bold',width=8)
btn5.place(x=540,y=120)

# BUTTON FOR GOING TO LOGOUT PAGE.
btn6 = Button(homePage,text="Logout",bg="#146C94",command=to_login,font='Bold',width=6)
btn6.place(x=2,y=2)

homePage.mainloop()