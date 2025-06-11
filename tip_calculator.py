print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 or 15? "))
people = int(input("How many people to split the bill? "))

indiv_amt = (bill + (tip/100) * bill)/people
print(f"Each person should must pay ${round(indiv_amt, 2)}")
