questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Rome"],
        "answer": 1
    },
    {
        "question": "Which language is used for AI?",
        "options": ["C", "Java", "Python", "HTML"],
        "answer": 3
    }
]
def menu():
  print("1. Add Question")
  print("2. Start Quiz")
  print("3. Exit")
  
def load_questions():
  quest=input("Enter your question: ")
  option=[]
  for i in range(4):
    opt=input(f"Enter option {i+1}:")
    option.append(opt)
  answer=int(input("enter the anwer option number (1-4):"))
  questions.append({
    "question":quest,
    "options":option,
    "answer":answer
  })
  print("Question added successfully!")

def ask_question(q):
  print(q["question"])
  for i, opt in enumerate(q["options"],start=1):
    print(i, opt)

  ans=int(input("your answer (1-4):"))
  return ans == q["answer"]


def start_qiux():
  score = 0
  for q in questions:
    if ask_question(q):
      print("Correct!")
      score += 1
    else:
      print("worng answer.")
  print(f"Your final score is {score} out of {len(questions)}")


def main():
  while True:
    menu()
    choice=int(input("Enter your choice:"))
    if choice == 1:
      load_questions()
    elif choice == 2:
      start_qiux()
    elif choice == 3:
      print("Exiting the quiz. Goodbye!")
      break
    else:
      print("Invalid choice. Please  Try again.")

if __name__ == "__main__":
  main()