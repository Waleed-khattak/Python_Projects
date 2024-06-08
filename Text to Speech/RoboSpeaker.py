import pyttsx3

while(True):
    x = input("What do you want to Speak: ")
    speak = pyttsx3.init()
    voices = speak.getProperty('voices')
    speak.setProperty('voice', voices[1].id)
    speak.say(x)
    speak.runAndWait()
    if(x == "exit"):
        break
        
print("Executing finished....")