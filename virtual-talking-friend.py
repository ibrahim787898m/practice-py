import pyttsx3

while True:
    friend = pyttsx3.init()
    speech = input("Say Something: ")
    friend.say(speech)
    friend.runAndWait()
