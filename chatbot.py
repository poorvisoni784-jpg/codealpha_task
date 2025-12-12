"""
Basic Rule-Based Chatbot
Author: Your Name
Description:
    A very simple chatbot that replies to specific user inputs.
    Demonstrates:
    - if-elif conditions
    - functions
    - loops
    - simple input/output
"""

def get_reply(user_input):
    """Return a predefined reply based on the user's message."""
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "I don't understand that."

def chatbot():
    """Main chatbot loop."""
    print("🤖 Chatbot: Type something (hello, how are you, bye)")

    while True:
        user_input = input("You: ")

        reply = get_reply(user_input)
        print("Bot:", reply)

        if user_input.lower() == "bye":
            break


if __name__ == "__main__":
    chatbot()
