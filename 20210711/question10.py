results = []

for _ in range(int(input())):
    number, word = input().split()
    number = int(number)
    output = ''
    for letter in word:
        output += letter * number
    results.append(output)
for result in results:
    print(result)
