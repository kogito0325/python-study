"""
숫자가 소수인지 아닌지를 알려주는 프로그램
소수이면 "prime", 합성수 또는 1이면 "not prime"
"""

"""
def is_prime():
    n = int(input('Enter any number\n'))

    for i in range(n):
        number = int(input())
        prime = True
        for j in range(2, number):
            if number % j == 0:
                prime = False
                break
        if prime and number != 1:
            print('prime')
        else:
            print('not prime')
    print()


while True:
    is_prime()
"""

n = int(input())


def is_prime():
    prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            prime = False
            break

    if prime and number != 1:
        print('prime')
    else:
        print('not prime')


for i in range(n):
    number = int(input())

    is_prime()
