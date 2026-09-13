#练习1
coins = ["BTC", "ETH", "SOL", "LINK"]
for coin in coins:
    print(f"Coin: {coin}")

#练习2
for i in range(1,6):
    print(i)
for i in range(2,11,2):
    print(i)

#练习3
total = 0
numbers = [10, 20, 30, 40, 50]
for number in numbers:
    total = total + number
print(total)

#正式项目：Trading Record Analyzer V2
print("======== Trading Record Analyzer V2 ========")
trades = [100, -50, 200, -30, 80, 0]
for trade in trades:
    if trade > 0:
        print(f"Trade: ${trade} → PROFIT")
    elif trade == 0 :
        print(f"Trade: ${trade} → BREAK EVEN")
    else :
        print(f"Trade: ${trade} → LOSS")
print("======== Statistics ========")
number_of_trades = 0
winning_trades = 0
losing_trades = 0
break_even_trades = 0
total_profit_loss = 0
for trade in trades :
    number_of_trades += 1
    total_profit_loss = total_profit_loss + trade
    if trade > 0:
        winning_trades += 1
    elif trade < 0 :
        losing_trades += 1
    else :
        break_even_trades += 1
print(f"Number of Trades: {number_of_trades}")
print(f"Winning Trades: {winning_trades}")
print(f"Losing Trades: {losing_trades}")
print(f"Break Even Trades: {break_even_trades}")
win_rate=winning_trades / number_of_trades * 100
print(f"Win Rate: {win_rate:.2f}%")
print(f"Total Profit/Loss: ${total_profit_loss}")
average_Profit_loss = total_profit_loss / number_of_trades
print(f"Average P/L: ${average_Profit_loss:.2f}")
if total_profit_loss > 0 :
    print("Overall: PROFIT")
elif total_profit_loss < 0 :
    print("Overall: LOSS")
else :
    print("Overall: BREAK EVEN")


#加分挑战
print("======== Trading Record Analyzer V2 ========")
trades = []
while True :
    command=input("Enter trade P/L (or q to quit):")
    if command != "q" :
        command=float(command)
        trades.append(command)
    elif command == "q" :
        break
for trade in trades:
    if trade > 0:
        print(f"Trade: ${trade} → PROFIT")
    elif trade == 0 :
        print(f"Trade: ${trade} → BREAK EVEN")
    else :
        print(f"Trade: ${trade} → LOSS")
print("======== Statistics ========")
number_of_trades = 0
winning_trades = 0
losing_trades = 0
break_even_trades = 0
total_profit_loss = 0
for trade in trades :
    number_of_trades += 1
    total_profit_loss = total_profit_loss + trade
    if trade > 0:
        winning_trades += 1
    elif trade < 0 :
        losing_trades += 1
    else :
        break_even_trades += 1
print(f"Number of Trades: {number_of_trades}")
print(f"Winning Trades: {winning_trades}")
print(f"Losing Trades: {losing_trades}")
print(f"Break Even Trades: {break_even_trades}")
win_rate=winning_trades / number_of_trades * 100
print(f"Win Rate: {win_rate:.2f}%")
print(f"Total Profit/Loss: ${total_profit_loss}")
average_Profit_loss = total_profit_loss / number_of_trades
print(f"Average P/L: ${average_Profit_loss:.2f}")
if total_profit_loss > 0 :
    print("Overall: PROFIT")
elif total_profit_loss < 0 :
    print("Overall: LOSS")
else :
    print("Overall: BREAK EVEN")
