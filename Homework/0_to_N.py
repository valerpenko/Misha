n = int(input())
n_new = 0

while n_new < n:
    if n_new != 0 and n_new * 4 <= n:
        n_new *= 4
        print('*4')
    else:
        n_new += 1
        print('1')
