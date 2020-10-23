import speech_recognition as sr
import pyttsx3
import os
import datetime

# Initialize the recognizer
r = sr.Recognizer()
r.energy_threshold = 4000

engine = pyttsx3.init()
# Function to convert text to
# speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)

    engine.runAndWait()


# Loop infinitely for user to
# speak
hour = int(datetime.datetime.now().hour)
if hour >= 0 and hour < 12:
    engine.say("Good Morning")
    print("Good Morning")
elif hour >= 12 and hour < 18:
    engine.say("Good afternoon")
    print("Good afternoon")
else:
    engine.say("Good evening ")
    print("Good evening")

while (1):
    engine.say("What you want me to do")
    # Exception handling to handle
    # exceptions at the runtime
    try:

        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.1)

            # listens for the user's input
            audio2 = r.listen(source2)

            # Using ggogle to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            if MyText == "launch browser":
                engine.say("Ok Lets" + MyText)
                os.system("GoogleChrome")

            elif MyText == "launch media player":
                engine.say("Ok Lets" + MyText)
                os.system("VLC")
                # SpeakText("Ok Lets"+MyText)

            elif MyText == "launch me":
                engine.say("Ok Lets" + MyText)
                os.system("Figma")
                # SpeakText("Ok Lets"+MyText)

            elif MyText == "quit":
                SpeakText("Bye")
                exit()

            else:
                print("Did you say " + MyText)
                SpeakText(MyText)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")
