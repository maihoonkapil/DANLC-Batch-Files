prime = 0
Num = 2 

while prime < 10:
    
    is_prime = True
    for i in range(2, Num):

        if Num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(Num, end=" ")
        prime += 1
    
    Num += 1
