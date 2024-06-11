#pip install speechrecognition
#pip install wikipedia
#pip install pyttsx3
import speech_recognition as sr
import wikipedia
import pyttsx3
import webbrowser
import datetime
def telltime():
    current_time=datetime.datetime.now()
    print(current_time)

def takecommand():
    r=sr.Recognizer()
    try:
        with sr.Microphone() as source:#yaha microphone class audio lega
            audio=r.listen(source)#listen function source se audio lega aur audio var me store karega
            query=r.recognize_google(audio)#recognize_google funtcion audio  to text
            return query
    except sr.RequestError:
        print("please check ur internet connection")



def speak(audio):#is function me text to speech hua hai
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.say(audio)
    engine.runAndWait()
def hello():
#    speak("assalamu alaikum ammmaar khairiyyat")#yaha se hamne text pass kia hai
    speak("Hello I'm your virtual Assistance")#yaha se hamne text pass kia hai
#    speak('Hello there I am blaze')
def TakeQuery():
    hello()
    while True:
        query=takecommand().lower()
        if 'open google' in query:
            webbrowser.open("www.google.com")
        elif 'open java' in query:
            webbrowser.open("www.javatpoint.com")
        elif 'from wikipedia' in query:
            speak("Checking wikipedia")
            #star=input("Enter star name")
            query=query.replace("wikipedia","shahrukh khan")
            result=wikipedia.summary(query,sentences=4)
            speak("According to wikipedia")
            speak(result)
        elif 'tell me name' in query:
            speak("iam vikas your assistant")
        elif 'tell me time' in query:
            telltime()




if __name__ =="__main__":
    TakeQuery()