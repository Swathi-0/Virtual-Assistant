import pyttsx3
import datetime
from playsound import playsound
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)    
    if hour>=0 and hour<=12:
        speak("Good Morning!!")
        print("Good Morning!!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!!")
        print("Good Afternoon!!")

    else:
        speak("Good Evening!!")
        print("Good Evening!!")

    speak("I am Maya, Please tell me how can i help you.")
    print("I am Maya, Please tell me how can i help you.")    
                 
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.79
        r.energy_threshold = 500
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n") 

    except Exception as e:
        # print(e)    
        print("Say that again please...")    
        return "None" 
    return query   

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('eng21ct0018@dsu.edu.in', 'Lavanya@123')
    server.sendmail('eng21ct0018@dsu.edu.in', to, content)
    server.close()

def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
				5: 'Friday', 6: 'Saturday',
				7: 'Sunday'}
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)   
        print("The day is " + day_of_the_week)        

def Whatsapp():
    speak("Tell me the name of the person!")
    print("Tell me the name of the person!")
    name = takeCommand()

    if 'deepa' in name:
        speak("Tell me the message!")
        print("Tell me the message!")
        msg= takeCommand()
        speak("Tell me the time ")
        print("Tell me the time")
        hour = int(takeCommand())
        speak("Time in minutes")
        print("Time in minutes")
        min = int(takeCommand())
        pywhatkit.sendwhatmsg("+919916548600", msg, hour, min,20)
        speak("ok,sending the whatsapp message")
        print("ok,sending the whatsapp message")

    elif 'disha' in name:
        speak("Tell me the message!")
        print("Tell me the message!")
        msg= takeCommand()
        speak("Tell me the time")
        print("Tell me the time")
        hour = int(takeCommand())
        speak("Time in minutes")
        print("Time in minutes")
        min = int(takeCommand())
        pywhatkit.sendwhatmsg("+917349509443", msg,hour,min,10)
        speak("ok,sending the whatsapp message") 
        print("ok,sending the whatsapp message")  

    elif 'ramkumar' in name:
        speak("Tell me the message!")
        print("Tell me the message!")
        msg= takeCommand()
        speak("Tell me the time")
        print("Tell me the time")
       
        pywhatkit.sendwhatmsg("+919845186938", msg,hour,min,10)
        speak("ok,sending the whatsapp message")
        print("ok,sending the whatsapp message")   

    else:
        speak("Tell me the phone number")
        print("Tell me the phone number")
        phone = input("Ph number: ")
        ph = '+91'+ phone 
        speak("Tell me the message!")
        print("Tell me the message!")
        msg= takeCommand()
        speak("Tell me the time")
        print("Tell me the time")
        hour = int(input("Time in hour: "))
        speak("Time in minutes")
        print("Time in minutes")
        min = int(input("time in minute:"))
        pywhatkit.sendwhatmsg(ph,msg,hour,min,10)
        speak("ok,sending the whatsapp message")
        print("ok,sending the whatsapp message") 


def Whats():
    speak("Tell me the group name")
    print("Tell me the group name")
    p= input("Group Name: ")
    speak("Tell me the message!")
    print("Tell me the message!")
    msg= takeCommand()
    speak("Tell me the time")
    print("Tell me the time")
    hour = int(input("Time in hour: "))
    speak("Time in minutes")
    print("Time in minutes")
    min = int(input("time in minute:"))        
    pywhatkit.sendwhatmsg_to_group(p,msg,hour,min,2)
    speak("ok,sending the whatsapp message")
    print("ok,sending the whatsapp message") 

if _name=="main_" :
    wishme()
    while True:
        query = takeCommand().lower() 
        if 'wikipedia' in query:  
            speak('Searching Wikipedia...')
            print('Searching Wikipedia...')
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print("According to Wikipedia")
            print(results)
            speak(results)


        elif 'youtube search' in query:
            speak("Ok, this is what i found for your search!")
            print("Ok, this is what i found for your search!")
            query = query.replace("Maya", " ")
            query = query.replace("youtube search", " ")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            speak("Done!!")
            print("Done!!")


        elif 'google search' in query:
            speak("Ok, this is what i found for your search!")
            print("Ok, this is what i found for your search!")
            query = query.replace("Maya", " ")
            query = query.replace("google search", " ")
            pywhatkit.search(query)
            speak("Done!!")
            print("Done!!")
        
        elif 'website' in query:
            speak("ok, Launching...")
            print("ok, Launching...")
            query = query.replace("Maya"," ")
            query = query.replace("Website"," ")
            query = query.replace(" ","")
            web1 = query.replace("open"," ")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            speak("Launches!!")
            print("Launches!!")

        elif 'open google' in query:
            webbrowser.open('www.google.com')

        
        elif 'open code' in query:
            codePath = "C:\\Users\\Lavanya\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(codePath) 

        elif 'open whatsapp' in query:
            codePath = "C:\\Users\\Lavanya\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\WhatsApp\\WhatsApp.lnk"
            os.startfile(codePath)             
        
        
        
        elif 'open canva' in query:
            codePath = "C:\\Users\\Lavanya\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Canva.lnk"
            os.startfile(codePath)       


        elif 'play music' in query:
            music_dir = 'C:\\Users\\Lavanya\\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))      

        
        elif 'date' in query:
            date = datetime.datetime.now().strftime('%d %m %Y') 
            speak("Today's date is " + date)
            print("Today's date is " + date)
            

        elif 'whatsapp message' in query:
            Whatsapp()

        elif 'group message' in query:
            Whats()  

        
        elif 'how are you' in query:
            speak("I am fine, how about you")
            print("I am fine, how about you")

        elif 'what is your name' in query:
            speak("I am Maya, What can I do for you?")
            print("I am Maya, What can I do for you?")

        elif 'who is' in query:
            human = query.replace('Who is', ' ')
            info = wikipedia.summary(human,1)
            print(info)
            speak(info) 

        elif 'joke' in query:
            Jokee=pyjokes.get_joke()
            print(Jokee)
            speak(Jokee)    

        elif "play" in query:
            song = query.replace('play'," ")
            speak("playing" + song)
            print("playing" + song)
            pywhatkit.playonyt(song)            

        elif 'send email' in query:
            try:
                speak("What should I say?")
                print("What should I say?")
                content = takeCommand()
                to = "dishlavu@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
                print("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry ,I am not able to send this email")
                print("Sorry, I am not able to send this email")
        elif 'day' in query:
            tellDay() 
        
        elif 'goodbye' in query:
            print('Bye. I hope you have a Great Day!!')
            speak("Bye. I hope you have a Great Day!!")
            exit()
                                      
        elif 'repeat my words' in query:
            speak("Yes Definitely!!")
            print("Yes Definitely!!")
            jj = takeCommand()  
            speak(f'You said: {jj}')     
            print(f'You said: {jj}')            
        
        elif 'my location' in query:
            speak('ok,wait a second')
            print('ok,wait a second')
            webbrowser.open("https://www.google.com/maps/@12.95396,77.4908521,11z")    

        elif 'alarm' in query:
            speak("Enter the Time :")
            time = input(": Enter the Time :")

            while True:
                t = datetime.datetime.now()
                now = t.strftime("%H:%M:%S")

                if now == time:
                    speak("Time to wake up sir!!")
                    print("Time to wake up sir!!")
                    playsound("C:\\Users\\Lavanya\\Downloads\\alarm.mp3")
                    speak("Alarm Closed!")
                    print("Alarm Closed!")

                elif  now>time:
                    break

        elif 'news' in query:
            news = webbrowser.open_new_tab ("https://timesofindia.indiatimes.com/india")
            speak('Here are some headlines from the Times of India,Happy reading')
            print('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)