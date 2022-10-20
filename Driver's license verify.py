Year = input("Type Year of birth: ")
Age = 2022 - int(Year)
print(Age)
if Age > 60:
    print("Please retire")
elif Age <= 59:
    print("You are qualified to be issued driver's license")

else:
    print("Too young")