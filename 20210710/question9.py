word = input().upper()

frequency = {}  # 어떠한 문자에 대해, 그 문자가 몇 번 나왔는지 알려주는 dict
for character in word:
    if character not in frequency:
        frequency[character] = 1
    else:
        frequency[character] += 1

most_frequent = 0  # 가장 많이 나온 문자가 나온 횟수
the_character = ''  # 그 가장 많이 나온 문자
multiple = False  # 그 문자가 여러번 나왔는지 아닌지

for key in frequency.keys():
    if frequency[key] > most_frequent:
        the_character = key
        most_frequent = frequency[key]
        multiple = False
    elif frequency[key] == most_frequent:
        multiple = True

if multiple:
    print('?')
else:
    print(the_character)
