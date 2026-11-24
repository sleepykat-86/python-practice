#unfinished

user_str = input()

if ' ' in user_str:
    for index in range(len(user_str)):
        if user_str[index] == ' ':
            print(index, end=', ')
else:
    print('no spaces found')
