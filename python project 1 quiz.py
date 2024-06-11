# Define the questions, options, and correct answers
questions = [
    {
        "question": "What is the mother tounge of Mahatma gandhi?",
        "options": ["A. Bengali", "B. Telugu", "C. Gujarati", "D. Tamil"],
        "answer": "C"
    },
    {
        "question": "Which language is spoken by Andhra people?",
        "options": ["A. Tamil", "B. Telugu ", "C. kannada", "D. hindi"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"],
        "answer": "D"
    }
]

def ask_question(question):
    print(question["question"])
    for option in question["options"]:
        print(option)
    answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
    while answer not in ["A", "B", "C", "D"]:
        print("Invalid option. Please enter A, B, C, or D.")
        answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
    return answer

def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer

def quiz_game(questions):
    score = 0
    for question in questions:
        user_answer = ask_question(question)
        if check_answer(user_answer, question["answer"]):
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is {question['answer']}.")
        print()
    print(f"Your final score is {score} out of {len(questions)}.")

if __name__== "__main__":
    quiz_game(questions)