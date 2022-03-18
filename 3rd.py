import pyttsx3

import pywhatkit as kit

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def boliyesir(audio):
    engine.say(audio)
    engine.runAndWait()

boliyesir("Type y for a youtube search and s for a website search")
x=input("Type y for a youtube search and s for a website search\n")
if (x=='y'):
    boliyesir("Input anything you want to search on Youtube")
    a=input('Input anything you want to search on youtube \n')
    print("We will repeat what you have typed for your confirmation. Type yes if we are correctly saying what you said\n")
    boliyesir("We will repeat what you have typed for your confirmation. Type yes if we are correctly saying what you said\n")
    boliyesir(a)
    n=input()
    if n=='yes':
        kit.playonyt(a)
    else:
        pass
if(x=='s'):
    boliyesir("Input anything you want to search on google")
    b=input('Input anything you want to search on google \n')
    print("We will repeat what you have typed for your confirmation. Type yes if we are correctly saying what you said\n")
    boliyesir("We will repeat what you have typed for your confirmation. Type yes if we are correctly saying what you said\n")
    boliyesir(b)
    n=input()
    if n=='yes':
        kit.search(b)
    else:
        pass
