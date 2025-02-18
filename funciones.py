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

def raiz(num, exp=2):
    """
    Funcion que calcula la raiz de un numero
    :param num: Numero a calcular la raiz cuadrada
    :param exp: Exponente de la raiz cuadrada
    :return: Resultado de la raiz cuadrada
    :exception Si se intenta calcular la raiz de un numero negativo, devolvera 0
    """
    try:
        return num ** (1/exp)
    except TypeError:
        print(f"No se puede calcular la raiz cuadrada de {num} con exponente {exp}")
        return 0