import sys

def add_vectors(a,b):
    """Função para adicionar dois vetores de mesmo tamanho e retornar o resultado"""
    n = len(a)
    c = []
    for i in range(n):
        new_elem = a[i] + b[i]
        c.append(new_elem)
    return c

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
    test(add_vectors([1,1],[1,1]) == [2,2])
    test(add_vectors([1,2],[1,4]) == [2,6])
    test(add_vectors([1,2,1],[1,4,3]) == [2,6,4])

test_suite()
