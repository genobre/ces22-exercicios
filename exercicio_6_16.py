import sys

def is_factor(f,n):
    """Função para verificar se o parâmetro f é fator do parâmetro n"""
    if n % f == 0:
        return 1
    else:
        return 0

def test(did_pass):
    """Printa o resultado de um teste"""
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Teste na linha {0} ok.".format(linenum)
    else:
        msg = ("Teste na linha {0} FALHOU.".format(linenum))
    print(msg)

def test_suite():
    """Realiza um conjunto específico de testes da função is_factor"""
    test(is_factor(3,12))
    test(not is_factor(5,12))
    test(is_factor(7,14))
    test(not is_factor(7,15))
    test(is_factor(1,15))
    test(is_factor(15,15))
    test(not is_factor(25,15))

test_suite()
