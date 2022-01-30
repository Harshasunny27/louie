import pyttsx3 #we imported pyttsx3. (pyttsx3 - pyttsx3 is a text-to-speech conversion library in Python.)
import datetime#we are importing date and time from the computer
import speech_recognition as sr #it will recognize the speech from the user.
import wikipedia #for wikipedia reference after installing
import webbrowser
import os
import smtplib



engine = pyttsx3.init('sapi5') #Microsoft Speech API (SAPI5) is the technology for voice recognition
voices = engine.getProperty('voices') #defining the voices from microsoft
#print(voices[1].id) #we are checking the voices
engine.setProperty('voice',voices[0].id) #we selected the male voice



def speak(audio): #we created the function called speak. to perform the task.
    engine.say(audio) #engines will speak the audio string.
    engine.runAndWait() # just to wait



def wishMe(): #It is a function used to wish by speaking the time and date.
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour <18:
        speak("Good afternoon")
    else:
        speak("Good Evening")
    speak("I am Loui, please tell me how can I help you")



def takecommand():
    #it takes microphone input from the user and returns string output
    r = sr.Recognizer() # class to detect the audio
    with sr.Microphone() as source: # to detect the voice via microphone
        print("listening...")
        r.pause_threshold = 1 #click (for the gap between the words)
        audio = r.listen(source)

    try: #we will test the block of code for errors
        print("Recognizing....")
#Google has a great Speech Recognition API. This API converts spoken text (microphone) into written text (Python strings), briefly Speech to Text. You can simply speak in a microphone and Google API will translate this into written text.
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smptlib.SMTP('smtp.gmail.com', 587)
    server.elho()
    server.startls()
    server.login('kasiharsha10@gmail.com', 'your-password')
    server.sendmail('kasiharsha10@gmail.com', to, content)
    server.close()
if __name__ == '__main__':
    wishMe()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('searching in wikipedia..')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) #number for using the sentence
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open loginwebpage' in query:
            webbrowser.open("https://cas.nau.edu/cas/login?service=https%3A%2F%2Fwww.peoplesoft.nau.edu%2Fpsp%2Fps92pr%2F%3Fcmd%3Dstart.com")

        elif 'open blackboard' in query:
            webbrowser.open("https://bblearn.nau.edu/")

        elif 'open events' in query:
            webbrowser.open("https://events.nau.edu/")

        elif 'nau according to wikipedia' in query:
            results = wikipedia.summary(query, sentences=2)  # number for using the sentence
            speak("According to wikipedia")
            webbrowser.open()

        elif 'play music' in query:
            music_dir = 'C:\\Users\\hk452\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'disconnect' in query:
            speak("OKay Harsha, You can call me any time")
            speak("Just say wake up louie")
            break


        elif 'change my address' in query:
            speak("Please make sure all of your addresses are correct on LOUIE by using the drop-down box located in the Personal Information section of Student Center.")
        elif 'how do i submit payments' in query:
            speak("You may submit payments on LOUIE by clicking “Make a Payment” within the Finances section.  Additionally, you may look at other options for submitting payment.")
        elif 'add meal plan' in query:
            speak("To pay meal plan and Dining Dollar charges on your LOUIE account, see “How do I submit payments?”  Some dining accounts are not maintained on LOUIE and can be paid at the Dining Services Office on the first floor of the University Union or by phone at 928-523-2372.")
        elif 'apply for on campus jobs' in query:
            speak("you can apply for jobs on campus in handshake app, all the job applications, internships are avaliable there")
        elif 'add money to jack card' in query:
            speak("Please call 928-523-1905 or visit the JacksCard page.")
        elif 'drop my course' in query:
            speak("if you drop your course on time according to the deadline, We begin issuing tuition refunds after the second week of the Flagstaff campus regular term.")
        elif 'awarded financial aid' in query:
            speak("Students new to NAU are awarded financial aid in December for the following academic year. Continuing students are awarded beginning late May for the following academic year. We award continuing or returning students after they are evaluated for and meet satisfactory academic progress.")
        elif 'hr office' in query:
            speak("for any questions related hr please contact (928) 523-2223, and they are open all weekdays for 9-4 at 411 S Beaver St, Flagstaff, AZ 86011 ")
        elif 'transit office' in query:
            speak("for any questions related transit please contact (928) 523-6623, and they are open all weekdays for 9-4 at 411 S Beaver St, Flagstaff, AZ 86011")
        #elif '' in query:
            #speak("")


        #elif 'directions to' in query:



        elif 'the time' in query:
            strTime =  datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Harsha, the time is {strTime}")

        elif 'email to nandy' in query:
            try:
                speak ("what should i say?")
                content = takecommand()
                to = "sainandan83@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                Print(e)
                speak("I am unable to perform the task")








