subject1=int(input("Enter marks of subject 1: "))
subject2=int(input("Enter marks of subject 2: "))
subject3=int(input("Enter marks of subject 3: "))
total_marks=subject1+subject2+subject3
percentage=(total_marks/300)*100
if percentage>=40: 
    print("You have passed.")
else:
    print("You have failed.")