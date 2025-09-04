import math
import numpy as np
import pandas as pd
import sklearn
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

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

### Seu código inicia aqui ###

nome = 'gustavo_voltani_von_atzingen' # # coloque aqui o nome completo sem espaços (colocar '_' entre as palavras e.g. gustavo_voltani_von_atzingen) no formato de uma string
          # Mantenha o mesmo nome que você colocou na atividade 1 para facilitar a agregação de dados no final

### Seu código termina aqui ###


def entropia(na, nb):
    '''
    Crie uma função que recebe a quantidade (em inteiros) de dois elementos - na e nb - e retorne
    o valor da entropia do conjunto.
    
    Utilize math.log2(p) para calcular o valor do log base do de uma probabilidade.
    
    Test
    -----------
    >>> entropia(50, 50)
    1
    
    >>> entropia(10, 50)
    0.6500224216483541
    
    >>> entropia(10, 100)
    0.4394969869215134
    
    >>> entropia(0, 100)
    0.0
    
    >>> entropia(10, 0)
    0.0
    ''' 
    entropia = 1
    ### Seu código inicia aqui ###	
    
    ### Seu código termina aqui ###
    return entropia


def organize_data(file_name):
    '''
    Crie uma função que utiliza le um arquivo csv utilizando a biblioteca pandas
    e então organiza os dados apenas com as colunas:
    A, B, C, D, targuet (Removendo as colunas E e F) e retorne um dataframe (df)
    
    * Utilize o arquivo dados.csv como teste de entrada para a função
    
    * Utilize pandas como pd
    
    Test
    -----------
    >>> type(organize_data('data.csv'))
    pandas.core.frame.DataFrame
    
    >>> organize_data('data.csv').shape
    (200, 5)
    
    >>> organize_data('data.csv').columns
    Index(['A', 'B', 'C', 'D', 'y'], dtype='object')
    
    >>> organize_data('data.csv').loc[1].values
    array([9.74986214, 5.14024213, 5.86335541, 5.24703444, 1.0])
    
    >>> organize_data('data.csv').loc[100].values
    array([9.00177971, 4.42446467, 7.19523579, 5.72467708, 1.0])
    '''
    df = None
    ### Seu código inicia aqui ###
    
    ### Seu código termina aqui ###
    return df

def shuffle_split_data(df):
    '''
    Crie uma função que receba o dataframe com as colunas A, B, C, D, targuet,
    (gerado na função organize_data() ) e organize os dados em numpy arrays
    X_train, X_test, y_train, y_test, com X contendo as colunas A, B, C e D e 
    y a coluna targuet.
    Embaralhe os dados X e y com a train_test_split da biblioteca skelarn com o 
    random_state 33 e com 75% dos dados para treino e 25% para teste.
    
    Test
    -----------
    >>> len(shuffle_split_data(df))
    4
    
    >>> shuffle_split_data(df)[0].shape
    (150, 4)
    
    >>> shuffle_split_data(df)[1].shape
    (50, 4)
    
    >>> shuffle_split_data(df)[2].shape
    (150,)
    
    >>> shuffle_split_data(df)[3].shape
    (50,)
    '''
    X_train, X_test, y_train, y_test = None, None, None, None
    ### Seu código inicia aqui ###
    
    ### Seu código termina aqui ###
    return X_train, X_test, y_train, y_test


def limpa_dataset(df):
    '''
    Crie uma função que recebe um dataframe e remove todas as linhas que possuem valores faltando
    (NaN) e depois disso transforma todas as colunas numéricas em números de 0 a 1.
    '''
    ### Seu código inicia aqui ###
    
    ### Seu código termina aqui ###
    return df



#################################################################################
#### Fim da Atividade 2 - O código abaixo é apenas para mostrar o resultado #####
#### Não altere nada abaixo desta linha                                     #####
#################################################################################

if __name__ == '__main__':
    print("=" * 60)
    print("TESTANDO SUAS FUNÇÕES - RELATÓRIO DE PROGRESSO - ATIVIDADE 2")
    print("=" * 60)
    
    total_testes = 0
    testes_passaram = 0
    
    # Teste 1: entropia (caso balanceado)
    print("\n1. Testando função entropia (caso balanceado)...")
    try:
        resultado = entropia(50, 50)
        assert abs(resultado - 1.0) < 0.001, f"Esperado: 1.0, Obtido: {resultado}"
        print("   [OK] PASSOU - Entropia balanceada calculada corretamente!")
        testes_passaram += 1
    except AssertionError as e:
        print(f"   [X] FALHOU - {e}")
    except Exception as e:
        print(f"   [!] ERRO - {e}")
    total_testes += 1
    
    # Teste 2: entropia (caso desbalanceado)
    print("\n2. Testando função entropia (caso desbalanceado)...")
    try:
        resultado = entropia(10, 100)
        expected = 0.4394969869215134
        assert abs(resultado - expected) < 0.001, f"Esperado: {expected}, Obtido: {resultado}"
        print("   [OK] PASSOU - Entropia desbalanceada calculada corretamente!")
        testes_passaram += 1
    except AssertionError as e:
        print(f"   [X] FALHOU - {e}")
    except Exception as e:
        print(f"   [!] ERRO - {e}")
    total_testes += 1
    
    # Teste 3: entropia (caso extremo - sem elementos)
    print("\n3. Testando função entropia (caso extremo)...")
    try:
        resultado = entropia(0, 100)
        assert abs(resultado - 0.0) < 0.001, f"Esperado: 0.0, Obtido: {resultado}"
        print("   [OK] PASSOU - Entropia de caso extremo calculada corretamente!")
        testes_passaram += 1
    except AssertionError as e:
        print(f"   [X] FALHOU - {e}")
    except Exception as e:
        print(f"   [!] ERRO - {e}")
    total_testes += 1
    
    # Teste 4: organize_data - tipo do retorno
    print("\n4. Testando função organize_data (tipo)...")
    try:
        resultado = organize_data('data.csv')
        if resultado is None:
            raise AssertionError("Função retornou None - implemente a função!")
        assert str(type(resultado)) == "<class 'pandas.core.frame.DataFrame'>", f"Esperado: DataFrame, Obtido: {type(resultado)}"
        print("   [OK] PASSOU - Tipo de retorno correto (DataFrame)!")
        testes_passaram += 1
    except AssertionError as e:
        print(f"   [X] FALHOU - {e}")
    except Exception as e:
        print(f"   [!] ERRO - {e}")
    total_testes += 1
    
    # Teste 5: organize_data - formato dos dados
    print("\n5. Testando função organize_data (formato)...")
    try:
        resultado = organize_data('data.csv')
        if resultado is None:
            raise AssertionError("Função retornou None - implemente a função!")
        assert resultado.shape == (200, 5), f"Esperado: (200, 5), Obtido: {resultado.shape}"
        print("   [OK] PASSOU - Formato dos dados correto!")
        testes_passaram += 1
    except AssertionError as e:
        print(f"   [X] FALHOU - {e}")
    except Exception as e:
        print(f"   [!] ERRO - {e}")
    total_testes += 1
    
    # Teste 6: organize_data - colunas
    print("\n6. Testando função organize_data (colunas)...")
    try:
        resultado = organize_data('data.csv')
        if resultado is None:
            raise AssertionError("Função retornou None - implemente a função!")
        colunas_esperadas = ['A', 'B', 'C', 'D', 'y']
        colunas_obtidas = list(resultado.columns)
        assert colunas_obtidas == colunas_esperadas, f"Esperado: {colunas_esperadas}, Obtido: {colunas_obtidas}"
        print("   [OK] PASSOU - Colunas organizadas corretamente!")
        testes_passaram += 1
    except AssertionError as e:
        print(f"   [X] FALHOU - {e}")
    except Exception as e:
        print(f"   [!] ERRO - {e}")
    total_testes += 1
    
    # Teste 7: organize_data - valores específicos
    print("\n7. Testando função organize_data (valores específicos)...")
    try:
        resultado = organize_data('data.csv')
        if resultado is None:
            raise AssertionError("Função retornou None - implemente a função!")
        valores_linha_1 = resultado.loc[1].values
        esperado = np.array([9.74986214, 5.14024213, 5.86335541, 5.24703444, 1.0])
        assert np.allclose(valores_linha_1, esperado, atol=1e-6), f"Esperado: {esperado}, Obtido: {valores_linha_1}"
        print("   [OK] PASSOU - Valores específicos corretos!")
        testes_passaram += 1
    except AssertionError as e:
        print(f"   [X] FALHOU - {e}")
    except Exception as e:
        print(f"   [!] ERRO - {e}")
    total_testes += 1
    
    # Teste 8: shuffle_split_data - formato X_train
    print("\n8. Testando função shuffle_split_data (X_train)...")
    try:
        df = organize_data('data.csv')
        if df is None:
            raise AssertionError("organize_data retornou None - implemente primeiro!")
        resultado = shuffle_split_data(df)
        if any(x is None for x in resultado):
            raise AssertionError("Função retornou None - implemente a função!")
        X_train = resultado[0]
        if X_train is None:
            raise AssertionError("X_train é None - implemente a função!")
        assert X_train.shape == (150, 4), f"Esperado: (150, 4), Obtido: {X_train.shape}"
        print("   [OK] PASSOU - Formato de X_train correto!")
        testes_passaram += 1
    except AssertionError as e:
        print(f"   [X] FALHOU - {e}")
    except Exception as e:
        print(f"   [!] ERRO - {e}")
    total_testes += 1
    
    # Teste 9: shuffle_split_data - formato X_test
    print("\n9. Testando função shuffle_split_data (X_test)...")
    try:
        df = organize_data('data.csv')
        if df is None:
            raise AssertionError("organize_data retornou None - implemente primeiro!")
        resultado = shuffle_split_data(df)
        if any(x is None for x in resultado):
            raise AssertionError("Função retornou None - implemente a função!")
        X_test = resultado[1]
        if X_test is None:
            raise AssertionError("X_test é None - implemente a função!")
        assert X_test.shape == (50, 4), f"Esperado: (50, 4), Obtido: {X_test.shape}"
        print("   [OK] PASSOU - Formato de X_test correto!")
        testes_passaram += 1
    except AssertionError as e:
        print(f"   [X] FALHOU - {e}")
    except Exception as e:
        print(f"   [!] ERRO - {e}")
    total_testes += 1
    
    # Teste 10: shuffle_split_data - formato y_train e y_test
    print("\n10. Testando função shuffle_split_data (y_train e y_test)...")
    try:
        df = organize_data('data.csv')
        if df is None:
            raise AssertionError("organize_data retornou None - implemente primeiro!")
        resultado = shuffle_split_data(df)
        if any(x is None for x in resultado):
            raise AssertionError("Função retornou None - implemente a função!")
        y_train, y_test = resultado[2], resultado[3]
        if y_train is None or y_test is None:
            raise AssertionError("y_train ou y_test é None - implemente a função!")
        assert y_train.shape == (150,), f"Esperado y_train: (150,), Obtido: {y_train.shape}"
        assert y_test.shape == (50,), f"Esperado y_test: (50,), Obtido: {y_test.shape}"
        print("   [OK] PASSOU - Formato de y_train e y_test corretos!")
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
    print("Lembre-se de:")
    print("- A função entropia usa math.log2()")
    print("- O organize_data deve renomear 'targuet' para 'y' e remover colunas E e F")
    print("- O shuffle_split_data usa train_test_split com random_state=33")
    print("=" * 60)