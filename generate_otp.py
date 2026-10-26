import random
otp=random.randint(1000,9999)
print("Your OTP is:", otp)
user_otp=int(input("Enter the OTP: "))
while True:
    if otp==user_otp:
        print("login successful")
        break
    user_otp=int(input("Enter the OTP: "))