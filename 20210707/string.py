# string, str, 문자열

a = 'Hello, '
b = 'Shtelo!'

c = a + b
d = b + a

print(c)
print(d)
print()

print(a * 1)
print(b * 2)
print(c * 3)
print()

print(c[3])		# indexing
print(c[-1])		# indexing
print(c[3:10])		# slicing
print(c[3:])		# slicing
print(c[:10])		# slicing
print(c[::2])		# slicing & jumping
print(c[::-1])		# reverse sorting
print()

print(c[3] == 'l')
print('Shtelo' in c)
print('shtelo' not in c)

print('----------------------------')

'''
.join()
.split()	# 문자열을 seperator를 기준으로 쪼갬
.replace()	# 문자열 안의 일부를 다른 것으로 교체
.strip()	# 문자열 양 끝의 whitespace를 제거
.lstrip()	# 문자열 왼쪽의 "
.rstrip()	# 문자열 오른쪽의 "
.upper()
.lower()
'''


