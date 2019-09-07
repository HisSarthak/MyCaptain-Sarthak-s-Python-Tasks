print("Enter 3 Sides of Triangle");
s1=input("Enter Side 1: ");
s2=input("Enter Side 2: ");
s3=input("Enter Side 3: ");

if(s1.isnumeric()==False and s2.isnumeric()==False and s3.isnumeric()==False):
    print("Sides should be a number");
else:
    if(s1==s2==s3):
        print("It is an EQUILATERAL Triangle");
    elif(s1==s2!=s3 or s2==s3!=s1 or s3==s1!=s2):
        print("It is an ISOSCELES Triangle");
    elif(s1!=s2 and s2!=s3 and s3!=s1):
        print("It is an SCALENE Triangle");
    else:
        print("Side not entered properly");

