#unfinished

pyramid1 = int(input())

for space_num in range(0, pyramid1):
    space = ' ' * space_num

for i in range(pyramid1, 0,  -1):
    pyramid = (i - 1) * '10' + '1'

print(space + pyramid)


