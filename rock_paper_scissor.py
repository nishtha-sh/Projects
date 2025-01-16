import random

def play():
    user_input = "a"
    com_input = "b"
    while user_input != com_input: #This is only an added feature, the loop will break when it's a tie.
        user_input = input("Select one out of these: (s) for scissor, (r) for rock, (p) for paper: ")
        com_input = random.choice(["p","r","s"])
        if (user_input == "r" and com_input == "s") or (user_input == "s" and com_input == "p") or (user_input == "p" and com_input == "r"):
            print(f"You won: {user_input} vs {com_input}")
        elif user_input == com_input:
            print("It's a tie")
        else:
            print(f"You lost: {user_input} vs {com_input}")

play()