print("Welcome to the ticket price calculator!")

height = int(input("What's your height? "))
bill = 0

if (height >= 120):
    print("Yes, you can buy the ticket.")
    age = int(input("What's your age? "))
    if (age <= 12):
        bill = 5
    elif (age <= 18):
        bill = 7
    else:
        bill = 12

    want_photos = input("Do you want photos? Type y for yes and n for no: ")
    if (want_photos == "y"):
        bill += 3

    print(f"Here's you final bill ${bill}")

else:
    print("You can't buy the ticket. You are a midget! 😂")
