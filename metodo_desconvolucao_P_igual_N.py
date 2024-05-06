# Projeto ATLAS - Reconstrução de sinal - Método da desconvolução de sinais.
# Autor: Guilherme Barroso Morett.
# Data: 06 de maio de 2024.

# Objetivo do código: aplicação do método da desconvolução de sinais - P = N.

""" Organização do Código:

Funções presentes:

1) Função para a construção da matriz H a partir dos dados dos pulsos de referência.
Entrada: número de janelamento.
Saída: matriz H.

2) Instrução para o método da desconvolução para o caso N = P.
Entrada: Matriz com os pulsos de sinais e o vetor da amplitude de referência.
Saída: nada.

"""

# Importação das bibliotecas.
import numpy as np

### ---------------------------------- 1) DEFINIÇÃO DA FUNÇÃO PARA A CONSTRUÇÃO DA MATRIZ H ---------------------------------------------------- ###

# Criação da função matriz_H.
def matriz_H(n_janelamento):
    
    # Caso o número de janelamento seja 7.
    if n_janelamento == 7:
        
        # Definição dos valores dos pulsos de referência g para o janelamento 7.
        g1 = 0.00002304
        g2 = 0.01722640
        g3 = 0.45244500
        g4 = 1.00000000
        g5 = 0.56330700
        g6 = 0.14933500
        g7 = 0.04235980
    
        # Criação das linhas da matriz H com os pulsos de referência deslocados para o janelamento 7.
        H1 = [g4, g5, g6, g7, 0, 0, 0]
        H2 = [g3, g4, g5, g6, g7, 0, 0]
        H3 = [g2, g3, g4, g5, g6, g7, 0]
        H4 = [g1, g2, g3, g4, g5, g6, g7]
        H5 = [0, g1, g2, g3, g4, g5, g6]
        H6 = [0, 0, g1, g2, g3, g4, g5]
        H7 = [0, 0, 0, g1, g2, g3, g4]
        
        # Construção da matriz H a partir dessas linhas.
        H = list(zip(H1, H2, H3, H4, H5, H6, H7))
    
    # Caso o número de janelamento seja 9.
    elif n_janelamento == 9:
        
        # Definição dos valores dos pulsos de referência g para o janelamento 9.
        g1 = 0.00000000
        g2 = 0.00002304
        g3 = 0.01722640
        g4 = 0.45244500
        g5 = 1.00000000
        g6 = 0.56330700
        g7 = 0.14933500
        g8 = 0.04235980
        g9 = 0.00480767
        
        # Criação das linhas da matriz H com os pulsos de referência deslocados para o janelamento 9.
        H1 = [g5, g6, g7, g8, g9, 0, 0, 0, 0]
        H2 = [g4, g5, g6, g7, g8, g9, 0, 0, 0]
        H3 = [g3, g4, g5, g6, g7, g8, g9, 0, 0]
        H4 = [g2, g3, g4, g5, g6, g7, g8, g9, 0]
        H5 = [g1, g2, g3, g4, g5, g6, g7, g8, g9]
        H6 = [0, g1, g2, g3, g4, g5, g6, g7, g8]
        H7 = [0, 0, g1, g2, g3, g4, g5, g6, g7]
        H8 = [0, 0, 0, g1, g2, g3, g4, g5, g6]
        H9 = [0, 0, 0, 0, g1, g2, g3, g4, g5]
        
        # Construção da matriz H a partir dessas linhas.
        H = list(zip(H1, H2, H3, H4, H5, H6, H7, H8, H9))
    
    # Caso o número de janelamento seja 11.
    elif n_janelamento == 11:
        
        # Definição dos valores dos pulsos de referência g para o janelamento 11.
        g1 = 0.00000000
        g2 = 0.00000000
        g3 = 0.00002304
        g4 = 0.01722640
        g5 = 0.45244500
        g6 = 1.00000000
        g7 = 0.56330700
        g8 = 0.14933500
        g9 = 0.04235980
        g10 = 0.00480767
        g11 = 0.00000000
        
        # Criação das linhas da matriz H com os pulsos de referência deslocados para o janelamento 11.
        H1 = [g6, g7, g8, g9, g10, g11, 0, 0, 0, 0, 0]
        H2 = [g5, g6, g7, g8, g9, g10, g11, 0, 0, 0, 0]
        H3 = [g4, g5, g6, g7, g8, g9, g10, g11, 0, 0, 0]
        H4 = [g3, g4, g5, g6, g7, g8, g9, g10, g11, 0, 0]
        H5 = [g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, 0]
        H6 = [g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11]
        H7 = [0, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10]
        H8 = [0, 0, g1, g2, g3, g4, g5, g6, g7, g8, g9]
        H9 = [0, 0 , 0, g1, g2, g3, g4, g5, g6, g7, g8]
        H10 = [0, 0, 0, 0, g1, g2, g3, g4, g5, g6, g7]
        H11 = [0, 0, 0, 0, 0, g1, g2, g3, g4, g5, g6]
        
        # Construção da matriz H a partir dessas linhas.
        H = list(zip(H1, H2, H3, H4, H5, H6, H7, H8, H9, H10, H11))
        
    # Caso o número de janelamento seja 13.
    elif n_janelamento == 13:
        
        # Definição dos valores dos pulsos de referência g para o janelamento 13.
        g1 = 0.00000000
        g2 = 0.00000000
        g3 = 0.00000000
        g4 = 0.00002304
        g5 = 0.01722640
        g6 = 0.45244500
        g7 = 1.00000000
        g8 = 0.56330700
        g9 = 0.14933500
        g10 = 0.04235980
        g11 = 0.00480767
        g12 = 0.00000000
        g13 = 0.00000000
        
        # Criação das linhas da matriz H com os pulsos de referência deslocados para o janelamento 13.
        H1 = [g7, g8, g9, g10, g11, g12, g13, 0, 0, 0, 0, 0, 0]
        H2 = [g6, g7, g8, g9, g10, g11, g12, g13, 0, 0, 0, 0, 0]
        H3 = [g5, g6, g7, g8, g9, g10, g11, g12, g13, 0, 0, 0, 0]
        H4 = [g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, 0, 0, 0]
        H5 = [g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, 0, 0]
        H6 = [g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, 0]
        H7 = [g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13]
        H8 = [0, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12]
        H9 = [0, 0 , g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11]
        H10 = [0, 0, 0, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10]
        H11 = [0, 0, 0, 0, g1, g2, g3, g4, g5, g6, g7, g8, g9]
        H12 = [0, 0, 0, 0, 0, g1, g2, g3, g4, g5, g6, g7, g8]
        H13 = [0, 0, 0, 0, 0, 0, g1, g2, g3, g4, g5, g6, g7]
        
        # Construção da matriz H a partir dessas linhas.
        H = list(zip(H1, H2, H3, H4, H5, H6, H7, H8, H9, H10, H11, H12, H13))
        
    # Caso o número de janelamento seja 15.
    elif n_janelamento == 15:
        
        # Definição dos valores dos pulsos de referência g para o janelamento 15.
        g1 = 0.00000000
        g2 = 0.00000000
        g3 = 0.00000000
        g4 = 0.00000000
        g5 = 0.00002304
        g6 = 0.01722640
        g7 = 0.45244500
        g8 = 1.00000000
        g9 = 0.56330700
        g10 = 0.14933500
        g11 = 0.04235980
        g12 = 0.00480767
        g13 = 0.00000000
        g14 = 0.00000000
        g15 = 0.00000000
        
        # Criação das linhas da matriz H com os pulsos de referência deslocados para o janelamento 15.
        H1 = [g8, g9, g10, g11, g12, g13, g14, g15, 0, 0, 0, 0, 0, 0, 0]
        H2 = [g7, g8, g9, g10, g11, g12, g13, g14, g15, 0, 0, 0, 0, 0, 0]
        H3 = [g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, 0, 0, 0, 0, 0]
        H4 = [g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, 0, 0, 0, 0]
        H5 = [g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, 0, 0, 0]
        H6 = [g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, 0, 0]
        H7 = [g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, 0]
        H8 = [g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15]
        H9 = [0, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14]
        H10 = [0, 0, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13]
        H11 = [0, 0, 0, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12]
        H12 = [0, 0, 0, 0, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11]
        H13 = [0, 0, 0, 0, 0, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10]
        H14 = [0, 0, 0, 0, 0, 0, g1, g2, g3, g4, g5, g6, g7, g8, g9]
        H15 = [0, 0, 0, 0, 0, 0, 0, g1, g2, g3, g4, g5, g6, g7, g8]
        
        # Construção da matriz H a partir dessas linhas.
        H = list(zip(H1, H2, H3, H4, H5, H6, H7, H8, H9, H10, H11, H12, H13, H14, H15))
    
    # Caso o número de janelamento seja 17.
    elif n_janelamento == 17:
        
        # Definição dos valores dos pulsos de referência g para o janelamento 17.
        g1 = 0.00000000
        g2 = 0.00000000
        g3 = 0.00000000
        g4 = 0.00000000
        g5 = 0.00000000
        g6 = 0.00002304
        g7 = 0.01722640
        g8 = 0.45244500
        g9 = 1.00000000
        g10 = 0.56330700
        g11 = 0.14933500
        g12 = 0.04235980
        g13 = 0.00480767
        g14 = 0.00000000
        g15 = 0.00000000
        g16 = 0.00000000
        g17 = 0.00000000
        
        # Criação das linhas da matriz H com os pulsos de referência deslocados para o janelamento 17.
        H1 = [g9, g10, g11, g12, g13, g14, g15, g16, g17, 0, 0, 0, 0, 0, 0, 0 ,0]
        H2 = [g8, g9, g10, g11, g12, g13, g14, g15, g16, g17, 0, 0, 0, 0, 0, 0, 0]
        H3 = [g7, g8, g9, g10, g11, g12, g13, g14, g15, g16, g17, 0, 0, 0, 0, 0, 0]
        H4 = [g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, g16, g17, 0, 0, 0, 0, 0]
        H5 = [g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, g16, g17, 0, 0, 0, 0]
        H6 = [g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, g16, g17, 0, 0, 0]
        H7 = [g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, g16, g17, 0, 0]
        H8 = [g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, g16, g17, 0]
        H9 = [g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, g16, g17]
        H10 = [0, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, g16]
        H11 = [0, 0, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15]
        H12 = [0, 0, 0, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14]
        H13 = [0, 0, 0, 0, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13]
        H14 = [0, 0, 0, 0, 0, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12]
        H15 = [0, 0, 0, 0, 0, 0, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11]
        H16 = [0, 0, 0, 0, 0, 0, 0, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10]
        H17 = [0, 0, 0, 0, 0, 0, 0, 0, g1, g2, g3, g4, g5, g6, g7, g8, g9]
        
        # Construção da matriz H a partir dessas linhas.
        H = list(zip(H1, H2, H3, H4, H5, H6, H7, H8, H9, H10, H11, H12, H13, H14, H15, H16, H17))
        
    # Caso o número de janelamento seja 19.
    elif n_janelamento == 19:
        
        # Definição dos valores dos pulsos de referência g para o janelamento 19.
        g1 = 0.00000000
        g2 = 0.00000000
        g3 = 0.00000000
        g4 = 0.00000000
        g5 = 0.00000000
        g6 = 0.00000000
        g7 = 0.00002304
        g8 = 0.01722640
        g9 = 0.45244500
        g10 = 1.00000000
        g11 = 0.56330700
        g12 = 0.14933500
        g13 = 0.04235980
        g14 = 0.00480767
        g15 = 0.00000000
        g16 = 0.00000000
        g17 = 0.00000000
        g18 = 0.00000000
        g19 = 0.00000000
        
        # Criação das linhas da matriz H com os pulsos de referência deslocados para o janelamento 19.
        H1 = [g10, g11, g12, g13, g14, g15, g16, g17, g18, g19, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        H2 = [g9, g10, g11, g12, g13, g14, g15, g16, g17, g18, g19, 0, 0, 0, 0, 0, 0, 0, 0]
        H3 = [g8, g9, g10, g11, g12, g13, g14, g15, g16, g17, g18, g19, 0, 0, 0, 0, 0, 0, 0]
        H4 = [g7, g8, g9, g10, g11, g12, g13, g14, g15, g16, g17, g18, g19, 0, 0, 0, 0, 0, 0]
        H5 = [g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, g16, g17, g18, g19, 0, 0, 0, 0, 0]
        H6 = [g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, g16, g17, g18, g19, 0, 0, 0, 0]
        H7 = [g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, g16, g17, g18, g19, 0, 0, 0]
        H8 = [g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, g16, g17, g18, g19, 0, 0]
        H9 = [g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, g16, g17, g18, g19, 0]
        H10 = [g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, g16, g17, g18, g19]
        H11 = [0, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, g16, g17, g18]
        H12 = [0, 0, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, g16, g17]
        H13 = [0, 0, 0, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, g16]
        H14 = [0, 0, 0, 0, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15]
        H15 = [0, 0, 0, 0, 0, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14]
        H16 = [0, 0, 0, 0, 0, 0, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13]
        H17 = [0, 0, 0, 0, 0, 0, 0, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12]
        H18 = [0, 0, 0, 0, 0, 0, 0, 0, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11]
        H19 = [0, 0, 0, 0, 0, 0, 0, 0, 0, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10]
        
        # Construção da matriz H a partir dessas linhas.
        H = list(zip(H1, H2, H3, H4, H5, H6, H7, H8, H9, H10, H11, H12, H13, H14, H15, H16, H17, H18, H19))
        
    # Conversão dessa lista para um numpy array.
    H = np.array(H)
    
    # A função retorna a matriz H.
    return H

### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### ---------------------------------------- 2) FUNÇÃO DO MÉTODO DE DESCONVOLUÇÃO -------------------------------------------------------------- ###

# Definição da função desconvolucao.
def desconvolucao_P_igual_N(Matriz_pulsos_sinais, vetor_amplitude_referencia, n_janelamento):  
    
    # Criação da lista vazia para armazenar os erros calculados para a amplitude. 
    lista_erro_amplitude = []

    # Para o índice de zero até o número de linhas da matriz Matriz_pulsos_sinais.
    for indice_linha in range(len(Matriz_pulsos_sinais)):
        
        # A variável H recebe o retorno da função matriz_H.
        H = matriz_H(n_janelamento)
    
        # O vetor vetor_pulsos_sinais corresponde a linha de índice indice_linha da matriz Matriz_pulsos_sinais.    
        vetor_pulsos_sinais = Matriz_pulsos_sinais[indice_linha]
    
        # A amplitude de referência é o elemento de índice indice_linha do vetor vetor_amplitude_referencia.
        valor_amplitude_referencia = vetor_amplitude_referencia[indice_linha]
        
        # Tenta calcular a inversa da matriz.
        try:
        # Calcula a inversa da matriz usando numpy.linalg.inv.
            inv_H = np.linalg.inv(H)
          
        # Caso a matriz seja singular ou não invertível.  
        except np.linalg.LinAlgError:
        # Impressão de mensagem de erro
            print("A matriz não é invertível.")
        
        # Cálculo do vetor da amplitude estimada.
        vetor_amplitude_estimada = np.dot(inv_H, vetor_pulsos_sinais)
        
        # Armazena o índice da amplitude central na variável indice_amplitude_central.
        indice_amplitude_central = len(vetor_amplitude_estimada) // 2
            
        # A amplitude estimada é definida como o elemento do vetor com o índice indice_amplitude_central.
        amplitude_estimada = vetor_amplitude_estimada[indice_amplitude_central]
         
        # Cálculo do erro de estimação da amplitude.
        erro_amplitude = valor_amplitude_referencia-amplitude_estimada
    
        # O elemento erro_amplitude é adicionado na lista correspondente.    
        lista_erro_amplitude.append(erro_amplitude)

    # A função retorna a lista lista_erro_amplitude.
    return lista_erro_amplitude

### -------------------------------------------------------------------------------------------------------------------------------------------- ###
