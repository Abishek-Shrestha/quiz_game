#import library for json file
import json

# Function to load quiz questions from a JSON database
def load_questions():
    # Making statement to handle the error if the file is not found
    try:
        with open("quiz_data.json", "r") as file:
            return json.load(file)  # Load questions from file
    except FileNotFoundError:
        print("Error: quiz_data.json file not found!")
        return []

# Function to run the quiz
def run_quiz():
    while True:  # Loop to allow replaying the quiz
        questions = load_questions()  # Load questions from the database
        # Check if questions are available
        if not questions:
            print("No questions available! Please check the database.")
            return
        
        print("\n🎯 Welcome to the Quiz Game! 🎯")
        print("Type your answer and press Enter.\n")

        score = 0  # Initialize score

        for q in questions:
            print(q["question"])  # Show question
            user_answer = input("Your answer: ").strip().lower()  # Get user's answer (convert to lowercase)

            if user_answer == q["answer"].lower():  # Check if answer is correct
                print("✅ Correct!\n")
                score += 1
            else:
                print(f"❌ Incorrect! The correct answer is: {q['answer']}\n")

        # Display final score
        print("🎉 Quiz Completed! 🎉")
        print(f"Your final score: {score}/{len(questions)}")

        # Option to Play Again or Exit
        while True:
            choice = input("\nDo you want to play again? (yes/no): ").strip().lower()
            if choice == "yes":
                break  # Restart the quiz
            elif choice == "no":
                print("Thanks for playing! Goodbye! 👋")
                return  # Exit the game
            else:
                print("Invalid input! Please type 'yes' or 'no'.")

# Run the quiz
run_quiz()
