start = 2
multiplyer = 1

while True:
    print(f'{start} * {multiplyer} = {start * multiplyer}')
    multiplyer += 1
    if multiplyer >= 10:
        multiplyer = 1
        start += 1
        if start == 10:
            break
        print()
