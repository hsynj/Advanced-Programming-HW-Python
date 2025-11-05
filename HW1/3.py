count = 2000
buy = 40.00
buy_commission = 0.03 * buy * count
sell = 42.75
sell_commission = 0.03 * sell * count
print(f"Joe paid $, {buy * count}, for buy stock.")
print(f"Joe paid $, {buy_commission}, for buy commission.")
print(f"Joe sold the stock for $, {sell * count}.")
print(f"Joe paid $, {sell_commission}, for sell commission.")
x = (sell * count) - (buy * count) - buy_commission - sell_commission
print(f"Joe's profit is $, {x}.")
if x > 0:
    print("Joe made a profit.")
else:
    print("Joe made a loss.")