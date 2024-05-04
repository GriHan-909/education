num = list(map(int, range(3, 21)))
my_list = []

for k in num:
    for i in range(1, k+1):
        for j in range(i, k+1):
            if k % (i+j) == 0 and i != j:
                num_str = str(i) + str(j)
                my_list.append(num_str)
    result = ''.join(my_list)
    print(f'{k} - {result}')
    my_list = []
