from datetime import datetime

def show_help():
    return (
        "I can help with:\n"
        "- greetings\n"
        "- time\n"
        "- how are you\n"
        "- creator\n"
        "- bye"
    )

def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello mate ! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm doing great! How about you?"
    elif "time" in user_input:
        now = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {now}."
    elif "who made you" in user_input or "creater" in user_input:
        return "I was created by Ras"
    elif "help" in user_input:
        return show_help()
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry  , I dont understand that. Type 'help' to see what can i do."
    
def main():
    print("Heello! I'm your chatbot. Type 'help' to see what i can do.")
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Bot:", response)
        if "bye" in user_input.lower() or "exit" in user_input.lower():
            break

if __name__ == "__main__":
    main()