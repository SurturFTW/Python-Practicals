sub1 = int(input("Enter marks of English: "))
sub2 = int(input("Enter marks of Maths: "))
sub3 = int(input("Enter marks of Science: "))

avg = sub1 + sub2 + sub3 / 3
if avg >= 50:
    print("You got A grade.")

elif 40 <= avg < 50:
    print("You got B grade.")

elif 30 <= avg < 40:
    print("You got C grade.")

elif 20 <= avg < 20:
    print("You got D grade.")

else:
    print("You got failed.")
