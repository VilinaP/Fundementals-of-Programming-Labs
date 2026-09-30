gender = input('Please enter your biological gender (female or male): ').lower()
if gender != 'male' and gender != 'female':
    print('\nGender not recognized; please rerun the program.')
    quit()

weightPound = float(input('Please enter your weight in pounds: '))
heightFeet = input('Please enter your height in feet and inches separated by a space: ')
age = int(input('Please enter your age in years: '))
print('Actuvity levels: \n \t 1 sedentary \n \t 2 somewhat active (exercise occasionally) \n \t 3 active (exercise 3 or 4 days a week) \n \t 4 highly active (exercise everyday)')
activity = input('Please enter your activity level (1, 2, 3, or 4): ')
if activity != '1' and activity != '2' and activity != '3' and activity != '4':
    print('Activity level must be one of 1, 2, 3, or 4; please rerun the program.')
    quit()

weightKg = weightPound * 0.453529

feet = float(heightFeet.split()[0])
inches = float(heightFeet.split()[1])
heightCm = (feet*12 + inches) * 2.54

BMR = 0

if gender == 'male':
    BMR = (10*weightKg) + (6.25*heightCm) - (5*age) + 5
elif gender == 'female':
    BMR = (10*weightKg) + (6.25*heightCm) - (5*age) - 161

if activity == '1':
    BMR = BMR + (BMR*0.2)
elif activity == '2':
    BMR = BMR + (BMR*0.3)
elif activity == '3':
    BMR = BMR + (BMR*0.4)
elif activity == '4':
    BMR = BMR + (BMR*0.5)

print(f'\nTotal energy required per day is {(BMR):.1f} kcals.')
print(f'To maintain your weight, you must consume the equivalent of {(BMR/69):.1f} slices of whole wheat bread per day.')