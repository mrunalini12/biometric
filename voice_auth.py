import speechrecognition as sr

def authenticate_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please say something for authentication")
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
        # Authentication logic: check if the recognized text matches the predefined phrase
        if text.lower() == "open sesame":
            return True
        else:
            return False
    except sr.UnknownValueError:
        print("Could not understand the audio")
        return False
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return False

if __name__ == "__main__":
    if authenticate_voice():
        exit(0)
    else:
        exit(1)
