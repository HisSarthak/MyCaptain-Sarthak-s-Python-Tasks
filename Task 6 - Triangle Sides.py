print('Enter 3 sides of a triangle \n');
s1=input('Side 1 is : ');
s2=input('Side 2 is : ');
s3=input('Side 3 is : ');

if (s1==s2==s3):
	print('It is an EQUILATERAL Triangle');
elif(s1==s2!=s3 or s2==s3!=s1 or s3==s1!=s2):
	print('It is an ISOSCELES Triangle');
elif(s1!=s2 and s2!=s3 and s3!=s1):
	print('It is an SCALENE Triangle');
else :
	print('Side not entered properly');