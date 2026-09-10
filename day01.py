#练习一
name="Nathan"
age="20"
city="..."
print("My name is "+name)
print("I am "+age+" years old")
print("I live in "+city)
#练习二
BTC价格 = 100000
BTC数量 = 0.15
print(BTC价格*BTC数量)
#练习三
BTC_price=float(input("BTC price:"))
BTC_amount=float(input("BTC amount:"))
print(BTC_price*BTC_amount)

#小项目
print("Personal Asset Calculator")
btc_amount=float(input("BTC数量："))
btc_price=float(input("BTC价格："))
btc_value=btc_amount*btc_price
stock=float(input("股票资产："))
cash=float(input("现金："))
total_asset=btc_value+stock+cash
print("BTC Value:$"+str(btc_value))
print("Stock Value:$"+str(stock))
print("Cash:$"+str(cash))
print("Total Asset:$"+str(total_asset))




