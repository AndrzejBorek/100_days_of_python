from gettext import find


def caesar_ciphre(message,shift):
    letters = "abcdefghijklmnoprstqwuxyz"
    chifred_message = ""
    for i in range(len(message)):
        letter = message[i]
        index = letters.find(letter)
        pos = index + shift
        if (pos >= len(letters)):
            pos = shift - (len(letters)-index)
        chifred_message = chifred_message+letters[pos]
    print(chifred_message)
    

shift = int(input("Give the shift of numbers "))
message = input("Give message  ")

caesar_ciphre(message=message,shift=shift)
