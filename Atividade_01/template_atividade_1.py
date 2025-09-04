'''
Informações sobre o como fazer a atividade:

* O script deverá ter o formato: seunome_sobrenome.py (sem espaços)
  Para pessoas com multiplos sobrenomes, colocar apenas o ultimo.
  Caracteres com acentos devem ser substituidos pelo equivalente sem acento.
  
* Não adicione nada no script fora dos locais onde está escrito :
    ### Seu código inicia aqui ###	
    print("Olá mundo!")
    ### Seu código termina aqui ###
    
'''
import numpy as np

### Seu código inicia aqui ###

nome = 'gustavo_voltani_von_atzingen' # # coloque aqui o nome completo sem espaços (colocar '_' entre as palavras e.g. gustavo_voltani_von_atzingen) no formato de uma string
email = 'gustavo.von.atzingen@gmail.com' # Coloque o seu email aqui no formato string como no exemplo

### Seu código termina aqui ###


# Exemplo 1 já resolvido
def progressao_aritmetica(a1, r, n):
    '''
    Crie uma função que recebe um número inteiro a1, a razão de progressão aritmética r 
    e um número inteiro n > 1 e retorna uma lista com os n primeiros termos da progressão aritmética
    
    PA: https://pt.wikipedia.org/wiki/Progress%C3%A3o_aritm%C3%A9tica 
    
    Test
    -----------
    >>> progressao_aritmetica(1, 2, 4)
    [1, 3, 5, 7]
    ''' 
    lista_pa = []
    ### Seu código inicia aqui ###	
    # Este exemplo já está resolvido
    lista_pa.append(a1) 
    for i in range(n-1):
        lista_pa.append(lista_pa[-1] + r)
    ### Seu código termina aqui ###
    return lista_pa

def soma_pa(a1, r, n):
    '''
    Crie uma função que recebe um número inteiro a1, a razão de progressão aritmética r 
    e um número inteiro n > 1 e retorna a soma dos n primeiros termos da progressão aritmética
    
    PA: https://pt.wikipedia.org/wiki/Progress%C3%A3o_aritm%C3%A9tica 
    
    Return
    -----------
    soma: int
    
    Test
    -----------
    >>> soma_pa(1, 2, 4)
    16
    '''
    soma = 0
    ### Seu código inicia aqui ###	

    ### Seu código termina aqui ###
    return soma

def progressao_geometrica(a1, q, n):
    '''
    Crie uma função que recebe um número inteiro a1, a razão de progressão geométrica q 
    e um número inteiro n e retorna uma lista com os n primeiros termos da progressão geométrica
    
    https://pt.wikipedia.org/wiki/Progress%C3%A3o_geom%C3%A9trica 
    
    Test
    -----------
    >>> progressao_geometrica(1, 2, 4)
    [1, 2, 4, 8]
    >>> progressao_geometrica(1, 2, 3)
    [1, 2, 4]
    '''
    pg = []
    ### Seu código inicia aqui ###	
    
    ### Seu código termina aqui ###
    return pg

def soma_pg(a1, q, n):
    '''
    Crie uma função que recebe um número inteiro a1, a razão de progressão geométrica q > 1
    e um número inteiro n e retorna a soma dos n primeiros termos da progressão geométrica
    
    https://pt.wikipedia.org/wiki/Progress%C3%A3o_geom%C3%A9trica
    
    Test
    -----------
    >>> soma_pg(1, 2, 3)
    7
    >>> soma_pg(1, 2, 4)
    15
    '''
    soma = 0
    ### Seu código inicia aqui ###	
    
    ### Seu código termina aqui ###
    return soma

def fibonacci(n):
    '''
    Crie uma função que recebe um número inteiro n e retorna uma lista com os n primeiros termos da sequência de Fibonacci
    
    https://pt.wikipedia.org/wiki/Sequ%C3%AAncia_de_Fibonacci  0, 1, 1, 2, 3, 5, 8, ...
    
    Test
    -----------
    >>> fibonacci(4)
    [0, 1, 1, 2]
    >>> fibonacci(2)
    [0, 1]
    '''
    fib = []
    ### Seu código inicia aqui ###	
    
    ### Seu código termina aqui ###
    return fib

def soma_fibonacci(n):
    '''
    Crie uma função que recebe um número inteiro n e retorna a soma dos n primeiros termos da sequência de Fibonacci
    
    https://pt.wikipedia.org/wiki/Sequ%C3%AAncia_de_Fibonacci 0, 1, 1, 2, 3, 5, 8, ...
    
    Test
    -----------
    >>> soma_fibonacci(4)
    4
    >>> soma_fibonacci(5)
    7
    >>> soma_fibonacci(1)
    0
    >>> soma_fibonacci(2)
    1
    '''
    soma = 0
    ### Seu código inicia aqui ###	
    
    ### Seu código termina aqui ###
    return soma

def primo(n):
    '''
    Crie uma função que recebe um número inteiro n e retorna True se ele é primo e False caso contrário
    Test
    -----------
    >>> primo(7)
    True
    >>> primo(8)
    False
    '''
    resultado = False
    ### Seu código inicia aqui ###	
    
    ### Seu código termina aqui ###
    return resultado

def fit_linear(x, y):
    '''
    Crie uma função que recebe duas listas de números x e y e retorna uma lista com os coeficientes da 
    equação linear [A, B], considerando que y = A + B*x

    Importante: Use a equação da regressão linear como mostrada no vídeo da aula
    e não importe bibliotecas extras.
    
    Test
    -----------
    >>> fit_linear([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
    [0, 1]
    
    >>> fit_linear([1, 2, 3, 4, 5], [11, 21, 31, 41, 51])
    [1, 10]
    '''
    A, B = 0, 0
    ### Seu código inicia aqui ###	
    
    ### Seu código termina aqui ###
    return A, B

def numpy_seno(inicial, final, n_elementos):
    '''
    Crie uma função que calcule o seno de um vetor 1D no formato ndarray do numpy
    com a quantidade de elementosigual a n_elementos, iniciando no valor inicial e 
    terminando no final (variáveis da função).

    Importante: A biblioteca numpy já está importada no início do programa, 
    não importe novamente ela nem adicione outra bibliteca.

    Test
    ------------
    >>> numpy_seno(0, 1, 11)
    array([0.        , 0.09983342, 0.19866933, 0.29552021, 0.38941834,
       0.47942554, 0.56464247, 0.64421769, 0.71735609, 0.78332691, 0.84147098])

    >>> numpy_seno(2, 3, 4)
    array([0.90929743, 0.72308588, 0.45727263, 0.14112001])

    >>> numpy_seno(0, 0, 4)
    array([0., 0., 0., 0.])
    '''
    vetor = None
    ### Seu código inicia aqui ###	
    
    ### Seu código termina aqui ###
    return vetor

def cria_ndarray(linhas, colunas, min, max):
    '''
    Crie uma matriz (numpy ndarray) com duas dimensões contendo a quantidade
    de linhas igual a "linhas" e colunas "colunas (parâmetros da função).
    Este ndarray deverá conter valores randomicos que sejam no máximo igual 
    ao parâmetro max e no mínimo igual ao min.

    Test
    ------------
    >>> cria_ndarray(2, 3, 1, 2)
    array([[1.94385021, 1.08854403, 1.69537097],
        [1.69999035, 1.49960034, 1.50270302]])

    >>> cria_ndarray(3, 2, 3, 5)
    array([[4.88770042, 3.17708806],
           [4.39074194, 4.39998071],
           [3.99920069, 4.00540604]])
    '''
    np.random.seed(137)
    matrix = None
    ### Seu código inicia aqui ###	
    
    ### Seu código termina aqui ###
    return matrix



#################################################################################
#### Fim da Atividade 1 - O código abaixo é apenas para mostrar o resultado #####
#### Não altere nada abaixo desta linha                                     #####
#################################################################################


if __name__ == '__main__':
    print("=" * 60)
    print("TESTANDO SUAS FUNÇÕES - RELATÓRIO DE PROGRESSO")
    print("=" * 60)
    
    total_testes = 0
    testes_passaram = 0
    
    # Teste 1: soma_pa
    print("\n1. Testando função soma_pa...")
    try:
        resultado = soma_pa(1, 2, 4)
        assert resultado == 16, f"Esperado: 16, Obtido: {resultado}"
        print("   [OK] PASSOU - Soma de PA calculada corretamente!")
        testes_passaram += 1
    except AssertionError as e:
        print(f"   [X] FALHOU - {e}")
    except Exception as e:
        print(f"   [!] ERRO - {e}")
    total_testes += 1
    
    # Teste 2: progressao_geometrica
    print("\n2. Testando função progressao_geometrica...")
    try:
        resultado = progressao_geometrica(1, 2, 4)
        assert resultado == [1, 2, 4, 8], f"Esperado: [1, 2, 4, 8], Obtido: {resultado}"
        print("   [OK] PASSOU - Progressão geométrica criada corretamente!")
        testes_passaram += 1
    except AssertionError as e:
        print(f"   [X] FALHOU - {e}")
    except Exception as e:
        print(f"   [!] ERRO - {e}")
    total_testes += 1
    
    # Teste 3: soma_pg
    print("\n3. Testando função soma_pg...")
    try:
        resultado = soma_pg(1, 2, 3)
        assert resultado == 7, f"Esperado: 7, Obtido: {resultado}"
        print("   [OK] PASSOU - Soma de PG calculada corretamente!")
        testes_passaram += 1
    except AssertionError as e:
        print(f"   [X] FALHOU - {e}")
    except Exception as e:
        print(f"   [!] ERRO - {e}")
    total_testes += 1
    
    # Teste 4: fibonacci
    print("\n4. Testando função fibonacci...")
    try:
        resultado = fibonacci(4)
        assert resultado == [0, 1, 1, 2], f"Esperado: [0, 1, 1, 2], Obtido: {resultado}"
        print("   [OK] PASSOU - Sequência de Fibonacci criada corretamente!")
        testes_passaram += 1
    except AssertionError as e:
        print(f"   [X] FALHOU - {e}")
    except Exception as e:
        print(f"   [!] ERRO - {e}")
    total_testes += 1
    
    # Teste 5: soma_fibonacci
    print("\n5. Testando função soma_fibonacci...")
    try:
        resultado = soma_fibonacci(4)
        assert resultado == 4, f"Esperado: 4, Obtido: {resultado}"
        print("   [OK] PASSOU - Soma de Fibonacci calculada corretamente!")
        testes_passaram += 1
    except AssertionError as e:
        print(f"   [X] FALHOU - {e}")
    except Exception as e:
        print(f"   [!] ERRO - {e}")
    total_testes += 1
    
    # Teste 6: primo (testando número primo)
    print("\n6. Testando função primo (número primo)...")
    try:
        resultado = primo(7)
        assert resultado == True, f"Esperado: True, Obtido: {resultado}"
        print("   [OK] PASSOU - Número primo identificado corretamente!")
        testes_passaram += 1
    except AssertionError as e:
        print(f"   [X] FALHOU - {e}")
    except Exception as e:
        print(f"   [!] ERRO - {e}")
    total_testes += 1
    
    # Teste 7: primo (testando número não primo)
    print("\n7. Testando função primo (número não primo)...")
    try:
        resultado = primo(8)
        assert resultado == False, f"Esperado: False, Obtido: {resultado}"
        print("   [OK] PASSOU - Número não primo identificado corretamente!")
        testes_passaram += 1
    except AssertionError as e:
        print(f"   [X] FALHOU - {e}")
    except Exception as e:
        print(f"   [!] ERRO - {e}")
    total_testes += 1
    
    # Teste 8: fit_linear
    print("\n8. Testando função fit_linear...")
    try:
        resultado = fit_linear([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
        # Verificar se os valores estão próximos (tolerância para números decimais)
        A, B = resultado
        assert abs(A - 0) < 0.001 and abs(B - 1) < 0.001, f"Esperado: [0, 1], Obtido: {resultado}"
        print("   [OK] PASSOU - Regressão linear calculada corretamente!")
        testes_passaram += 1
    except AssertionError as e:
        print(f"   [X] FALHOU - {e}")
    except Exception as e:
        print(f"   [!] ERRO - {e}")
    total_testes += 1
    
    # Teste 9: numpy_seno
    print("\n9. Testando função numpy_seno...")
    try:
        resultado = numpy_seno(0, 0, 4)
        if resultado is None:
            raise AssertionError("Função retornou None - implemente a função!")
        esperado = np.array([0., 0., 0., 0.])
        assert np.allclose(resultado, esperado), f"Esperado: {esperado}, Obtido: {resultado}"
        print("   [OK] PASSOU - Função seno com numpy funcionando!")
        testes_passaram += 1
    except AssertionError as e:
        print(f"   [X] FALHOU - {e}")
    except Exception as e:
        print(f"   [!] ERRO - {e}")
    total_testes += 1
    
    # Teste 10: cria_ndarray
    print("\n10. Testando função cria_ndarray...")
    try:
        resultado = cria_ndarray(2, 3, 1, 2)
        if resultado is None:
            raise AssertionError("Função retornou None - implemente a função!")
        # Verificar se tem o formato correto e valores no intervalo
        assert resultado.shape == (2, 3), f"Formato esperado: (2, 3), Obtido: {resultado.shape}"
        assert np.all(resultado >= 1) and np.all(resultado <= 2), "Valores devem estar entre 1 e 2"
        print("   [OK] PASSOU - Array numpy criado corretamente!")
        testes_passaram += 1
    except AssertionError as e:
        print(f"   [X] FALHOU - {e}")
    except Exception as e:
        print(f"   [!] ERRO - {e}")
    total_testes += 1
    
    # Relatório final
    print("\n" + "=" * 60)
    print("RELATÓRIO FINAL")
    print("=" * 60)
    porcentagem = (testes_passaram / total_testes) * 100
    print(f"Testes realizados: {total_testes}")
    print(f"Testes que passaram: {testes_passaram}")
    print(f"Taxa de sucesso: {porcentagem:.1f}%")
    
    if porcentagem == 100:
        print("*** PARABENS! Todas as funções estão funcionando perfeitamente!")
    elif porcentagem >= 80:
        print("*** Muito bom! A maioria das funções está correta. Continue assim!")
    elif porcentagem >= 60:
        print("*** Você está no caminho certo! Revise as funções que falharam.")
    elif porcentagem >= 40:
        print("*** Continue estudando! Metade do caminho já foi percorrido.")
    else:
        print("*** Não desista! Revise os conceitos e implemente as funções faltantes.")
    
    print("\nDica: Implemente as funções que ainda não estão funcionando!")
    print("=" * 60)