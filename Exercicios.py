''' 
Exercício de Recursividade

Exercício 01 - O máximo divisor comum (MDC) de dos números inteiros x e y
é o maior inteiro que é divisível por x e y, e pode pode ser calculado de
acordo com a definição abaixo. Escreva uma função recursiva em python que
calcule o MDC de dois números inteiros positivos.
'''


def mdc(x, y):
    if x >= y and x % y == 0:
        return y
    elif x < y:
        return mdc(y, x)
    else:
        return mdc(y, x % y)


'''
Exercício 02 - Pode-se calcular o resto da divisão de dois números
inteiros utilizando a definição abaixo. Escreva uma função recursiva
em python que calcule o resto da divisão entre dois números inteiros
positivos.
'''


def resto(x, y):
    if x < y:
        return x
    elif x == y:
        return 0
    elif x > y:
        return resto(x - y, y)


'''
Exercicio 03 - Escreva uma função recursiva em python que recebe
como entrada um número inteiro positivo N e retorna o somatório de
todos os números inteiros no intervalo de 1 a N.
'''


def somatorio(n):
    if n <= 1:
        return 1
    else:
        return n + somatorio(n - 1)


'''
Exercício 04 - Escreva uma função recursiva em python que
receba dois números inteiros A e B, e retorna o resultado de AB.
'''


def elevado(a, b):
    if a == 0:
        return 0
    elif b == 0:
        return 1
    else:
        return a * elevado(a, b-1)


'''
Exercício 05 - Escreva uma versão recursiva do algoritmo de
busca linear. O algoritmo deve receber como entrada uma lista e
uma chave de busca, e retornar o índice da posição onde a chave
de busca foi localizada, ou -1, caso não a localize na lista.
'''


def busca(lista, item):
    if len(lista) == 1:
        if lista[0] == item:
            return True
        else:
            return False
    elif lista[0] == item:
        return True
    else:
        return busca(lista[1:], item)


print("\nEXECUÇÃO DOS TESTES\n")


def test_01a_mdc():
    try:
        assert mdc(12, 18) == 6, 'MDC deve ser 6'
        assert mdc(6, 12) == 6, 'MDC deve ser 6'
        assert mdc(12, 20) == 4, 'MDC deve ser 4'
        assert mdc(20, 24) == 4, 'MDC deve ser 4'
        print("ACERTO: test_01a_mdc")
    except AssertionError as erro:
        print("Erro test_01a_mdc: ", erro)


def test_01b_mdc():
    try:
        assert mdc(18, 12) == 6, 'MDC deve ser 6'
        assert mdc(12, 6) == 6, 'MDC deve ser 6'
        assert mdc(20, 12) == 4, 'MDC deve ser 4'
        assert mdc(24, 20) == 4, 'MDC deve ser 4'
        print("ACERTO: test_01b_mdc")
    except AssertionError as erro:
        print("Erro test_01b_mdc: ", erro)


def test_02a_resto():
    try:
        assert resto(5, 2) == 1, 'Resto deve ser 1'
        assert resto(4, 2) == 0, 'Resto deve ser 0'
        assert resto(8, 5) == 3, 'Resto deve ser 3'
        assert resto(10, 4) == 2, 'Resto deve ser 2'
        print("ACERTO: test_02a_resto")
    except AssertionError as erro:
        print("Erro test_02a_resto: ", erro)


def test_02b_resto():
    try:
        assert resto(2, 2) == 0, 'Resto deve ser 0'
        assert resto(3, 3) == 0, 'Resto deve ser 0'
        assert resto(4, 4) == 0, 'Resto deve ser 0'
        assert resto(5, 5) == 0, 'Resto deve ser 0'
        print("ACERTO: test_02b_resto")
    except AssertionError as erro:
        print("Erro test_02b_resto: ", erro)


def test_03a_somatorio():
    try:
        assert somatorio(5) == 15, 'Somatório deve ser 15'
        assert somatorio(4) == 10, 'Somatório deve ser 10'
        assert somatorio(6) == 21, 'Somatório deve ser 21'
        assert somatorio(3) == 6, 'Somatório deve ser 6'
        print("ACERTO: test_03a_somatorio")
    except AssertionError as erro:
        print("Erro test_03a_somatorio: ", erro)


def test_03b_somatorio():
    try:
        assert somatorio(1) == 1, 'Somatório deve ser 1'
        assert somatorio(0) == 1, 'Somatório deve ser 1'
        assert somatorio(-1) == 1, 'Somatório deve ser 1'
        assert somatorio(-2) == 1, 'Somatório deve ser 1'
        print("ACERTO: test_03b_somatorio")
    except AssertionError as erro:
        print("Erro test_03b_somatorio: ", erro)


def test_04_elevado():
    try:
        assert elevado(2, 3) == 8, 'Resultado deve ser 8'
        assert elevado(3, 2) == 9, 'Resultado deve ser 9'
        assert elevado(4, 2) == 16, 'Resultado deve ser 16'
        assert elevado(2, 4) == 16, 'Resultado deve ser 6'
        print("ACERTO: test_04_elevado")
    except AssertionError as erro:
        print("Erro test_04_elevado: ", erro)


def test_05a_busca():
    try:
        assert busca([1, 3, 4, 6], 3) is True, 'Resultado deve ser True'
        assert busca([2, 4, 6, 8], 2) is True, 'Resultado deve ser True'
        assert busca([1, 3, 4, 5], 3) is True, 'Resultado deve ser True'
        print("ACERTO: test_05a_busca")
    except AssertionError as erro:
        print("Erro test_05a_busca: ", erro)


def test_05b_busca():
    try:
        assert busca([1, 3, 4, 6], 7) is False, 'Resultado deve ser False'
        assert busca([2, 4, 6, 8], 3) is False, 'Resultado deve ser False'
        assert busca([1, 3, 4, 5], 8) is False, 'Resultado deve ser False'
        print("ACERTO: test_05b_busca")
    except AssertionError as erro:
        print("Erro test_05b_busca: ", erro)


test_01a_mdc()
test_01b_mdc()
test_02a_resto()
test_02b_resto()
test_03a_somatorio()
test_03b_somatorio()
test_04_elevado()
test_05a_busca()
test_05b_busca()
