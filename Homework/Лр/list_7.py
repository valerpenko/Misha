from random import randint
n = 4
multiply = 1

matrix = [[randint(1, 9) for j in range(n)] for i in range(n)]

# for i in range(n):
#     for j in range(n):
#         if i > j:
#             multiply *= matrix[i][j]

for i in range(1, n):
    for j in range(i):
        multiply *= matrix[i][j]


for el in matrix:
    print(el)

print(multiply)
