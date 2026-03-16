import random

def number_guessing_game():
    secret_no= random.randint(1, 20)
    attempts = 0
    guess = None
    
    print("Welcome to my game; number guessing game!!")
    print("I have picked a number between 1 and 20. Try to guess it.")
    print('-'*50)
    while attempts < 5:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < secret_no:
                print("Too low! Try a higher number.")
            elif guess > secret_no:
                print("Too high! Try a lower number.")
            
            else:
                print(f"Congratulations! You guessed the number {secret_no} in {attempts} attempts.")
                return
                
        except ValueError:
                print("Invalid input. Please enter a whole number.")
    print('-'*40)
        
    print("Game Over!!")
    print(f"The number was {secret_no}")

       
if __name__ == "__main__":
    while True:
        number_guessing_game()
        answer=input("Do you want to play again? (Yes/No): ").lower()
        if answer != "yes":
            print("Thank you for playing!: ")
            break
        
        

