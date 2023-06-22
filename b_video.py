from tkinter import *

b_video=Tk()
b_video.geometry("770x450+250+100")
b_video.resizable(False,False)
b_video.configure(bg="#6096B4")
def c_bt():
    b_video.destroy()
    import homepage
bt1=Button(b_video,text="Back",command=c_bt,width=10,height=2)
bt1.place(x=0,y=0)

b_video.mainloop()