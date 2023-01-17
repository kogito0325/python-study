num = input()

for i in range(1, 1000001):
    if i < 10:
        division_sum = i + i
    elif i < 100:
        division_sum = i + int(str(i)[0]) + int(str(i)[1])
    elif i < 1000:
        division_sum = i + int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2])
    elif i < 10000:
        division_sum = i + int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2]) + int(str(i)[3])
    elif i < 100000:
        division_sum = i + int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2]) + int(str(i)[3]) + int(str(i)[4])
    elif i < 1000000:
        division_sum = i + int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2]) + int(str(i)[3]) + int(str(i)[4]) \
                       + int(str(i)[5])
    else:
        division_sum = i + int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2]) + int(str(i)[3]) + int(str(i)[4]) \
                       + int(str(i)[5]) + int(str(i)[6])
    if division_sum == int(num):
        print(i)
        quit()

print(0)
