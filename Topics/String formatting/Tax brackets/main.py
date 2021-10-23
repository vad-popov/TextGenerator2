income = int(input())
if income < 0:
    print('Please enter positive value')
elif income < 15528:
    percent = 0
elif income < 42708:
    percent = 15 / 100
elif income < 132407:
    percent = 25 / 100
else:
    percent = 28 / 100
calculated_tax = income * percent
print(f"The tax for {income} is {percent:.0%}. That is {calculated_tax:.0f} dollars!")
