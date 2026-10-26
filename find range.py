num=int(input("Enter a number: "))
low=int(input("Enter the lower range: "))
high=int(input("Enter the higher range: "))
if low <= num <= high:
    print(num, "is in the range.")
else:
    print(num, "is not in the range.")