import random

total_tails = 0
total_heads = 0


def main():
    user_num = get_valid_number("Enter a number: ")
    for _ in range(user_num):
        flip_coin()
    print_results(user_num)


def get_valid_number(prompt: str) -> int:
    #Continuously prompt the user until True.
    while True:
        user_input = input(prompt)
        if check_input(user_input):
            return int(user_input)
        else:
            print("That doesn't work!")


def check_input(user_input: str) -> int:
    try:
        return int(user_input) > 0
    except ValueError:
        return False
    
    
def flip_coin():
    global total_heads
    global total_tails
    
    #basic code to flip a coin
    choice = random.choice(["Heads", "Tails"])
    if choice == "Heads":
        total_heads += 1
    else:
        total_tails += 1
    return 


def print_results(user_input):
    #Choose the side with the higher total
    winning_side, winning_total = (
        ("Heads", total_heads)
        if total_heads > total_tails
        else ("Tails", total_tails)
        )
    
    #Calculate winning percentage
    winning_percentage = int((winning_total / user_input) * 100)

    #Build the percentage bar
    percentage_won_icon = "█" * winning_percentage
    percentage_lost_icon = "▒" * (100 - winning_percentage)
    
    #Print out results
    print(f"\n\n\n\n\n\n\n{percentage_won_icon}{percentage_lost_icon} {winning_percentage}%")
    print(f"{winning_side} Won By: {winning_percentage}% Out Of 100%")
    print(f'\n--{winning_side.upper()}--\n')
    
    
if __name__ == "__main__":
    main()