n=input("Enter Numbers to be added seperated with comma \n");
lst=n.split(',');
odd=0;
even=0;
r=0;
add=[];

for i in lst:
    i=int(i);
    add.append(i);

for j in add:
    if add[r] %2 == 0:
        even=even+1;
    else:
        odd=odd+1;
    r=r+1;


print("Number of Even's:",even);
print("Number of Odd's",odd);
