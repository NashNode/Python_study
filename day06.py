#练习1
command = input("Enter coin:")
print(f"Coin: {command.strip().upper()}")

#练习2
trades = [100, -50, 200]
with open("trades.txt","w") as file :
    for trade in trades:
        str(trade)
        file.write(f"{trade}\n")

#练习3
prices = []
with open("prices.txt","r") as file:
    for line in file:
        price = float(line.strip())
        prices.append(price)
print(f"Highest Price:{max(prices)}")
print(f"Lowest Price:{min(prices)}")
print(f"Average Price:{sum(prices) / len(prices):.2f}")

#正式项目：Trading Record Analyzer V4
def save_trade(trade):
    with open("trades.txt","a") as file :
        file.write(f"{trade}\n")

def load_trades():
    trades = []
    with open("trades.txt","r") as file :
        for line in file :
            trades.append(float(line.strip()))
    return trades

def get_trade_status(trade):
    if trade > 0:
        return "PROFIT"
    elif trade < 0:
        return "LOSS"
    else:
        return "BREAK EVEN"

def calculate_total(trades):
    total = 0
    for trade in trades :
        total += trade
    return total

def calculate_win_rate(trades):
    win_trade = 0
    total_trade = 0
    for trade in trades :
        if trade > 0 :
            win_trade += 1
            total_trade += 1
        else :
            total_trade += 1
    if total_trade > 0:
        return win_trade / total_trade * 100
    else:
        return "No trades entered."

def analyze_trades(trades):
    for trade in trades:
        status = get_trade_status(trade)
        print(f"Trade: ${trade} → {status}")

trades = load_trades()

while True:
    command = input("Enter trade P/L (or q to quit): ")

    if command == "q":
        break

    trade = float(command)

    trades.append(trade)
    trade = str(trade)
    save_trade(trade)

analyze_trades(trades)

#Day 6 小挑战
import csv

with open("trades.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["profit_loss"])

    for trade in trades:
        trade = str(trade)
        writer.writerow(trade)