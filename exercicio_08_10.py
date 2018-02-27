import sys

def reverse(pali):
    """Função que retorna o reverso da palavra que recebeu como input"""
    n = len(pali)
    i = 0
    word = ""
    for i in range (0,n):
        x = pali[n-1-i]
        word += x
    return word

def is_palindrome(palavra):
    teste = palavra.lower()
    reversa = reverse(teste)
    if teste == reversa:
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
    test(is_palindrome("abba"))
    test(not is_palindrome("abab"))
    test(is_palindrome("tenet"))
    test(not is_palindrome("banana"))
    test(is_palindrome("straw warts"))
    test(is_palindrome("a"))

test_suite()
