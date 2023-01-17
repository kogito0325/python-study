# dictionary, dict

dictionary = {
    '안녕': 'hello',
    '밥': 'rice',
    '사전': {
        '사': 4,
        '전': 'war'
    }
}

print(dictionary)

dictionary['값'] = 'value'
print(dictionary)

del dictionary['사전']
print(dictionary)
print()

print(bool(dictionary))
print(bool({}))
print()

print('안녕' in dictionary)
print('hello' in dictionary)
print()

for key, value in dictionary.items():
    print(key, ':', value)
print()

print(dictionary.keys())
print(dictionary.values())
