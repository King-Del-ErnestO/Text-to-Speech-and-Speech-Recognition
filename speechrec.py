import speech_recognition as sr
import pyttsx3 as p

r = sr.Recognizer()
engine = p.init()

def music():
    print("I will now play music!")

engine.say("Hello, How are you doing?")
engine.runAndWait()
with sr.Microphone() as source:
    print("Hello, How are you doing?")
    text = r.listen(source)
    try:
        recognized_text = r.recognize_google(text)
        print(recognized_text)
    except sr.UnknownValueError:
        print('Unknown Value')
    except sr.RequestError as e:
        print('No Internet!')
    engine.say("what do you want me to do?")
    engine.runAndWait()

    text1 = r.listen(source)
    try:
        recognized_text1 = r.recognize_google(text1)
        print(recognized_text1)

        if recognized_text1 == "play music":
            music()

    except sr.UnknownValueError:
        print('Unknown Value')
    except sr.RequestError as e:
        print('No Internet!')

# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for 'Microphone(device_index={0})'".format(index, name))
