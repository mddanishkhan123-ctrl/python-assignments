correct_password = "12345"
attemt =4
for i in range(attemt):
        password = input("Enter the password: ")
        if password == correct_password:
            print("Password correct!")
            break
        else:
            print("Incorrect password. Please try again.")
else:
        print("Maximum attempts reached. Access denied.")