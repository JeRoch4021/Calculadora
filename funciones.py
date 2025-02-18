def sum(*nums)->int:
    sum = 0
    for num in nums:
        sum += num
    return sum

def mult(*nums)->float:
    mult = 0
    for num in nums:
        mult *= num
    return mult
