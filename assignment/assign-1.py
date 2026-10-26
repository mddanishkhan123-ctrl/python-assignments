name=input("Enter your name: ")
monthly_income=float(input("Enter your monthly income: "))
rent=float(input("Enter your monthly rent: "))
food_expenses=float(input("Enter your monthly food expenses: "))
travel_expenses=float(input("Enter your monthly travel expenses: "))
entertainment_expenses=float(input("Enter your monthly entertainment expenses: "))
other_expenses=float(input("Enter your other monthly expenses: "))
total_expenses=rent+food_expenses+travel_expenses+entertainment_expenses
remaining_money=monthly_income-total_expenses
savings_percentage=(remaining_money/monthly_income)*100
daily_expenses=total_expenses/30
weekly_expenses=total_expenses/4
saving_target=float(input("Enter your saving target: "))
print(f"""my name is: {name}\n
my salary is: {monthly_income}\n
my total_expenses is: {total_expenses}\n
my savings_money is: {remaining_money}\n
my savings_percentage is: {savings_percentage}\n
my daily_expenses is: {daily_expenses}\n
my weekly_expenses is: {weekly_expenses}\n
my saving_target is: {saving_target}\n
""")