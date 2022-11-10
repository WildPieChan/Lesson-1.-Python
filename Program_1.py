# Write a program that accepts a digit indicating the day of the week as input 
# and checks whether this day is a weekend.
n = 0
while (n > 7) or (n < 1):
    n = int(input("~Computer~ Enter number of the day of the week: "))

print("~Computer~ Is it a weekend?")
if n == 7 or n == 6:
    print("~Computer~ Yes")
else:
    print("~Computer~ No")
