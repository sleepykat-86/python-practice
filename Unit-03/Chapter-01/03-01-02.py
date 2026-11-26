name = input()

while name != 'A girl has no name':
    print(f'hello {name}! \nNEXT!')
    name = input()

if name == 'A girl has no name':
    print('*sweats profusely*')

#better solution
#while True:
#    if name == 'A girl has no name':
#       break
#    print(f'hello {name} \nNEXT')
#print('*sweats profusely*')