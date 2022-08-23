def number_guessing_game():

    import random as r

    def win_condition(number_of_attempts):
        while number_of_attempts > 0:
            print(f"You have {number_of_attempts} attempts remaining to guess the number ")
            guess = int(input("Make a guess: "))
            if guess not in range(1,100):
                print("Your range is 1 to 100! Bad answear")
                return
            elif guess < number:
                print("Too low ")
                number_of_attempts -=1
            elif guess > number:
                print("Too high ")
                number_of_attempts -=1
            else:
                print("You won! ")
                return 
        print("You lost :(")   

    def choose_difficulty():
        difficulty = input("Choose a difficulty, type 'e' for easy and 'h' for hard: ")
        if difficulty == 'h':
            number_of_attempts = 5
        elif difficulty=='e':
            number_of_attempts = 10
        else:
            print("Wrong Symbol")
            return
        return number_of_attempts

    print("Welcome to the number guessing game! ")
    number = r.randint(1,100)
    print("I'm thinking of a number between 1 and 100. ")
    win_condition(choose_difficulty())

   
    
    
number_guessing_game()