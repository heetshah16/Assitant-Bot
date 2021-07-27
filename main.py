import selenium.webdriver as wb
from selenium.webdriver.common.keys import Keys
import os
import time
import speech_recognition as sr
import playsound
from gtts import gTTS

count = 1


def search(text):
    driver = wb.Chrome()
    driver.get('https://www.google.com')
    input_elements = driver.find_element_by_css_selector('input[name=q]')
    input_elements.send_keys(text)
    input_elements.send_keys(Keys.ENTER)


def speak(text):
    global count
    tts = gTTS(text=text)
    p = "voice" + str(count) + ".mp3"
    filename = p
    tts.save(filename)
    playsound.playsound(filename)
    count += 1


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception" + str(e))
    return said


while True:
    speak("Do you wish to search the web?")
    time.sleep(3)
    x = input("Y/N")
    if x == 'N':
        speak("Thank you for your patience and see you soon!")
        exit()
    else:
        speak("What can I search for you and ?")
        get_audio()
        speak('Are you Satisfied with the answer?')
        y = input("Y/N")
        if y == "Y":
            break
        else:
            speak("could you please repeat the question")
            get_audio()
    continue