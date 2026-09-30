employee1 = int(input('Please enter this month\'s sales for employee 1: '))
employee2 = int(input('Please enter this month\'s sales for employee 2: '))
employee3 = int(input('Please enter this month\'s sales for employee 3: '))
employee4 = int(input('Please enter this month\'s sales for employee 4: '))
employee5 = int(input('Please enter this month\'s sales for employee 5: '))
employee6 = int(input('Please enter this month\'s sales for employee 6: '))
employee7 = int(input('Please enter this month\'s sales for employee 7: '))
employee8 = int(input('Please enter this month\'s sales for employee 8: '))

def chart(num):
    i = num // 1000
    return i

print('Sales for the month \n (Each * = $1,000)')

print(f'Employee 1: |{'*'*chart(employee1)}')   
print(f'Employee 2: |{'*'*chart(employee2)}')
print(f'Employee 3: |{'*'*chart(employee3)}')
print(f'Employee 4: |{'*'*chart(employee4)}')
print(f'Employee 5: |{'*'*chart(employee5)}')
print(f'Employee 6: |{'*'*chart(employee6)}')
print(f'Employee 7: |{'*'*chart(employee7)}')
print(f'Employee 8: |{'*'*chart(employee8)}')


