num=int(input("enter a four-digit number: "))
sum=0
while num!=0:
    rem=num%10
    sum=sum+rem
    num=num//10
print("the sum of digits is: ",sum)