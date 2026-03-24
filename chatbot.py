import random
import datetime

print("🤖 Chatbot: Hello! I'm your bot.")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    if user_input in ["hello", "hi", "hey"]:
        responses = ["Hello there! 😊", "Hi How can I help you?", "Hey! What's up?"]
        print("🤖 Chatbot:", random.choice(responses))

    elif "how are you" in user_input:
        print("🤖 Chatbot: I'm just a program, but I'm doing great! 😄")

    elif "name" in user_input:
        print("🤖 Chatbot: I'm your bot 🤖")

    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("🤖 Chatbot: Current time is", current_time)

    elif "joke" in user_input:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
            "Why did the computer get cold? Because it forgot to close Windows! 😂",
            "Why do Python programmers wear glasses? Because they can't C! 🤓"
        ]
        print("🤖 Chatbot:", random.choice(jokes))

    elif "help" in user_input:
        print("🤖 Chatbot: You can say hello, ask time, or tell me to tell a joke!")

    elif user_input == "bye":
        print("🤖 Chatbot: Goodbye! Have a great day! 👋")
        break

    else:
        print("🤖 Chatbot: Hmm... I didn't understand that. Try something else!")