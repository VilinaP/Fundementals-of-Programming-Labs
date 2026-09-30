
# total = round(int(float(input('Enter the amount of money (no dollar sign in front): '))*100))


# bills20 = total // 2000
# total = total % 2000

# bills10 = total // 1000
# total = total % 1000

# bills5 = total // 500
# total = total % 500

# bills1 = total // 100
# total = total % 100
   
# cents25 = total // 25
# total = total % 25

# cents10 = total // 10
# total = total % 10

# cents5 = total // 5

# cents1 = total % 5




# print('Twenties: ' ,bills20)
# print('Tens: ' ,bills10)
# print('Fives: ' ,bills5)
# print('Ones: ' ,bills1)
# print('Quarters: ' ,cents25)
# print('Dimes: ' ,cents10)
# print('Nicles: ' ,cents5)
# print('Pennies: ' ,cents1)

stop = 17
total = 0
for number in [6, 7, 2, 6, 2, 7]:
    print(number, end=" ")
    total += number
    if total > stop:
        print("*")
        break
else:
    print(f"/ {total}")
print("done")