import random

pows_of_2 = [128, 64, 32, 16, 8, 4, 2, 1]

#Converts decimal to binary
def decimal_to_binary(dec_num):
    binary_num = ""
    for num in pows_of_2:
        if dec_num >= num:
            binary_num = binary_num + "1"
            dec_num = dec_num - num
        else:
            binary_num = binary_num + "0"
    return binary_num

#Checks if player input is valid
def check_valid_input(player_input, mode):
    if mode == 1:
        if len(player_input) == 8:
            for char in player_input:
                if char != "0" and char != "1":
                    return False
            return True
        else:
            return False
    if mode == 0:
        for char in player_input:
            if not char.isdigit():
                return False
        return True
        
#Asks player if they want to play again
def play_again():
    while True:
        response = input("Play again? (y/n): ")
        if response == "y":
            return True
        elif response == "n":
            print("Thanks for playing!")
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            

#Determines which mode to put the game in
while True:
    mode = input("0 for binary to decimal, 1 for decimal to binary\n")
    if mode == "0":
        mode = int(mode)
        break
    elif mode == "1":
        mode = int(mode)
        break
    else:
        print("Invalid input. Please enter 0 or 1")



"""GAME LOOP"""
while True:
    correct_answer = random.randint(0, 255)
    binary_number = decimal_to_binary(correct_answer)
    
    if mode == 1:
        #Decimal to binary
        guess = input("What is " + str(correct_answer) + " in binary?\n")
        if check_valid_input(guess, 1) == True:
            if guess == binary_number:
                print("Correct!")
            else:
                print("Wrong. The correct answer is " + str(binary_number))
        else:
            print("Invalid input. Please enter exactly 8 binary digits (0s and 1s).")
            continue
            
        if play_again() == True:
            continue
        else:
            exit()
    
    else:
        #Binary to decimal
        guess = input("What is " + str(binary_number) + " in decimal?\n")
        if check_valid_input(guess, 0) == True:
            if guess == str(correct_answer):
                print("correct!")
            else:
                print("Wrong. The correct answer is " + str(correct_answer))
        else:
            print("Invalid input. Please enter a number")
            continue
        
    if play_again() == True:
        continue
    else:
        exit()

