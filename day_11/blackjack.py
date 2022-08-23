def blackjack():

    import random as r

    def who_won(my_points,computer_points):
        if my_points > computer_points and my_points <= 21:
            print("You won!")
        elif my_points > computer_points and my_points > 21:
            print("you lost!")
        elif computer_points > my_points and computer_points <= 21:
            print("You lost!")
        elif computer_points > my_points and computer_points > 21:
            print("You won")
        else:
            print("DRAW!")

    def add_card(cards,deck,number_of_cards):
        for i in range(number_of_cards):
            deck.append(r.choice(list(cards)))

    def print_cards(deck,whose):
        print(f"{whose} cards: {deck}")

    def print_points(points,whose):
        print(f"{whose} points {points}")

    def decrease_cards(cards,deck):
        for card in deck:
            cards[card][1] -=1 

    def calculate_points(cards,deck,points):
        for card in deck:
            if card == "A":
                if points <= 10:
                    cards[card][0] = 11
                else:
                    cards[card][0] = 1
            points +=  cards[card][0]
        return points

    cards = { 
        "2":[2,4],
        "3":[3,4],
        "4":[4,4],
        "5":[5,4],
        "6":[6,4],
        "7":[7,4],
        "8":[8,4],
        "9":[9,4],
        "10":[10,4],
        "J":[10,4],
        "Q":[10,4],
        "K":[10,4],
        "A":[[1,11],4]
        }

    choice_to_play = input("Yo, want to play blackjack? Type 'y' for yes 'n' for no ")
    if choice_to_play == 'y':
        my_cards=[]
        computer_cards = []
        add_card(cards=cards,deck=my_cards,number_of_cards=2)
        decrease_cards(cards,my_cards)
        print_cards(my_cards,"Your")
        add_card(cards=cards,deck = computer_cards,number_of_cards=1)
        decrease_cards(cards,computer_cards)
        print_cards(computer_cards,"Computer")
        choice_to_get_card = input("Type 'y' to get another card, type 'n' to pass  ")
        if choice_to_get_card == 'y':
            add_card(cards=cards,deck=my_cards,number_of_cards=1)
            cards[my_cards[-1]][1] -= 1
            print_cards(my_cards,"Your")
            no_cards = True
            while no_cards:
                last_card = r.choice(list(cards))
                if cards[last_card][1] == 0:
                    last_card = r.choice(list(cards))
                else:
                    add_card(cards=cards,deck = computer_cards,number_of_cards=1)
                    cards[computer_cards[-1]][1] -= 1
                    no_cards = False
            print_cards(computer_cards,"Computer")
            my_points,computer_points = 0,0
            my_points =  calculate_points(cards,my_cards,my_points)
            print_points(my_points,"Your")
            computer_points = calculate_points(cards,computer_cards,computer_points)
            print_points(computer_points,"Computer")
        else:
            add_card(cards=cards,deck = computer_cards,number_of_cards=1)
            cards[computer_cards[-1]][1] -= 1
            print_cards(computer_cards,"Computer")
            my_points, computer_points = 0,0
            my_points = calculate_points(cards,my_cards,my_points)
            print(f"my points {my_points}")
            computer_points = calculate_points(cards,computer_cards,computer_points)
            print(f"computer points {computer_points}")
        who_won(my_points,computer_points)
    else:
        return 0   

blackjack()

