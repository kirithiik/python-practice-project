questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["Python", "Java", "JavaScript", "C++"],
        "answer": "JavaScript"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    }
]

def start_quiz():
    score = 0
    total = len(questions)

    print("🧠 Quiz Started")
    print("----------------")

    for q in questions:
        print("\n" + q["question"])

        for i, option in enumerate(q["options"], start=1):
            print(f"{i}. {option}")

        user_choice = int(input("Enter option number: "))

        selected_answer = q["options"][user_choice - 1]

        if selected_answer == q["answer"]:
            print("Correct ✅")
            score += 1
        else:
            print(f"Wrong ❌ | Correct answer: {q['answer']}")

    print("\nQuiz Finished 🎉")
    print(f"Your score: {score}/{total}")

if __name__ == "__main__":
    start_quiz()
