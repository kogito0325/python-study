numbers = map(int, input().split())

correct = []
for i in numbers:
    correct.append(i)

if correct == [8, 7, 6, 5, 4, 3, 2, 1]:
    print('descending')
elif correct == [1, 2, 3, 4, 5, 6, 7, 8]:
    print('ascending')
else:
    print('mixed')
