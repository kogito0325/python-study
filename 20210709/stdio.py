# 파일 입출력: fileio
# 정규 입출력: stdio

from os.path import isfile


FILE_PATH = './saves.txt'

if isfile(FILE_PATH):
    file = open(FILE_PATH, 'r')
    score = int(file.read())
    file.close()
else:
    score = 0

while True:
    print(f'현재 점수는 {score}점입니다.')

    input()
    score += 1

    file = open(FILE_PATH, 'w')
    file.write(str(score))
    file.close()
