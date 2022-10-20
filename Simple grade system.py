#Simple grade score
Score = input("Enter your score: ")
Mark= int(Score)
if Mark >= 70:
    print("A")
elif Mark >= 60:
    print("B")
elif Mark >= 50:
    print("C")
elif Mark >= 40:
    print("P")
else:
    print("F")