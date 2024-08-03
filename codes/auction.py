import os

auction_dict = {}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_dictionary(name, price):
    auction_dict[name] = price

def result(auction_dict):
    max_bid = max(auction_dict.values(), key=lambda x: float(x))
    winner = [name for name, bid in auction_dict.items() if bid == max_bid][0]
    print(f"Dictionary: {auction_dict}")
    print(f"\nThe Winner is {winner} with a bid of ${max_bid}")

def auction():
    ans = True
    while ans:
        print("Welcome to the auction of the product\n")
        name = input("What is your name?\n")
        price = input("What is your bid?\n")

        while price in auction_dict.values():
            print(f"This bid of ${price} is already taken, try again")
            price = input("What is your bid?\n")

        add_dictionary(name, price)

        while True:
            cont = input("Are there other bidders? Type 'Yes' or 'No'\n").lower()
            if cont == "no":
                ans = False
                break
            elif cont == "yes":
                clear()
                break
            else:
                print("Invalid input. Please type 'Yes' or 'No'.")

    result(auction_dict)

auction()
