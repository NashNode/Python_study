#练习1
prices = [80000, 82000, 79000, 85000, 81000]
print(prices[0])
print(prices[-1])
print(max(prices))
print(min(prices))
print(len(prices))
print(sum(prices))

#练习2
trade = {
    "coin": "BTC",
    "entry_price": 80000,
    "exit_price": 85000,
    "capital": 1000
}
print(trade["coin"])
print(trade["entry_price"])
trade["capital"]=2000
return_rate=(trade["exit_price"]-trade["entry_price"])/trade["entry_price"]*100
trade["return_rate"]=return_rate
print(trade)

#正式项目
trades = [100, -50, 200, -30, 80]
print("======== Trading Record Analyzer ========")
print(trades)
trades_length=len(trades)
print("Number of Trades:"+str(trades_length))
total_profit_loss=sum(trades)
print("Total Profit/Loss: $"+str(total_profit_loss))
best_trade=max(trades)
print("Best Trade: $"+str(best_trade))
worst_trade=min(trades)
print("Worst Trade: $"+str(worst_trade))
average = sum(trades) / len(trades)
print("Average Profit/Loss: $"+str(average))
total = sum(trades)
if total > 0 :
    print("Overall: PROFIT")
elif total == 0:
    print("Overall: BREAK EVEN")
else:
    print("Overall: LOSS")

#加分挑战
trades = [100, -50, 200, -30, 80]
new_trade=float(input("Enter new trade P/L:"))
trades.append(new_trade)
total_profit_loss=sum(trades)
print("Total Profit/Loss: $"+str(total_profit_loss))
average = sum(trades) / len(trades)
print("Average Profit/Loss: $"+str(average))
best_trade=max(trades)
print("Best Trade: $"+str(best_trade))
worst_trade=min(trades)
print("Worst Trade: $"+str(worst_trade))