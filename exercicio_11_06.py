import sys

def scalar_mult(s,v):
    """Função para adicionar dois vetores de mesmo tamanho e retornar o resultado"""
    n = len(v)
    c = []
    for i in range(n):
        new_elem = s*v[i]
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
    test(scalar_mult(5,[1,2]) == [5,10])
    test(scalar_mult(3,[1,0,-1]) == [3,0,-3])
    test(scalar_mult(7,[3,0,5,11,2]) == [21,0,35,77,14])

test_suite()
