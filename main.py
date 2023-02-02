from replit import clear
from art import logo

bidders = []


def add_new_bidder():
    name = input("What is your name?: ")
    bid = float(input("What is your bid: $"))
    new_bidder = {}
    new_bidder["name"] = name
    new_bidder["bid"] = bid
    bidders.append(new_bidder)

    
def calculate_higher_bid():
    higher_bid = 0
    name = ""
    for bidder in bidders:
        if bidder["bid"] > higher_bid:
            name = bidder["name"]
            higher_bid = bidder["bid"]
    print(f"The winner is {name} with a bid of ${higher_bid}")
    

other_bidder = True
print(logo)

while other_bidder:
    add_new_bidder()
    if input("Are there any other bidders? Type 'yes' or any key to close: ") != "yes":
        other_bidder = False
    clear()
    
calculate_higher_bid()
