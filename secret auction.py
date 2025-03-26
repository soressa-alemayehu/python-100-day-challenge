
bids = {}
bidding_finished = False
while not bidding_finished:
    name = input("type your name: ")
    price = int(input("what is your bid: $"))
    bids[name] = price
    other_bider = input("are there another bider?(Y/N): ")
    if other_bider == "n":
        bidding_finished = True
        highest_bid = 0
        winner = ""
        
        for bidder in bids:
            bid_amount = bids[bidder] 
            if highest_bid < bid_amount:
                highest_bid = bid_amount
                winner = bidder
        
        print(f" the higest bider  is{winner} with bid of {highest_bid}")


