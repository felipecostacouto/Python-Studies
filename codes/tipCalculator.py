print("Welcome to the tip calculator!")
totalBill = float(input("What is your total bill? $"))
percentage = int(input("How much tip would you like to give(percentage)? 10,12, or 15 ? "))

while percentage != 10 and percentage != 12 and percentage != 15:
    print("Please input a valid percentage (10 or 12 or 15) without the %")
    percentage = int(input("How much tip would you like to give? 10,12 or 15 ? "))

numbPeople = int(input("How many people to split the bill ? "))
total = totalBill + (totalBill * percentage / 100)
ans = ("%.2f" % round(total / numbPeople, 2))
print(f"Each person should pay: ${ans}")
