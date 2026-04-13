import speech_recognition as sr
import pyttsx3
import os
import pyautogui
import sounddevice as sd
import numpy as np

# Fast Voice Setup
engine = pyttsx3.init()
engine.setProperty('rate', 220) # Bohat fast awaaz

def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    # In settings se speed barh jati hai
    r.energy_threshold = 300
    r.dynamic_energy_threshold = False 
    
    fs = 44100
    duration = 2 # Recording time mazeed kam kar diya speed ke liye
    
    try:
        # Sounddevice recording bina delay ke
        rec = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
        sd.wait() 
        audio_data = sr.AudioData(rec.tobytes(), fs, 2)
        
        # Google recognition (Iske liye internet fast hona chahiye)
        query = r.recognize_google(audio_data, language='en-in')
        return query.lower()
    except:
        return ""

if __name__ == "__main__":
    speak("High speed mode active.")
    
    while True:
        query = listen()
        if not query: continue
        print(f"Detected: {query}")

        # Instant Commands
        if 'open' in query:
            app = query.replace("open", "").strip()
            pyautogui.press('win')
            pyautogui.typewrite(app, interval=0.01) # Fast typing
            pyautogui.press('enter')
            
        elif 'close' in query or 'exit' in query:
            pyautogui.hotkey('alt', 'f4')
            speak("Done")

        elif 'screenshot' in query:
            pyautogui.hotkey('win', 'prtscr')

        elif 'stop' in query:
            speak("Bye Farhan")
            break