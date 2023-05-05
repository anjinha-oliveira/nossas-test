"""
Resolva o problema de programação: Dado um array de números inteiros, encontre se o array possui algum número duplicado. Sua função deve retornar “true” se algum número aparecer ao menos duas vezes no array, e ela deve retornar “false” se todos os números forem distintos.
"""


"""
Resolva o problema de programação: Dado um array de números inteiros, encontre se o array possui algum número duplicado. Sua função deve retornar “true” se algum número aparecer ao menos duas vezes no array, e ela deve retornar “false” se todos os números forem distintos.
*
"""

def contem_duplicados(numeros):
    for numero in numeros:
        ocorrencias = numeros.count(numero)
        if ocorrencias >= 2:
            return True

    return False