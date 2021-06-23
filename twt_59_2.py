# twt_59_2.py

# 1st iteration
# for _ in[I:=input]*int(I()):I();print(*I().split()[::-1])

# 2nd iteration
# for _ in[input]*int(input()):_();print(*[P[::-1]for P in _()[::-1].split()])

# 3rd iteration
# for _ in range(int(input())):
#     L = int(input())
#     A = input().split()
#     for i in range(L//2):
#         A[i], A[~i] = A[~i], A[i]
#     for i in range(L):
#         print(A[i], end=' ')
#     print()

#4th iteration
for _ in ' ' * int(input()):
    L = int(input())
    K, T = '', ''
    for c in input():
        if c == ' ':
            K = T + c + K
            T = ''
        else:
            T = T + c
    if L > 1:
        K = T + ' ' + K
    else:
        K = T
    print(K)
