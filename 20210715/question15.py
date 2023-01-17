num, mul = map(int, input().split())

pattern = ''

while len(pattern) < 100:
    if num // mul == 0:
        if '.' not in pattern:
            if pattern == '':
                pattern += '0'
            pattern += '.'
        num *= 10
    else:
        pattern += str(num // mul)
        if num % mul == 0:
            break
        num %= mul

print(pattern)
