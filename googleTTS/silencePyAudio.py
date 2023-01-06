import os

from pyaudio import PyAudio
 
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


class pyaudio:
    """
    PyAudio is noisy af every time you initialise it, which makes reading the
    log output rather difficult.  The output appears to be being made by the
    C internals, so I can't even redirect the logs with Python's logging
    facility.  Therefore the nuclear option was selected: swallow all stderr
    and stdout for the duration of PyAudio's use.

    Lifted and adapted from StackOverflow:
      https://stackoverflow.com/questions/11130156/
    """

    def __init__(self):

        # Open a pair of null files
        self.null_fds = [os.open(os.devnull, os.O_RDWR) for x in range(2)]

        # Save the actual stdout (1) and stderr (2) file descriptors.
        self.save_fds = [os.dup(1), os.dup(2)]

        self.pyaudio = None

    def __enter__(self) -> PyAudio:

        # Assign the null pointers to stdout and stderr.
        os.dup2(self.null_fds[0], 1)
        os.dup2(self.null_fds[1], 2)

        self.pyaudio = PyAudio()

        return self.pyaudio

    def __exit__(self, *_):

        self.pyaudio.terminate()

        # Re-assign the real stdout/stderr back to (1) and (2)
        os.dup2(self.save_fds[0], 1)
        os.dup2(self.save_fds[1], 2)

        # Close all file descriptors
        for fd in self.null_fds + self.save_fds:
            os.close(fd)

# *************************************************************************




# Loop infinitely for user to speak
while(1):   
     
# Exception handling to handle
#  exceptions at the runtime
    try:
         
    # use the microphone as source for input.
        myText = ""
        with pyaudio() as audio:
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
        myText = ""
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")


