for i in range(int(input())):
    floor, rooms, count = map(int, (input().split()))

    floor_number = str(count % floor)
    room_number = f'{count // floor + 1:02d}'

    print(int(floor_number + room_number))
