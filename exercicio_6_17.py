import sys

def is_factor(f,n):
    """Função para verificar se o parâmetro f é fator do parâmetro n"""
    if n % f == 0:
        return 1
    else:
        return 0

def is_multiple(n,f):
    """Função para verificar se o parâmetro n é múltiplo do parâmetro f"""
    if is_factor(f,n):
        return 1
    else:
        return 0

#Na função is_multiple podemos chamar a função is_factor por que elas são inversas,
#isto é, se f é fator de n, então n será múltiplo de f

def test(did_pass):
    """Printa o resultado de um teste"""
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Teste na linha {0} ok.".format(linenum)
    else:
        msg = ("Teste na linha {0} FALHOU.".format(linenum))
    print(msg)

def test_suite():
    test(is_multiple(12,3))
    test(is_multiple(12,4))
    test(not is_multiple(12,5))
    test(is_multiple(12,6))
    test(not is_multiple(12,7))

test_suite()
