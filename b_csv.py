import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# import matplotlib
from tkinter import filedialog
from tkinter import *
from GradiantFrame import GradientFrame


# GUI.
b_csv=Tk()
b_csv.geometry("770x450+250+100")
b_csv.resizable(False,False)
b_csv.configure(bg="#19A7CE")
b_csv.title('Sentiment Analysis - CSV File')

# LEFT SIDE DARK COLOR FRAME.
# frame = Frame(width=190,height=450,bg="#146C94")
# frame.place(x=0,y=0)

gf = GradientFrame(b_csv, colors = ("darkblue", "lightblue"), width = 800, height = 600)
gf.config(direction = gf.left2right)
gf.pack()

# FUNCTION TO RETURN TO HOME PAGE.
def to_home():
    b_csv.destroy()
    import homepage

# FUNCTION TO TEXT PAGE.
def to_text():
    b_csv.destroy()
    import b_text

# FUNCTION TO AUDIO PAGE.
def to_audio():
    b_csv.destroy()
    import b_audio

# FUNCTION TO VIDEO PAGE.
def to_video():
    b_csv.destroy()
    import b_video

# FUNCTION TO LOGIN PAGE.
def to_login():
    b_csv.destroy()
    import login

# FUNCTION TO ANALYZE.
def analyze_sentiment(df):
    analyzer = SentimentIntensityAnalyzer()
    text=df.get(df.columns[0])
    scores = analyzer.polarity_scores(text)
    if scores['compound'] >= 0.05:
         sentiment = 'Positive'
         emoji = '😊'
    elif scores['compound'] <= -0.05:
         sentiment = 'Negative'
         emoji = '😔'
    else:
         sentiment = 'Neutral'
         emoji = '😐'
    #positive_words=[words for words in Text.split() if analyzer.polarity_scores(words)['compound']>0]
    #negative_words=[words for words in Text.split() if analyzer.polarity_scores(words)['compound']<0]
     #Update the label with the sentiment analysis results
    result_label.config(text=f"Sentiment: {sentiment}{emoji}\nScores: {scores}")
    #\nPositivewords:{positive_words}\nNegativewords:{negative_words}     removed part from the result wala label becoz it creates problem

# FUNCTION FOR UPLOAD BUTTON.
def upload_csv():
    file_path = filedialog.askopenfilename()
    if file_path.endswith('.csv'):
        df= pd.read_csv(file_path, encoding='ISO-8859-1')
        # csv_data = df.values
        
        #for value in csv_data:

        analyze_sentiment(df)




# CSV ANALYZER LABEL.
gf.create_text(400,40,text ="CSV ANALYZER",font=("",22,"bold"),fill="aqua")

# INSTRUCTION LABEL.
gf.create_text(390,120,text ="UPLOAD THE CSV FILE TO ANALYZE:",font=("",15,"bold"),fill="aqua")

# UPLOAD CSV FILE BUTTON.
select_button=Button(text="Upload CSV File",bg='#146C94', font='3', fg="black",command=upload_csv,height=1)
select_button.place(x=210,y=150)

# RESULT SECTION.
result_label = Label(b_csv, text="", font=("Microsoft Yahei UI Light", 13,"bold"), bg="lightgrey", fg="black",width=48,height=5)
result_label.place(x=210, y=200)

# ********* NAVBAR ***********
# BUTTON FOR GOING TO HOME PAGE.
btn2 = Button(gf,text="Home",bg="#146C94", command=to_home,font='Bold',width=7)
btn2.place(x=52,y=100)

# BUTTON FOR GOING TO TEXT PAGE.
btn3 = Button(gf,text="Text",bg="#146C94", command=to_text,font='Bold',width=7)
btn3.place(x=52,y=170)

# BUTTON FOR GOING TO AUDIO PAGE.
btn4 = Button(gf,text="Audio",bg="#146C94", command=to_audio ,font='Bold',width=7)
btn4.place(x=52,y=240)

# BUTTON FOR GOING TO VIDEO PAGE.
btn5 = Button(gf,text="Video",bg="#146C94", command=to_video ,font='Bold',width=7)
btn5.place(x=52,y=310)

# BUTTON FOR GOING TO LOGOUT PAGE.
btn6 = Button(gf,text="Logout",bg="#146C94", command=to_login,font='Bold',width=7)
btn6.place(x=688,y=410)
# ********* NAVBAR ENDS *********.

b_csv.mainloop()