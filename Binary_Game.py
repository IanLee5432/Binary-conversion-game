import random

pows_of_2 = [128, 64, 32, 16, 8, 4, 2, 1]
score = 0
attempts = 0

#Converts decimal to binary, returns an 8-digit binary number as a string
def decimal_to_binary(dec_num):
    binary_num = ""
    for num in pows_of_2:
        if dec_num >= num:
            binary_num = binary_num + "1"
            dec_num = dec_num - num
        else:
            binary_num = binary_num + "0"
    return binary_num

#Checks if player input is valid, returns boolean
#Mode 1 = checks if it is a valid binary num, Mode 0 checks if they input a number
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
        player_input = player_input.strip() #Takes out extra spaces
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
            print(f"Thanks for playing! Your score was {score}/{attempts}, or {(score/attempts)*100}%")
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            

#Determines which mode to put the game in
while True:
    mode = input("0 for binary to decimal, 1 for decimal to binary\n")
    if mode == "0":
        mode = int(mode)
    elif mode == "1":
        mode = int(mode)
    else:
        print("Invalid input. Please enter 0 or 1")
    
    for i in range(5):
        correct_answer = random.randint(0, 255)
        binary_number = decimal_to_binary(correct_answer)
    
        if mode == 1:
            # Decimal to binary game
            while True:
                guess = input("What is " + str(correct_answer) + " in binary?\n")
                if check_valid_input(guess, 1):
                    if guess == binary_number:
                        print("Correct!")
                        score += 1
                        attempts += 1
                        break
                    else:
                        print("Wrong. The correct answer is " + str(binary_number))
                        attempts += 1
                        break
                else:
                    print("Invalid input. Please enter exactly 8 binary digits (0s and 1s).")
                    continue
    
        else:  # Binary to decimal game
            while True:
                guess = input("What is " + str(binary_number) + " in decimal?\n")
                if check_valid_input(guess, 0):
                    if guess == str(correct_answer):
                        print("Correct!")
                        score += 1
                        attempts += 1
                        break
                    else:
                        print("Wrong. The correct answer is " + str(correct_answer))
                        attempts += 1
                        break
                else:
                    print("Invalid input. Please enter a number")
                    continue

    # Ask the user if they want to play again
    if not play_again():
        break
