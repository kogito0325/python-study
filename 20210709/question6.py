file = open('./numbers.txt', 'r')

'''
new_list = []

for i in file.read().split():
    new_list.append(int(i))
for i in sorted(new_list):
    print(i)
print()
'''

for i in sorted(map(int, file.read().split())):
    print(i)

file.close()
