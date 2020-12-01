import random

code = []
def create_code():
    global code
    while len(code) < 4:
        value = random.randint(1, 8) # 8 possible digits
        if value in code:
            continue
        else:                           # 8 possible digits
            code.append(value)

def show_instruction():
    print('4-digit Code has been set. Digits in range 1 to 8. ', end='')
    print('You have 12 turns to break it.')

def get_user_input():
    global answer
    answer = input("Input 4 digit code: ")
    while len(answer) != 4:
        print("Please enter exactly 4 digits.")
        answer = input("Input 4 digit code: ")

def check_user_input():
    # global code
    global correct_digits_and_position
    global correct_digits_only
    correct_digits_and_position = 0
    correct_digits_only = 0
    for i in range(len(answer)):
        if code[i] == int(answer[i]):
            correct_digits_and_position += 1
        elif int(answer[i]) in code:
            correct_digits_only += 1


def show_result():
    global correct_digits_and_position
    global correct_digits_only
    print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
    print('Number of correct digits not in correct place: '+str(correct_digits_only))


def game_status():
    global correct
    if correct_digits_and_position == 4:
        correct = True
        print('Congratulations! You are a codebreaker!')
    else:
        print('Turns left: '+str(12 - turns))



def show_code():
    print('The code was: '+str(code))


def run_game():
    global correct
    global turns
    global answer
    correct = False
    turns = 0
    create_code()
    show_instruction()
    while not correct and turns < 12:
        turns += 1
        get_user_input()
        check_user_input()
        show_result()
        game_status()
    show_code()


if __name__ == "__main__":
    run_game()
