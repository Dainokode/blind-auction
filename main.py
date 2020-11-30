from database import logo

print(logo)

print("Welcome to the secret auction program")

name = input("What is your name?: ")
bid = int(input("How much is your bid?: "))
choice = input("Are there any other bidders? Type 'yes' or 'no' ").lower()

bidders = []

def add_bidder(bidder_name, bid_amount):
    bidders.append({"name": bidder_name, "bid": bid_amount})

add_bidder(bidder_name=name, bid_amount=bid)      

while choice != "no":
    name = input("What is your name?: ")
    bid = int(input("How much is your bid?: "))
    choice = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    add_bidder(bidder_name=name, bid_amount=bid)

print(bidders[0]["bid"])

total = 0   
for index in range(len(bidders)):
    bid_amount = bidders[index]["bid"]
    if bid_amount > total:
        total = bid_amount

for index in range(len(bidders)):
    if bid_amount > total:
        total = bid_amount

import os
clear = lambda: os.system('cls')
clear()

for person in bidders:
    if total == person["bid"]:
        person_name = person["name"]
        print(f"{person_name} wins with a bid of £{total}")



    
