# install the SpeechRecognition library :
# import speech_recognition as sr
import time

# Initialize the recognizer class (for recognizing the speech)
r = sr.Recognizer()

def listen():
    """
    Listens for speech and returns the text as a string.
    """
    with sr.Microphone() as source:
        print("Listening... ")
        audio = r.listen(source)
        try:
            print("Recognizing... ")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
        return query.lower()

def game():
    """
    The game function contains the game logic.
    """
    print("Welcome to the speech recognition game!")
    time.sleep(1)
    print("I'm thinking of a number between 1 and 10.")
    time.sleep(2)
    answer = 7  # The correct answer

    # Get the user's guess
    while True:
        query = listen()
        if 'quit' in query or 'exit' in query:
            print("Thanks for playing!")
            break
        if query.isdigit() and int(query) in range(1, 11):
            if int(query) == answer:
                print("Congratulations! You guessed the number!")
                break
            else:
                print("Sorry, that's not correct. Try again.")
        else:
            print("Please enter a number between 1 and 10.")

if __name__ == "__main__":
    game()
