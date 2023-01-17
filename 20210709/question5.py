turn = 0
whole_n = 0

while True:
    turn += 1
    a = int(input())
    if a == 0:
        break
    else:
        whole_n += a
        print(whole_n / turn)

