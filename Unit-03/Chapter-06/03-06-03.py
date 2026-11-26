some_num = int(input())

while some_num > 0:
    for k in range(some_num, 0, -1):
        print(k, end=' ')
    some_num -= 1
    print()
