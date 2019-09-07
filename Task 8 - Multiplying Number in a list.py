num=input("Enter Numbers to be added seperated with comma \n");
lst=num.split(',');
add=[];
r=1;
for i in lst:
    i=int(i);
    add.append(i);
    r=r*i;
print(add);
print(r);

