# Write a program that shows the range of possible coordinates 
# of points in this quarter (x and y) according to the given number of quarters.

quarter = int(input('Enter number of quarter: '))

if quarter == 1:
    print('x > 0, y > 0')
elif quarter == 2:
    print('x < 0, y > 0')
elif quarter == 3:
    print('x < 0, y < 0')
elif quarter == 4:
    print('x > 0, y < 0')
else:
    print('There is only four quarters')
    print('From 1 to 4')