
sub1=float(input("enter the marks of subject 1: "))
sub2=float(input("enter the marks of subject 2: "))
sub3=float(input("enter the marks of subject 3: "))
sub4=float(input("enter the marks of subject 4: "))
sub5=float(input("enter the marks of subject 5: "))
total_sum=sub1+sub2+sub3+sub4+sub5
percentage=( total_sum/500)*100
print("the total marks is: ",total_sum)
print("the percentage is: ",percentage)
if  percentage >=40 :
    print("pass")
else:
    print("fail")
    