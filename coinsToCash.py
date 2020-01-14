# Create a function called calc_dollars. In the function body, define a dictionary and store it in a variable named piggyBank. The dictionary should have the following keys defined.

# quarters
# nickels
# dimes
# pennies
# For each coin type, give yourself as many as you like.

# Once you have given yourself a large stash of coins in your piggybank, look at each key and perform the appropriate math on the integer value to determine how much money you have in dollars. Store that value in a variable named dollarAmount and print it.

dollarAmount = 0

def calc_dollars():
    global dollarAmount
    piggyBank = {
        "quarters": 342,
        "nickels": 91,
        "dimes": 876,
        "pennies": 10035
    }
    dollarAmount += piggyBank["quarters"] * .25
    dollarAmount += piggyBank["nickels"] * .05
    dollarAmount += piggyBank["dimes"] * .1
    dollarAmount += piggyBank["pennies"] * .01



calc_dollars()
print(f"The total dollar amount is ${dollarAmount}")    


