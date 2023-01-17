'''
Question I.
    아이디와 비밀번호를 사용자로부터 입력받습니다.
    사용자가 입력한 아이디가 qwerty1234이고,
    사용자가 입력한 비밀번호가 asdf1234일 때,
    "승인"이라고 출력하고,
    둘 중에 하나라도 맞지 않는다면 "실패"라고 출력하는
    프로그램을 빌드하시오.
'''

ID = str(input("ID를 입력하세요. "))
password = str(input("password를 입력하세요. "))

if ID == 'qwerty1234' and password == 'asdf1234':
    print("승인")
else:
    print("실패")

