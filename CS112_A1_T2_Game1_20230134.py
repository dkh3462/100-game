# File: CS112_A1_T2_Game1_20230134.py
# purpose: Two players start from 0 and alternatively add a number from 1 to 10 to the sum the player who reaches 100 wins.
# Author: Dima Khaled Allam Mohamed ديمه خالد علام محمد
# ID: 20230134

def game():
    # set sum to zero
    sum = 0
    while sum <= 100:
        print("Player 1 Please select a number from 1 to 10")
        move = input()
        while True:        # check that the player entered a number
            try:
                move = int(move)
                break
            except ValueError:
                print("INVALID INPUT Please enter a number from 1 to 10")
                move = input()
        sum += move
        while move < 1 or move > 10:        # check that the player entered a number from 1 to 10
            sum -= move
            print("Player 1 please enter a number from 1 to 10")
            move = int(input())
            sum += move
        print("Now the sum is", sum)
        if sum == 100:            # declare the winner if the sum is 100
            print("Player 1 is the winner")
            return menu()
        elif sum > 100:        # check if the sum exceeded 100
            while sum > 100:
                print("The sum exceeds 100 please select a suitable number")
                sum -= move
                move = int(input())
                while move < 1 or move > 10:  # check that the player entered a number from 1 to 10
                    sum -= move
                    print("Player 1 please enter a number from 1 to 10")
                    move = int(input())
                sum += move
                print("Now the sum is", sum)
                if sum == 100:        # declare the winner if the sum is 100
                    print("Player 1 is the winner")
                    return menu()
        print("Player 2 Please select a number from 1 to 10")
        move = input()
        while True:        # check that the player entered a number
            try:
                move = int(move)
                break
            except ValueError:
                print("INVALID INPUT Please enter a number from 1 to 10")
                move = input()
        sum += move
        while move < 1 or move > 10:        # check that the player entered a number from 1 to 10
            sum -= move
            print("Player 2 please enter a number from 1 to 10")
            move = int(input())
            sum += move
        print("Now the sum is", sum)
        if sum == 100:              # declare the winner if the sum is 100
            print("Player 2 is the winner")
            return menu()
        elif sum > 100:        # check if the sum exceeded 100
            while sum > 100:
                print("The sum exceeds 100 please select a suitable number")
                sum -= move
                move = int(input())
                while move < 1 or move > 10:  # check that the player entered a number from 1 to 10
                    sum -= move
                    print("Player 2 please enter a number from 1 to 10")
                    move = int(input())
                sum += move
                print("Now the sum is", sum)
                if sum == 100:           # declare the winner if the sum is 100
                    print("Player 2 is the winner")
                    return menu()


# Welcome message and display status
print("Welcome to 100 game")
def menu():
    print("[A] Start a new game")
    print("[B] End game")
    choice = input("Please enter your choice [A] or [B]")
    while choice == 'A' or choice == 'B':
        if choice == 'A':
            game()
        elif choice == 'B':
            break
        break
    while choice != 'A' and choice != 'B':
        print("INVALID CHOICE")
        choice = input("Please enter your choice [A] or [B]")
        if choice == 'A':
            game()
        elif choice == 'B':
            break
        break

menu()










