#练习1
btc_price=float(input("BTC price:"))
if btc_price > 100000:
    print("BTC is above $100,000")
else:
    print("BTC is below or equal to $100,000")

#练习2
return_rate=float(input("Return rate (%):"))
if return_rate > 0:
    print("Profit")
elif return_rate == 0:
    print("Break even")
else:
    print("Loss")

#练习3
btc_price2=float(input("BTC price:"))
btc_daily_change=float(input("BTC daily change (%):"))
if btc_price2 > 100000 and btc_daily_change > 5:
    print("Strong bullish")
elif btc_price2 > 100000:
    print("Bullish")
else:
    print("Normal market")

#正式项目：BTC Profit Calculator
entry_price=float(input("Entry Price:"))
exit_price=float(input("Exit Price:"))
capital=float(input("Capital:"))
return_rate = (exit_price - entry_price) / entry_price * 100
print("Return:"+str(return_rate)+"%")
profit_loss=return_rate / 100 * capital
print("Profit/Loss: $"+str(profit_loss))
if return_rate > 0:
    print("Status: PROFIT")
elif return_rate == 0:
    print("Status: BREAK EVEN")
else:
    print("Status: Loss")
#加分挑战
if return_rate >= 10:
    print("GREAT PROFIT")
elif return_rate > 0:
    print("PROFIT")
elif return_rate ==0:
    print("BREAK EVEN")
elif return_rate > -10:
    print("LOSS")
else:
    print("BIG LOSS")