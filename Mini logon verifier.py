Username = input ("Username: ")

if Username == "":
    print("You didn't enter a username")
else:
    print("Welcome" + " " + Username)
Pin = input ("Pin: ")
if len(Pin) != 4:
    print ("pin must be 4 digits")
else:
    print("Successful")