# condition, 조건
# 흐름 제어, flow control

a = 3
b = 7

if a < b:
  print("a가 b보다 작다.")
elif a > b:
  print("a가 b보다 크다.")
else:
  print("a와 b가 같다.")

print("---------------------------")

answer = int(input("당신의 점수는?\n"))

if answer >= 90:
    print('A')
elif answer >= 80:
    print('B')
elif answer >= 70:
    print('C')
elif answer >= 60:
    print('D')
else:
    print('F')
