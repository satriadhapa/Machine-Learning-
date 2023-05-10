print("CAR ENSURANCE")
print("=" * 13)

print("male", "or" , "female")
gender = input("What is your gender? ")
gender = gender.lower()

if gender == "male":
    print("Your Male")
    age = int(input("What is your age? "))
    if age >= 26:
        print("Your Ensurance 23%")
        presentage = 23
    else:
        print("Your Ensurance 9%")
        persentage = 9
elif gender == "female":
    print("Your Female")
    sport = input("do you like Sport? yes or no? ")
    sport = sport.lower()
    if sport == "yes":
        print("Your Ensurance 21%")
    elif sport == "no":
        print("Your Ensurance 10%")
    else:
        print("Unknown Ensurance")
    
else:
    print("Wrong Format")
    
market_price = 