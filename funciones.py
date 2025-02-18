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

def resta (minuendo, sustraendo):
    """
    Funcion que resta dos numeros
    :param minuendo: Numero a restar
    :param sustraendo: Numero que resta
    :return: Resultado de la resta
    :exception Si se intenta restar con otro tipo de valor, devolvera 0
    """
    try:
        return minuendo - sustraendo
    except TypeError:
        print(f"No se puede restar {minuendo} con {sustraendo}")
        return 0