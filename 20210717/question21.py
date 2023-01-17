num = input()

num = '0' * (4 - len(num)) + num
result = ''

turn = 0
for i in num:
    turn += 1
    if turn == 1:
        result += 'M' * int(i)
    elif turn == 2:
        if int(i) < 4:
            result += 'C' * int(i)
        elif int(i) == 4:
            result += 'CD'
        elif int(i) < 9:
            result += 'D' + 'C' * (int(i) - 5)
        else:
            result += 'CM'
    elif turn == 3:
        if int(i) < 4:
            result += 'X' * int(i)
        elif int(i) == 4:
            result += 'XL'
        elif int(i) < 9:
            result += 'L' + 'X' * (int(i) - 5)
        else:
            result += 'XC'
    elif turn == 4:
        if int(i) < 4:
            result += 'I' * int(i)
        elif int(i) == 4:
            result += 'IV'
        elif int(i) < 9:
            result += 'V' + 'I' * (int(i) - 5)
        else:
            result += 'IX'

print(result)
