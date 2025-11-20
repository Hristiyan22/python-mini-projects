import pyttsx3

def text_to_speech_func(text, lang = 'english'):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 40)
    engine.setProperty('voice', lang)
    engine.say(text)
    engine.runAndWait()

text_to_speech_func("Hello, there!")
