def quiz_game():
    score=0
    questions = {
        "Who is the father of computers? " :"Charles Babbage", 
        "In which generation was integrated circuits first introdused? ":"Third generation",
        "What is USB in full? ":"Universal Serial Bus",
        "What is the unit for measuring storage space in computers? ":"Byte",
        "5GB is equals to how many kilobytes? ":"5242880",
        "Forth generation computers used what technogy? ": "Very large scale integrated circuits"
        }
    
    
    for question, correct_answer in questions.items():
        print("\n" + question)
        user_answer = input("Your answer: ")

        if user_answer.strip().lower() == correct_answer.lower():
            print("Correct!!")
            score += 1
        else:
           print(f"Wrong! The correct answer is {correct_answer}")
            
    print(f"\nYou scored {score} out of {len(questions)}")
quiz_game() 
     

   
