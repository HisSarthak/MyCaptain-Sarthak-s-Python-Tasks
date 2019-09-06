w = input('Enter a list of things seperated by comma we will give u the maximum number of characters in longest number \n');
lst=w.split(',');
j=[];
for i in lst:
	j.append(len(i));
print(max(j));
