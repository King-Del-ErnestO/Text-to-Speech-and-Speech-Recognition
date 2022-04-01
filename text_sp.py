import pyttsx3 as p

engine = p.init()
voices = engine.getProperty("voices")
# print(voices)
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 190)

engine.say("Hello, how are you doing?")
engine.say("What would you like me to do?")
engine.runAndWait()