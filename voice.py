from turtle import st
import speech_recognition as s_r
from selenium import webdriver
import pyttsx3
import pywhatkit as kit
import time
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
def boliyesir(audio):
    engine.say(audio)
    engine.runAndWait()
print(s_r.__version__) # just to print the version not required
r = s_r.Recognizer()
my_mic = s_r.Microphone(device_index=1) #my device index is 1, you have to put your device index
while True:
    with my_mic as source:
        print("Say now!!!!")
        boliyesir("Bol na madarchod")
        time.sleep(1)
        r.adjust_for_ambient_noise(source) #reduce noise
        audio = r.listen(source) #take voice input from the microphone
    stot = r.recognize_google(audio)
    if stot=="stop":
        break
    boliyesir(stot)
    time.sleep(1)
    print(stot)
    with my_mic as source:
        boliyesir("Sahi hai ki nai")
        time.sleep(1)
        r.adjust_for_ambient_noise(source) #reduce noise
        audio = r.listen(source)
    stoty = r.recognize_google(audio)
    if stoty=="Yes" or stoty=="yes":
        kit.search(stot)
    else:
        continue

     #to print voice into text