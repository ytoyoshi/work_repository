N = int(input())
A = [int(input()) for _ in range(N)]

yesterdaySales = A[0]
for i in range(1,N):
    if A[i] ==  yesterdaySales:
        print('stay')
    if A[i] > yesterdaySales:
        print(f'up {A[i]-yesterdaySales}')
    if A[i] < yesterdaySales:
        print(f'down {yesterdaySales-A[i]}')
    yesterdaySales = A[i]