sub1 = float(input("enter marks for sub 1:  "))
sub2 = float(input("enter marks for sub 1:  "))
sub3 = float(input("enter marks for sub 1:  "))
sub4 = float(input("enter marks for sub 1:  "))
sub5 = float(input("enter marks for sub 1:  "))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total / 500) * 100

print("\npercentage: ", percentage,"%")

if percentage >= 75:
    print("Grade: distinction")
elif percentage >= 65:
    print("Grade: 1st division")
elif percentage >= 40:
    print("Grade: 2nd division")
else:
    print("Grade: 3rd division")