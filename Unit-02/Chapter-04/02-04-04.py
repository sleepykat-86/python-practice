N = int(input())

if N % 3 == 0 == N % 5:
    print('Fizz Buzz')
elif N % 3 == 0:
    print('Fizz')
elif N % 5 == 0:
    print('Buzz')
else:
    print(N)