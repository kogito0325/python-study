n_and_x = list(map(int, input('N과 X를 입력하세요.\n').split()))
numbers = map(int, input().split())

for _ in numbers:
    if _ < n_and_x[1]:
        print(_, end=' ')
