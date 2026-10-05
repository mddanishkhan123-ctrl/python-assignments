weight=float(input("enter your weight in kg: "))
height_foot=float(input("enter your height in feet: "))
height_in_meter=height_foot*0.3048
bmi=weight/( height_in_meter**2)
print("your BMI is: ",bmi)
if bmi<18.5:
    print(" you areunder weight..")
elif bmi>=18.5 and bmi<24.9:
    print("You have a normal weight.")
elif bmi>=25 and bmi<29.9:
    print("you are over weight..")
else:
    print("You are obese.")