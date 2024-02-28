# Install SpeechRecognition:
pip install SpeechRecognition
# Create a new Python file and import necessary libraries:
import speech_recognition as sr
import time
import os
# Define a function to recognize the user's voice:
def recognize_voice(recognizer, audio):
    try:
        user_name = recognizer.recognize_google(audio, language="en-in")
        return user_name.lower()
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
      # Define a function to recognize the user's command:
      def recognize_command(recognizer, audio):
    try:
        command = recognizer.recognize_google(audio, language="en-in")
        return command.lower()
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
      #   Create the main game loop:
      def main():
    recognizer = sr.Recognizer()

    # Record the user's voice for training
    print("Say your name...")
    with sr.Microphone() as mic:
        audio = recognizer.listen(mic)
        user_name = recognize_voice(recognizer, audio)

    if user_name is None:
        print("Could not recognize your name")
        sys.exit()

    print("Hello, " + user_name + ". You can now give commands.")

    # Record the user's command
    while True:
        with sr.Microphone() as mic:
            print("Say a command...")
            audio = recognizer.listen(mic)
            command = recognize_command(recognizer, audio)

        if command is None:
            print("Could not recognize your command")
            continue

        if command == "hello":
            if user_name == "a":
                print("Hello, " + user_name + "!")
                print("1")
            else:
                print(user_name + ", I'm sorry, I can only respond to user A's 'hello' command.")
                print("0")
        elif command == "take command":
            if user_name == "a":
                print("Okay, " + user_name + ", I'm taking your command.")
                print("1")
            else:
                print(user_name + ", I'm sorry, I can only take commands from user A.")
                print("0")
        elif command == "stop taking command":
            if user_name == "a":
                print("Okay, " + user_name + ", I'm no longer taking your command.")
                print("1")
            else:
                print(user_name + ", I'm sorry, I can only take commands from user A.")
                print("0")
        else:
            print("Sorry, I didn't understand your command")
            print("0")

if __name__ == "__main__":
    main()
