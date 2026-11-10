
import random
from datetime import datetime

def chatbot():
    print("\n================================")
    print("       PYTHON CHATBOT")
    print("================================")
    print("Bot: Hello! I am your Python chatbot.")
    print("Bot: Type 'help' to see what I can do.")
    print("Bot: Type 'bye' to exit.\n")

    name = input("Bot: What is your name? ")
    print(f"Bot: Nice to meet you, {name}!")

    while True:
        user = input(f"\n{name}: ").lower().strip()

        if user in ["hello", "hi", "hey"]:
            print("Bot:", random.choice([
                "Hello!",
                "Hi there!",
                "Hey! How can I help you?"
            ]))

        elif user == "how are you":
            print("Bot: I'm doing great! Thanks for asking.")

        elif user == "what is your name":
            print("Bot: My name is Python Bot.")

        elif user == "time":
            current_time = datetime.now().strftime("%I:%M %p")
            print("Bot: Current time is", current_time)

        elif user == "date":
            today = datetime.now().strftime("%d-%m-%Y")
            print("Bot: Today's date is", today)

        elif user == "help":
            print("""
Bot: Here are the commands you can use:
- hello
- how are you
- what is your name
- time
- date
- help
- bye
""")

        elif user == "bye":
            print(f"Bot: Goodbye {name}! Have a nice day.")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()
