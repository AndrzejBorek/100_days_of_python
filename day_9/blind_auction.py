def auction():
    play = True
    offerts = {}
    highest_name = ""
    highest_bid = 0
    while play == True:
        name = input("What is your name? ")
        bid = int(input("Whats your bid? "))
        offerts[name] = bid
        play_further = input("Are there any other biders? Y for yes N for no ")
        if play_further == "N":
            play = False
            break
        
    for key in offerts:
        if offerts[name] > highest_bid:
            highest_bid = offerts[name]
            highest_name = name
    print(f"Auction is won by {highest_name} with offer {highest_bid}  ")
 