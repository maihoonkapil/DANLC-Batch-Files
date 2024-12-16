start = 1  
end = 1000  

for num in range(start, end + 1):

    str_num = str(num)
    num_digits = len(str_num) 
    sum_of_powers = 0  

    for digit in str_num:
        sum_of_powers += int(digit) ** num_digits  
 
    if sum_of_powers == num:
        print(num)  