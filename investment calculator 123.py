investment_amount = int(input("enter investment amount(greater than 0 less than 50000)"))
while investment_amount > 50000 or investment_amount <= 0 :
    print("value out of range")
    investment_amount = int(input("please provide an amount between 0-50000"))
intrest_rate = int(input("please enter the intrest rate between 0-15"))
while intrest_rate > 15 or intrest_rate <= 0 :
    print("value out of range")
    intrest_rate = int(input("please enter a intrest rate within 0-15"))
duration = int(input("please enter the duration of years of the investment"))
while duration <= 0 :
    int(input("value invalid please enter an amount greater than 0"))
months = duration * 12 
Monthly_intrest_rate = (intrest_rate / 12) / 100
total_balance = 0
for month in range(1,months + 1): 
    total_balance * Monthly_intrest_rate + total_balance
    total_balance = round(investment_amount + total_balance)
    if month % 12 == 0:
        print(f"Year {month // 12}: {total_balance}")
print (total_balance + investment_amount) 
print(f"Investment Duration: {duration} years")
print(f"Yearly Interest Rate: {Monthly_intrest_rate}.0% ")
print(f"Monthly Investment Amount: ${investment_amount} ")
