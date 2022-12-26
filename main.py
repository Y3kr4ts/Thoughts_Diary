# https://pyttsx3.readthedocs.io/en/latest/engine.html#examples
import pyttsx3


def talk(message):
    """ Talk function:
            setting the voice ID and RATE property's.
            returning the message string provided to TTS.
    """
    tts_engine = pyttsx3.init()
    voice = tts_engine.getProperty('voices')
    tts_engine.setProperty('voice', voice[1].id)
    # tts_engine.setProperty('rate', 139)
    tts_engine.say(message)
    tts_engine.runAndWait()


if __name__ == "__main__":
    talk(message="Hello Mike.. Nice to speak to you again, Would you like to make a Journal entry?")
    user_input = input("Please Type Yes or No")
    user_input = user_input.strip().lower()

    match user_input:

        case "yes":
            talk("Awesome! What's today's date?")
            date = input("Enter today's date :] ")

            talk("Great! How do you rate your mood today? Be honest.")
            mood = input("How do you rate your mood today be honest :] ")

            talk("Ok perfect, Now the best part! find the feelings deep inside, Let your thoughts flow Mike. ")
            thoughts = input("Let your thoughts flow:\n ")

            talk("Thank you for sharing your thoughts with me. have a amazing day. Feel the love Mike!")

            with open(f"{date}.txt", "w") as file:
                file.write("[Mood]: " + mood + 2 * "\n")
                file.write(thoughts)
                talk("I have saved the file in the directory of this program.")

        case "no":
            talk("I hope everything is ok Mike? I'm always here if you want to talk. Have the most amazing day.")

