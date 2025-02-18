def sum(*nums)->float:
    sum = 0
    for num in nums:
        sum += num
    return sum

def pow(base, exp)->float:
    pow = 1
    for i in range(exp):
        pow *= base 

def mult(*nums)->float:
    mult = 0
    for num in nums:
        mult *= num
    return mult
