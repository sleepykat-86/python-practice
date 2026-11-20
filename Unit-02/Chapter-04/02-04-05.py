anual_salary = float(input())

if anual_salary <= 55867:
    print(1)
elif 55867 < anual_salary <= 111733:
    print(2)
elif 111733 < anual_salary <= 173205:
    print(3)
elif 173205 < anual_salary <= 246752:
    print(4)
elif anual_salary > 246752:
    print(5)