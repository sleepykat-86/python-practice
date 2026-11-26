some_num = int(input())

for colum in range(1, some_num + 1):
    for row in range(1, some_num + 1):
        print(colum * row, end=' ')
    print()
