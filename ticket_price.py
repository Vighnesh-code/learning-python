print("Welcome to the ticket price calculator!")

height = int(input("What's your height? "))

if (height >= 120):
    print("Yes, you can buy the ticket.")
    age = int(input("What's your age? "))
    if (age <= 12):
        print("You will have to pay $5")
    elif (age <= 18):
        print("You will have to pay $7")
    else:
        print("You will have to pay $12")
else:
    print("You can't buy the ticket. You are a midget! 😂")
