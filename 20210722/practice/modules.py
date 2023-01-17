# modules.py
import random


def rsp(selection):
    selective = ('가위', '바위', '보')

    computer_selection = random.choice(selective)

    print(f'내 선택\t{selection}')
    print(f'컴 선택\t{computer_selection}')

    if selection == computer_selection:
        return '비겼다'
    elif (selective.index(selection) - selective.index(computer_selection)) % 3 == 1:
        return '이겼다'
    else:
        return '졌다ㅠㅠㅠ'
