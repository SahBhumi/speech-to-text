import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r= sr.Recognizer()

def record_text():
    while(1):
        try:
            # Use microphone as a source for input
            with sr.Microphone() as source:
                # Prepare the reconizer to receive the input
                r.adjust_for_ambient_noise(source,duration=0.2)
                
                audio= r.listen(source)
                
                Mytext= r.recognize_google(audio)
                return Mytext
            
        except sr.RequestError as e:
            print("Could not request result; {0}".format(e))
            
        except sr.UnknownValueError:
            print("Unknown error occurred")
    
    return

def output_text(text):
    f= open("output.txt","a")
    f.write(text)
    f.write("\n")
    f.close()
    return

while(1):
    text = record_text()
    output_text(text)
    
    print("The text is printed successfully")
