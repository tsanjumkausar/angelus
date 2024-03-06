import tkinter as tk
import speech_recognition as sr

# Function to recognize speech from microphone input
def recognize_speech_from_mic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please say something...")
        audio = r.listen(source)

    try:
        speech_text = r.recognize_google(audio)
        result_label.config(text="You said: " + speech_text)
    except sr.UnknownValueError:
        result_label.config(text="Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        result_label.config(text="Could not request results from Google Speech Recognition service; {0}".format(e))

# Create a Tkinter GUI
root = tk.Tk()
root.title("Speech Recognition Example")

# Create a label to display the recognized speech
result_label = tk.Label(root, text="")
result_label.pack()

# Create a button to trigger the speech recognition function
speech_button = tk.Button(root, text="Speak", command=recognize_speech_from_mic)
speech_button.pack()

# Start the Tkinter mainloop
root.mainloop()
