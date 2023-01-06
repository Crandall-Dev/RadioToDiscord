# Python program to translate
# speech to text and text to speech
 
 
import speech_recognition as sr
import pyttsx3
 
# Initialize the recognizer
recognizer = sr.Recognizer()
 

# Function to convert text to speech
def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
     
     
# Loop infinitely for user to speak
while(1):   
     
    # Exception handling to handle
    #  exceptions at the runtime
    try:
         
        # use the microphone as source for input.
        with sr.Microphone() as audioSourceMic:
             
            # Wait for a second to let the recognizer
            #  adjust the energy threshold based on
            #  the surrounding noise level
            recognizer.adjust_for_ambient_noise(audioSourceMic, duration=0.2)
             
            # Listens for the user's input
            audio2 = recognizer.listen(audioSourceMic)
             
            # Using google to recognize audio
            myText = recognizer.recognize_google(audio2)
            myText = myText.lower()
 
            print(f"Did you say: '{myText}'?")
            SpeakText(myText)
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")
