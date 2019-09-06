w = input("Enter a list of things seperated with comma and i will show the list item with the longest characters \n");
lst = w.split(',')
j=[];
for i in lst:
    j.append(len(i));
    
print(max(j));
