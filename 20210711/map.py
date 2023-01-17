# a, b = map(int, input().split())

# a, b = input().split()
# a, b = int(a), int(b)

names = ['동해물과', '백두산이', '마르고', '닳도록']

ideal_names = list(map(lambda x: x[0], names))
print(ideal_names)
