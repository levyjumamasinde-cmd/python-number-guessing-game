import random # import the random module to generate random numbers

def number_guessing_game():
    secret_no= random.randint(1, 20)# generate a secret number between 1 and 20
    attempts = 0 # counts the number of quesses the user makes
    guess = None # stores the users guess
    
    print("Welcome to my game; number guessing game!!")
    print("I have picked a number between 1 and 20. Try to guess it.")
    print('-'*50)
    while attempts < 5: # Allows the user upto 5 attempts
        try:
            # Gets input from the user and converts it into integer
            guess = int(input("Enter your guess: "))
            attempts += 1 # increase attempt count
            
            # Compares Guess with secret number
            if guess < secret_no:
                print("Too low! Try a higher number.")
            elif guess > secret_no:
                print("Too high! Try a lower number.")
            
            else:
                # If correct guess
                print(f"Congratulations! You guessed the number {secret_no} in {attempts} attempts.")
                return # End the Game if correct
                
        except ValueError: # Handle invalid input(like letters)
                print("Invalid input. Please enter a whole number.")
    # If user fails after 5 attempts
    print('-'*40)
        
    print("Game Over!!")
    print(f"The number was {secret_no}")

       
if __name__ == "__main__": # This ensures the game runs only when this file is executed directly
   
   # Asks the user if wants to play again
    while True:
        number_guessing_game()
        answer=input("Do you want to play again? (Yes/No): ").lower()
        if answer != "yes":
            print("Thank you for playing!: ")
            break
        
        

