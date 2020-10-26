# segitiga siku-siku/ right left triangle
x = 7
# Left triangle
for i in range(x):
    for j in range(i):
        print('*', end='')
    print('')

# Reverse left triangle
for i in range(x, 0, -1):
    for j in range(i):
        print('*', end='')
    print('')


print('\n')


# Diamond
space = x
for i in range(0, x):
    for j in range(0, space):
        print(end=" ")
    space -= 1
    for k in range(0, i+1):
        print("* ", end="")
    print("")
