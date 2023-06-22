from tkinter import *
from GradiantFrame import GradientFrame
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# window size and texture
b_text=Tk()
b_text.geometry("770x450+250+100")
b_text.resizable(False,False)
b_text.configure(bg="#19A7CE")
b_text.title('Sentiment Analysis - Text')

gf = GradientFrame(b_text, colors = ("darkblue", "lightblue"), width = 800, height = 600)
gf.config(direction = gf.left2right)
gf.pack()

# LEFT SIDE DARK COLOR FRAME.
#frame1 = Frame(width=190,height=450,bg="#146C94")
#frame1.place(x=0,y=0)


# button to home page
def to_home():
    b_text.destroy()
    import homepage

# button to csv page
def to_csv():
    b_text.destroy()
    import b_csv

# button to audio page
def to_audio():
    b_text.destroy()
    import b_audio

# button to video page
def to_video():
    b_text.destroy()
    import b_video

# FUNCTION TO LOGIN PAGE.
def to_login():
    b_text.destroy()
    import login

# button which analyzes the text
def t_analysis():
    result_label.config(text="")
    text = t.get()
    scores = analyzer.polarity_scores(text)

    for key in scores :
        print(key)
        print(scores.get(key))

    if scores['compound'] >= 0.05:
        sentiment = 'Positive'
        emoji = '😊'
    elif scores['compound'] <= -0.05:
        sentiment = 'Negative'
        emoji = '😔'
    else:
        sentiment = 'Neutral'
        emoji = '😐'
    positive_words=[words for words in text.split() if analyzer.polarity_scores(words)['compound']>0]
    negative_words=[words for words in text.split() if analyzer.polarity_scores(words)['compound']<0]
    # Update the label with the sentiment analysis results
    result_label.config(text=f"Sentiment: {sentiment}{emoji}\n Positive % = {(scores.get('pos'))*100}% \n Positive words:{positive_words} \n Negative % = {(scores.get('neg'))*100}% \n  Negative words:{negative_words}" )



# TEXTUAL ANALYZER LABEL.
gf.create_text(400,40,text ="TEXTUAL ANALYZER",font=("",22,"bold"),fill="aqua")

# BUTTON FOR GOING TO HOME PAGE.
btn2 = Button(gf,text="Home",bg="#146C94",command=to_home ,font='Bold',width=7)
btn2.place(x=52,y=100)

# BUTTON FOR GOING TO CSV PAGE.
btn3 = Button(gf,text="CSV",bg="#146C94",command=to_csv ,font='Bold',width=7)
btn3.place(x=52,y=170)

# BUTTON FOR GOING TO AUDIO PAGE.
btn4 = Button(gf,text="Audio",bg="#146C94",command=to_audio ,font='Bold',width=7)
btn4.place(x=52,y=240)

# BUTTON FOR GOING TO VIDEO PAGE.
btn5 = Button(gf,text="Video",bg="#146C94",command=to_video ,font='Bold',width=7)
btn5.place(x=52,y=310)

# BUTTON FOR GOING TO LOGOUT PAGE.
btn6 = Button(b_text,text="Logout",bg="#146C94",font='Bold',width=7,command=to_login)
btn6.place(x=685,y=410)

# INSTRUCTION LABEL.
gf.create_text(380,120,text ="ENTER THE SENTENCE TO BE ANALYZED:",font=("",12,"bold"),fill="aqua")

t=Entry(font=("Microsoft Yahei UI Light", 11, "bold"), relief=SUNKEN,bg='lightgray', fg="black",borderwidth=3)
t.place(x=210,y=145, height=40, width=450)

# ANALYZE BUTTON.
button=Button(text="ANALYZE",bg='#146C94', font='3', fg="black",command=t_analysis,height=1)
button.place(x=210,y=208)

# RESULT SECTION.
result_label = Label(b_text, text="", font=("Microsoft Yahei UI Light", 13,"bold"), bg='lightgray', fg="black",width=41,highlightthickness=0,highlightcolor="#FFE5D8",borderwidth=3)
result_label.place(x=210, y=270, height=125, width=450)

b_text.mainloop()