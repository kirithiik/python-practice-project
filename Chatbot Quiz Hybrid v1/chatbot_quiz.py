qa = [
    {"question": "What language is best for AI?", "answer": "python"},
    {"question": "What is the capital of France?", "answer": "paris"}
]

score = 0

def show_help():
    return (
        "I can help with:\n"
        "- add question\n"
        "- start quiz\n"
        "- view score\n"
        "- greetings\n"
        "- bye"
    )

def get_intent(user_input):
    user_input = user_input.lower()

    if "add question" in user_input:
        return "add"
    elif "start quiz" in user_input:
        return "quiz"
    elif "view score" in user_input:
        return "score"
    elif "bye" in user_input or "exit" in user_input:
        return "exit"
    elif "hello" in user_input or "hi" in user_input:
        return "greet"
    elif "help" in user_input:
        return "help"
    else:
        return "unknown"

def add_question():
    q = input("Enter the question: ").lower()
    a = input("Enter the answer: ").lower()
    qa.append({"question": q, "answer": a})
    print("Ras: Question added successfully")

def start_quiz():
    global score
    for item in qa:
        print("Ras:", item["question"])
        ans = input("You: ").lower()

        if item["answer"] in ans:
            print("Ras: Correct!\n")
            score += 1
        else:
            print(f"Ras: Wrong. Correct answer is {item['answer']}\n")

def main():
    print("Ras: Hello bro! I am Ras, your quiz chatbot. Type 'help' to see what I can do.")

    while True:
        user_input = input("You: ")
        intent = get_intent(user_input)

        if intent == "add":
            add_question()
        elif intent == "quiz":
            start_quiz()
        elif intent == "score":
            print(f"Ras: Your score is {score}")
        elif intent == "greet":
            print("Ras: Hello bro, what can I do for you?")
        elif intent == "help":
            print(show_help())
        elif intent == "exit":
            print("Ras: Goodbye bro!")
            break
        else:
            print("Ras: I don't understand that. Type 'help'.")

if __name__ == "__main__":
    main()
