# Convert the dollar amount into the coins that make up that dollar amount. The final result is an object with the correct number of quarters, dimes, nickels, and pennies.
import math

def make_change():
    dollar_amount = 8.69
    piggy_bank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
    }

    piggy_bank["quarters"] = math.floor(dollar_amount / .25 )
    dollar_amount %= .25
    piggy_bank["dimes"] = math.floor(dollar_amount / .1 )
    dollar_amount %= .1
    piggy_bank["nickels"] = math.floor(dollar_amount / .05 )
    dollar_amount %= .05

# dollarAmount = 8.69

# piggyBank = {
#     "pennies": 0,
#     "nickels": 0,
#     "dimes": 0,
#     "quarters": 0
# }

# def reduceAmount(num1, num2):
#     return round(num1 -num2, 2)

# def cashToCoins(amount):
#     num_quarters = amount // .25
#     val_quarters = num_quarters * .25
#     piggyBank["quarters"] = int(num_quarters)
#     amount = reduceAmount(amount, val_quarters)
    
#     num_dimes = amount // .1
#     val_dimes = num_dimes * .1
#     piggyBank["dimes"] = int(num_dimes)
#     amount = reduceAmount(amount, val_dimes)

#     num_nickels = amount // .05
#     val_nickels = num_nickels * .05
#     piggyBank["nickels"] = int(num_nickels)
#     amount = reduceAmount(amount, val_nickels)

#     num_pennies = amount // .01
#     piggyBank["pennies"] = int(num_pennies)


# cashToCoins(dollarAmount)

# print(piggyBank)