import random

def guess_number(x):
    
    random_number = random.randint(1, x)
    attempts = 0
    print(f"I've thought of a number between 1 and {x}. Can you guess it?")
    
    while True:
        
        attempts += 1
        guess = input("\n>>>")
        guess = int(guess)
        
        if guess < random_number:
            print("Incorrect. The number I'm thinking of is higher. Try again:")
            
        elif guess > random_number:
            print("Incorrect. The number I'm thinking of is lower. Try again:")
            
        else:
            break
    
    print(f"Congratulations! You guessed it in {attempts} attempts!\n")
    return attempts
    

def guess_number_pc(x):
    
    input(f"Think of a number between 1 and {x} and press any key when you're ready. I'll guess it!")
    
    upper_limit = x
    lower_limit = 1
    attempts = 0
    
    while True:
        
        attempts += 1
        
        if upper_limit != lower_limit:
            guess = random.randint(lower_limit, upper_limit)
        
        else:
            guess = lower_limit
            
        question = f"Is your number {guess}? Enter 'C' for correct, '+' if my guess is too low, or '-' if it's too high: "
        answer = input(question)
        
        if answer == 'C':
            print(f"I've guessed it! Your number is {guess}!")
            break
        
        elif answer == '+':
            lower_limit = guess + 1
            
        elif answer == '-':
            upper_limit = guess - 1
            
        else:
            print("Please respond with 'C', '+', or '-'.")
            
    print(f"I found your number in {attempts} attempts! Your number was {guess}!")
    return attempts
      

def play(x):
    
    play_again = True
    
    while play_again:
        
        user_attempts = guess_number(x)
        pc_attempts = guess_number_pc(x)
        
        if user_attempts > pc_attempts:
            print(f"I won with {pc_attempts} attempts!")
        
        elif user_attempts < pc_attempts:
            print(f"You won with {user_attempts} attempts!")
        else:
            print("It's a tie!")
            
        question = "\nDo you want to play again? (yes(1) / no(0)) "
        play_again = int(input(question))
        
        # if play_again != 1:
        #     play_again = False
