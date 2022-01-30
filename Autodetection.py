import os
import speech_recognition as sr


def takecommand():
    command = sr.Recogniser()
    with sr.Microphone() as source:
        print("Listening...")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing...")
            query = command.recognize_google(audio, language='en-in')
            print(f"you said : {query}")

        except:
            return "none"

            return query.lower()

        while True:

            wake_Up = takecommand()

            if 'wake_Up' in wake_Up:
                os.startfile('C:\\Users\\hk452\\PycharmProjects\\Louie\main.py')

            else:
                print("Nothing..")


