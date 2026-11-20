A = input()
B = input()
C = input()

if A == B == C:
    height = A
elif A >= B and A >= C:
    height = A
elif B >= A and B >= C:
    height = B
elif C >= A and C >= B:
    height = C

print(height)