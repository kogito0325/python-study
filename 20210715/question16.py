num = int(input())

for i in range(num):
    print(' ' * (num - (i + 1)), end='')
    print('*' * (i + 1))
