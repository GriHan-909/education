def is_prime(func):
    def wrapper(a,b,c):
        summ = func(a,b,c)
        count = 0
        for i in range(1,summ+1):
            if summ % i == 0:
                count+=1        
        if count==2:
            print('Простое')            
        else:
            print('Составное')
        return summ
    return wrapper


@is_prime
def sum_three(a,b,c):
    return a+b+c

result = sum_three(3, 3, 6)
print(result)
print()

result = sum_three(2, 3, 6)
print(result)