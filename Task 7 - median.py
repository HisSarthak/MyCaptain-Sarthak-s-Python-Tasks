print("Enter 3 numbers to find the median");
num1=input("Enter Number 1: ");
num2=input("Enter Number 2: ");
num3=input("Enter Number 3: ");

if num1>num2:
    if num1<num3:
        print("{} is the median".format(num1));
    elif num2>num3:
        print("{} is the median".format(num2));
    else:
        print("{} is the median".format(num3));
elif num1<num2:
    if num1>num3:
        print("{} is the median".format(num1));
    elif num2>num3:
        print("{} is the median".format(num3));
    else:
        print("{} is the median".format(num2));
else:
    print("Numbers should be different");


