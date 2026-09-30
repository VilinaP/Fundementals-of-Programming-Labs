print('Enter grades (Z terminates the list): ')
letter = ''
passing = 0
failing = 0
A = 0
B = 0
C = 0
D = 0
F = 0

while letter != 'Z':
    letter = input().upper()
    if letter == 'A':
        A += 1
        passing += 1
    elif letter == 'B':
        B += 1
        passing += 1
    elif letter == 'C':
        C += 1
        passing += 1
    elif letter == 'D':
        D += 1
        passing += 1
    elif letter == 'F':
        F += 1
        failing += 1
    
if (passing + failing) != 0:
    PerPass = (passing / (passing + failing)) * 100
    PerFail = (failing / (passing + failing)) * 100

    GPA = ((A*4.0)+(B*3.0)+(C*2.0)+(D*1.0)+(F*0.0))/(passing + failing)

    print(f'Student passing: {passing} ({PerPass:.2f}%)')
    print(f'Student failing: {failing} ({PerFail:.2f}%)')
    print(f'\n Class GPA: {round(GPA, 2)}')