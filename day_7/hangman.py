import random as r

def charposition(string, char):
    pos = [] #list to store positions for each 'char' in 'string'
    for n in range(len(string)):
        if string[n] == char:
            pos.append(n)
    return pos

word_list = ["hangman","babajaga","veryhardword"]


word = r.choice(word_list)

for i in range(0,len(word)):
    print("_", end = "")
lives = 6
used_letters = []
answear = ["_"]
answear = answear * len(word)

while lives >= 0:
    if lives == 0:
        print("You lost")
        break
    else:
        print("    ")
        letter = input(f"Guess the letter you have {lives} chances   ")
        print(f" You have already used  {used_letters} ")
        print("")
        pos = charposition(word,letter)
        if len(pos) == 0:
            lives = lives -1
            used_letters.append(letter)
            print("Wrong letter!")
        else:
            for i in pos:
             answear[i] = letter
            for i in range(0,len(answear)):
                print(answear[i]+"",end = "")
                    
        if "_" not in answear:
            print("You won")
            break

        

            

            
