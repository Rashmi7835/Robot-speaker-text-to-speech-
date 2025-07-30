import pyttsx3

engine = pyttsx3.init('sapi5')

def speak(text):
    engine.say(text)
    engine.runAndWait()
    engine.stop()

if __name__ == "__main__":
    print("welcome to robo speaker 1.1, created by rashmi.....")
    while True:
        x= input("enter what you want me to say:")
        if x=="q":
            speak("good bye")
            break
        speak(x)
            
       