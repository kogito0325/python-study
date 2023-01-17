a = int(input())
b = int(input())
c = int(input())

big = a * b * c

for number in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
    count = 0
    for i in str(big):
        if i == number:
            count += 1
    print(count)
