#练习1
def show_coin(coin):
    print(f"Coin: {coin}")
show_coin("BTC")

#练习2
def calculate_return_rate(entry_price, exit_price):
    return_rate = (exit_price - entry_price) / entry_price * 100
    return return_rate
rate = calculate_return_rate(80000, 85000)
print(rate)

#练习3
def get_trade_status(trade):
    if trade > 0:
        return "PROFIT"
    elif trade < 0:
        return "LOSS"
    else:
        return "BREAK EVEN"
print(get_trade_status(100))
print(get_trade_status(-50))
print(get_trade_status(0))

#正式项目
print("======== Trading Record Analyzer V3 ========")

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
    print("======== Statistics ========")
    print(f"Number of Trades: {len(trades)}")
    print(f"Total Profit/Loss: ${calculate_total(trades)}")
    print(f"Win Rate: {calculate_win_rate(trades)}%")
    total = calculate_total(trades)
    if total > 0 :
        print("Overall: PROFIT")
    elif total < 0 :
        print("Overall: LOSS")
    else :
        print("Overall: BREAK EVEN")

trades = [100, -50, 200, -30, 80, 0]
analyze_trades(trades)



#加分挑战
def input_trades():
    trades = []
    while True:
        command = input("Enter trade P/L (or q to quit): ")
        if command == "q":
            break
        trade = float(command)
        trades.append(trade)
    return trades

trades = input_trades()
analyze_trades(trades)