
import time
from colorama import Fore, Style, init

init()

def quiz_game():
    while True:
        print(Fore.CYAN + "\n=== QUIZ GAME ===" + Style.RESET_ALL)

        print("\nSelect difficulty level:")
        print("1) Easy (3 questions)")
        print("2) Medium (4 questions)")
        print("3) Hard (6 questions)")
        
        level = input("Enter 1, 2 or 3: ").strip()
        if level not in ["1", "2", "3"]:
            print(Fore.YELLOW + "Invalid choice, defaulting to Hard." + Style.RESET_ALL)
            level = "3"

        questions = [
            {
                "question": "Who is the father of computers?",
                "options": {"A": "Charles Babbage", "B": "Albert", "C": "George", "D": "Newton"},
                "answer": "A"
            },
            {
                "question": "In which generation was integrated circuits first introduced?",
                "options": {"A": "Second generation", "B": "Fourth generation",
                            "C": "Third generation", "D": "Fifth generation"},
                "answer": "C"
            },
            {
                "question": "What is USB in full?",
                "options": {"A": "Unit System Base", "B": "Universal System Backup",
                            "C": "Unit System Base", "D": "Universal Serial Bus"},
                "answer": "D"
            },
            {
                "question": "What is the unit for measuring storage space in computers?",
                "options": {"A": "Byte", "B": "Kilobyte", "C": "Bit", "D": "GB"},
                "answer": "A"
            },
            {
                "question": "5GB is equal to how many kilobytes?",
                "options": {"A": "5000", "B": "5242880", "C": "5000000", "D": "500"},
                "answer": "B"
            },
            {
                "question": "Fourth generation computers used what technology?",
                "options": {"A": "Very large scale integrated circuits", "B": "Magnetic Drums",
                            "C": "IC", "D": "AI"},
                "answer": "A"
            }
        ]

        if level == "1":
            selected_questions = questions[:3]
        elif level == "2":
            selected_questions = questions[:4]
        else:
            selected_questions = questions

        score = 0

        for q in selected_questions:
            print(Fore.BLUE + "\n" + q["question"] + Style.RESET_ALL)

            for key, value in q["options"].items():
                print(f"{key}) {value}")

            print(Fore.YELLOW + "⏳ You have 10 seconds to answer..." + Style.RESET_ALL)

            start_time = time.time()
            user_answer = input("Your answer (A/B/C/D): ").strip().upper()
            end_time = time.time()

            if (end_time - start_time) > 10:
                print(Fore.RED + "⏰ Time's up!" + Style.RESET_ALL)
                continue

            if user_answer == q["answer"]:
                print(Fore.GREEN + "Correct!! ✅" + Style.RESET_ALL)
                score += 1
            else:
                correct = q["answer"]
                print(Fore.RED + f"Wrong! Correct answer is {correct}) {q['options'][correct]}" + Style.RESET_ALL)

        total = len(selected_questions)
        percentage = (score / total) * 100

        print(Fore.CYAN + f"\nScore: {score}/{total} ({percentage:.1f}%)" + Style.RESET_ALL)

        if percentage >= 90:
            print(Fore.GREEN + "Excellent 🌟" + Style.RESET_ALL)
        elif percentage >= 70:
            print(Fore.YELLOW + "Good 👍" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Try Again 💡" + Style.RESET_ALL)

        replay = input("\nDo you want to play again? (Yes/No): ").strip().lower()
        if replay != "yes":
            print(Fore.CYAN + "Thank you for playing! 🎉" + Style.RESET_ALL)
            break

quiz_game()