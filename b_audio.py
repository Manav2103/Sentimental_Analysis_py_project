from tkinter import *
from tkinter import filedialog
import speech_recognition as sr
import speech_recognition as sr1
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from GradiantFrame import GradientFrame
analyzer = SentimentIntensityAnalyzer()

# window details
b_audio = Tk()
b_audio.geometry("770x450+250+100")
b_audio.resizable(False, False)
b_audio.configure(bg="#19A7CE")
b_audio.title('Sentiment Analysis - Audio')

# LEFT SIDE DARK COLOR FRAME.
#frame1 = Frame(width=190,height=450,bg="#146C94")
#frame1.place(x=0,y=0)

gf = GradientFrame(b_audio, colors = ("darkblue", "lightblue"), width = 800, height = 600)
gf.config(direction = gf.left2right)
gf.pack()


# FUNCTION TO RETURN TO HOME PAGE.
def to_home():
    b_audio.destroy()
    import homepage

# FUNCTION TO TEXT PAGE.
def to_text():
    b_audio.destroy()
    import b_text

# FUNCTION TO CSV PAGE.
def to_csv():
    b_audio.destroy()
    import b_csv

# FUNCTION TO VIDEO PAGE.
def to_video():
    b_audio.destroy()
    import b_video

# FUNCTION TO LOGIN PAGE.
def to_login():
    b_audio.destroy()
    import login


def convert_audio_to_text(file_path):
    # initialize the recognizer
    r = sr.Recognizer()

    # read the audio file
    with sr.AudioFile(file_path) as source:
    
        audio_text = r.record(source,offset=0,duration=180) # read the entire audio file

    # convert audio to text
    try:
        text = r.recognize_google(audio_text)
        text_output.config(state='normal') # enable text box for output
        text_output.delete(1.0, END) # clear previous output
        text_output.insert(END, text) # insert new output
        text_output.config(state='disable') # disable text box for output
    except sr.UnknownValueError: # voice recognition error
        text_output.config(state='normal')
        text_output.delete(1.0, END)
        text_output.insert(END, "Google Speech Recognition could not understand audio")
        text_output.config(state='disabled')
    except sr.RequestError as e: # network issues, server problems
        text_output.config(state='normal')
        text_output.delete(1.0, END)
        text_output.insert(END, "Could not request results from Google Speech Recognition service; {0}".format(e))
        text_output.config(state='disabled')


# function to handle file selection
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.wav;*.mp3;*.ogg")])
    if file_path:
        convert_audio_to_text(file_path)
def analyze():
    Text = text_output.get(1.0, END)
    scores = analyzer.polarity_scores(Text)
    if scores['compound'] >= 0.5:
        sentiment = 'Positive'
        emoji = '😊'
    elif scores['compound'] <= -0.5:
        sentiment = 'Negative'
        emoji = '😔'
    else:
        sentiment = 'Neutral'
        emoji = '😐'
    positive_words=[words for words in Text.split() if analyzer.polarity_scores(words)['compound']>0]
    negative_words=[words for words in Text.split() if analyzer.polarity_scores(words)['compound']<0]
    # Update the label with the sentiment analysis results
    result_label.config(text=f"Sentiment: {sentiment}{emoji}\nScores: {scores}\nPositivewords:{positive_words}\nNegativewords:{negative_words}")


def bt3speak():
    s = sr1.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Say something!")
        # Adjust for ambient noise levels
        s.adjust_for_ambient_noise(source)
        # Listen for speech and store it as an audio data object
        audio_data = s.listen(source)

    # Convert speech to text using Google's Speech Recognition API
    try:
        Text = s.recognize_google(audio_data)
        text_output.config(state='normal') # enable text box for output
        text_output.delete(1.0, END) # clear previous output
        text_output.insert(END, Text) # insert new output
        text_output.config(state='disable') # disable text box for output
        analyze(Text)
    except sr1.UnknownValueError:
        text_output.config(state='normal')
        text_output.delete(1.0, END)
        text_output.insert(END, "Google Speech Recognition could not understand audio")
        text_output.config(state='disabled')
    except sr1.RequestError as e:
        text_output.config(state='normal')
        text_output.delete(1.0, END)
        text_output.insert(END, "Could not request results from Google Speech Recognition service; {0}".format(e))
        text_output.config(state='disabled')
    




def analyze_sentiment():
    text = text_output.get(1.0, END)
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
    positive_words=[words for words in text.split() if analyzer.polarity_scores(words)['compound']>0]
    negative_words=[words for words in text.split() if analyzer.polarity_scores(words)['compound']<0]
    # Update the label with the sentiment analysis results
    # result_label.config(text=f"Sentiment: {sentiment}{emoji}\nScores: {scores}\nPositivewords:{positive_words}\nNegativewords:{negative_words}")
    # prints the positive and negative words percentage and also prints the positive and negative words
    result_label.config(text=f"Sentiment: {sentiment}{emoji}\n Positive % = {(scores.get('pos'))*100}% \n Positive words:{positive_words} \n Negative % = {(scores.get('neg'))*100}% \n  Negative words:{negative_words}" )



# AUDIO ANALYZER LABEL.
gf.create_text(400,35,text ="AUDIO ANALYZER",font=("",15,"bold"),fill = "aqua")

gf.create_text(410,80,text ="Enter An Audio file Or Record your speech",font=("",15,"bold"),fill = "aqua")
gf.create_text(410,170,text ="Text of Audio/speech will be displayed here",font=("",15,"bold"),fill = "aqua")

# INSTRUCTION LABEL.
#displabel=Label(text="Enter An Audio file Or Record your speech",bg="#19A7CE", font=("Microsoft Yahei UI Light", 12,"bold"))
#displabel.place(x=210,y=100)

# SELECT AUDIO FILE BUTTON.
select_button=Button(text="Select Audio File",bg='#146C94', font='3', fg="black",command=select_file,height=1)
select_button.place(x=210,y=110)

# MIC / SPEAKER BUTTON.
btn3=Button(text="Speak",bg='#146C94', font='3', fg="black",command=bt3speak,height=1)
btn3.place(x=400,y=110)

#simples
# textlabel = Label(text="Text of Audio/speech will be displayed here",bg="#19A7CE", font=("Microsoft Yahei UI Light", 12,"bold"))
# textlabel.place(x=210,y=190)

# TEXTBOX.
text_output = Text(state='disabled',height=4,width=60,bg="lightgrey")
text_output.place(x=210,y=185)

# ANALYZE BUTTON.
button=Button(text="ANALYZE",bg='#146C94', font='1', fg="black",command=analyze_sentiment)
button.place(x=210,y=258)

# RESULT SECTION.
result_label = Label(b_audio, text="", font=("Microsoft Yahei UI Light", 10,"bold"), bg="lightgrey", fg="black",width=53,height=5)
result_label.place(x=210, y=300)

# ********* NAVBAR ***********
# BUTTON FOR GOING TO HOME PAGE.
btn2 = Button(gf,text="Home",bg="#146C94", command=to_home,font='Bold',width=7)
btn2.place(x=52,y=100)

# BUTTON FOR GOING TO TEXT PAGE.
btn3 = Button(gf,text="Text",bg="#146C94", command=to_text,font='Bold',width=7)
btn3.place(x=52,y=170)

# BUTTON FOR GOING TO CSV PAGE.
btn4 = Button(gf,text="CSV",bg="#146C94", command=to_csv ,font='Bold',width=7)
btn4.place(x=52,y=240)

# BUTTON FOR GOING TO VIDEO PAGE.
btn5 = Button(gf,text="Video",bg="#146C94", command=to_video ,font='Bold',width=7)
btn5.place(x=52,y=310)

# BUTTON FOR GOING TO LOGOUT PAGE.
btn6 = Button(b_audio,text="Logout",bg="#146C94", command=to_login,font='Bold',width=7)
btn6.place(x=688,y=410)

b_audio.mainloop()