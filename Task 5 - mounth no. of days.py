month = input('Please Enter a Name of a Month \n');

if (month == 'January' or month == 'March' or month == 'May' or month == 'July' or month == 'August' or month == 'October' or month == 'December'):
    nod = 31;
    print('Name of Month: {}'.format(month));
    print('No. of Days: {}'.format(nod));
elif (month == 'April' or month == 'June' or month == 'September' or month == 'November'):
    nod = 30;
    print('Name of Month: {}'.format(month));
    print('No. of Days: {}'.format(nod));
elif (month == 'February'):
    nod = 29;
    print('Name of Month: {}'.format(month));
    print('No. of Days: {}'.format(nod));
else :
    print('Incorect Month Name');
