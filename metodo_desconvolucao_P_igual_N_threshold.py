# EXPERIMENTO ATLAS - Reconstrução de sinal - Método de Desconvolução de Sinal Versão Threshold Caso P = N - Estimação da amplitude.
# Autor: Guilherme Barroso Morett.
# Data: 29 de julho de 2024.

# Objetivo do código: aplicação do método de Desconvolução de Sinal Versão Threshold.

""" Organização do Código:

Funções presentes:

1) Função para a construção da matriz H a partir dos dados dos pulsos de referência.
Entrada: número de janelamento.
Saída: matriz H.

2) Função para a primeira parte do método de Desconvolução de Sinal. 
Entrada: vetor dos pulsos de sinais e a matriz H.
Saída: vetor da amplitude estimada.

3) Função para localizar o índice que corresponde ao pulso central da matriz H. 
Entrada: número de janelamento e a matriz H.
Saída: valor do índice da linha do pulso central na matriz H.

4) Função para o método de Desconvolução de SInal Versão Threshold.
Entrada: Matriz com os pulsos de sinais e o vetor da amplitude de referência.
Saída: lista do erro de estimação da amplitude.

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
        H = np.array([H1, H2, H3, H4, H5, H6, H7])
       
        # Definição da linha_pulso_central.
        linha_pulso_central = np.array(H4)
    
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
        H = np.array([H1, H2, H3, H4, H5, H6, H7, H8, H9])
        
        # Definição da linha_pulso_central.
        linha_pulso_central = np.array(H5)
    
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
        H = np.array([H1, H2, H3, H4, H5, H6, H7, H8, H9, H10, H11])
        
        # Definição da linha_pulso_central.
        linha_pulso_central = np.array(H6)
        
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
        H = np.array([H1, H2, H3, H4, H5, H6, H7, H8, H9, H10, H11, H12, H13])
        
        # Definição da linha_pulso_central.
        linha_pulso_central = np.array(H7)
        
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
        H = np.array([H1, H2, H3, H4, H5, H6, H7, H8, H9, H10, H11, H12, H13, H14, H15])
        
        # Definição da linha_pulso_central.
        linha_pulso_central = np.array(H8)
    
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
        H = np.array([H1, H2, H3, H4, H5, H6, H7, H8, H9, H10, H11, H12, H13, H14, H15, H16, H17])
        
        # Definição da linha_pulso_central.
        linha_pulso_central = np.array(H9)
        
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
        H = np.array([H1, H2, H3, H4, H5, H6, H7, H8, H9, H10, H11, H12, H13, H14, H15, H16, H17, H18, H19])
        
        # Definição da linha_pulso_central.
        linha_pulso_central = np.array(H10)
             
    # A função retorna a matriz H.
    return H, linha_pulso_central

### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### ---------------------------------- 2) FUNÇÃO PARA A PRIMEIRA PARTE DO MÉTODO DE DESCONVOLUÇÃO DE SINAL ------------------------------------- ###

# Obs.: a primeira parte consiste no cálculo no cálculo do vetor da amplitude estimada.
# Definição da função da primeira parte do método de desconvolução de sinal.
def metodo_desconvolucao_vetor_amplitude_estimada(vetor_pulsos_sinais, Matriz_H):
    
    # As variáveis n_linhas_matriz_H e n_colunas_matriz_H armazenam respectivamente o número de linhas e colunas da matriz H.
    n_linhas_matriz_H, n_colunas_matriz_H = Matriz_H.shape
    
    # Caso a matriz H seja quadrada (número de linhas é igual ao número de colunas).
    if n_linhas_matriz_H == n_colunas_matriz_H:
        
        # Tenta calcular a inversa da matriz.
        try:
            
        # Calcula a inversa da matriz usando numpy.linalg.inv.
            Inv_H = np.linalg.inv(Matriz_H)
          
        # Caso a matriz seja singular ou não invertível.  
        except np.linalg.LinAlgError:
        # Impressão de mensagem de erro
            print("A matriz não é invertível.") 
    
    # Caso contrário.
    else:
        
        # Tenta calcular a pseudoinversa da matriz.
        try:
            
            # Calcula a pseudoinversa da matriz usando numpy.linalg.pinv(matriz)
            Pseudo_Inversa_H = np.linalg.pinv(Matriz_H)
            
            Inv_H = np.transpose(Pseudo_Inversa_H)
            
        # Caso a matriz seja singular ou não invertível.  
        except np.linalg.LinAlgError:
        # Impressão de mensagem de erro
            print("A matriz não é invertível.") 
     
            
    # Cálculo do vetor da amplitude estimada.
    vetor_amplitude_estimada = np.dot(Inv_H, vetor_pulsos_sinais)
        
    # A função retorna o vetor da amplitude estimada.
    return vetor_amplitude_estimada

### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### -------------------- 3) FUNÇÃO PARA LOCALIZAR O ÍNDICE QUE CORRESPONDE AO PULSO CENTRAL DA MATRIZ H ---------------------------------------- ###

# Definição da função para localizar o índice da linha referente ao pulso central da matriz H.
def localizar_indice_pulso_central(n_janelamento, Matriz_H, linha_alvo_busca):
    
    # Encontrando o índice da linha alvo
    indices_linha_alvo_busca = np.where((Matriz_H == linha_alvo_busca).all(axis=1))[0]

    # Armazenando o índice da linha alvo na variável
    if len(indices_linha_alvo_busca) > 0:
        indice_linha_alvo = indices_linha_alvo_busca[0]
    else:
        indice_linha_alvo = None
    
    # A função retorna o indice da linha alvo de busca.
    return indice_linha_alvo

### ---------------------------------------- 4) FUNÇÃO DO MÉTODO DE DESCONVOLUÇÃO DE SINAL ----------------------------------------------------- ###

# Definição da função para o método de Desconvolução de Sinal.
def metodo_desconvolucao_threshold_P_igual_N(n_janelamento, Matriz_Pulsos_Sinais_Janelado, vetor_amplitude_referencia_janelado):  
    
    # Criação da lista vazia para armazenar os erros calculados para a amplitude. 
    lista_erro_estimacao_amplitude = []
    
    # Definição da variável valor_minimo_amplitude que armazena o valor mínimo da amplitude aceita.
    valor_minimo_amplitude = 4.5
    #Obs.: o valor de 4,5 ADC Count correponde a três vezes o valor do desvio padrão do ruído eletrônico (1,5 ADC Count). 

    # Para o índice de zero até o número de linhas da matriz Matriz_Pulsos_Sinais.
    for indice_linha in range(len(Matriz_Pulsos_Sinais_Janelado)):
        
        # A variável Matriz_H recebe o retorno da função matriz_H.
        Matriz_H, linha_pulso_central = matriz_H(n_janelamento)
    
        # O vetor vetor_pulsos_sinais corresponde a linha de índice indice_linha da matriz Matriz_Pulsos_Sinais_Janelado.    
        vetor_pulsos_sinais = Matriz_Pulsos_Sinais_Janelado[indice_linha]
    
        # A amplitude de referência é o elemento de índice indice_linha do vetor vetor_amplitude_referencia_janelado.
        valor_amplitude_referencia = vetor_amplitude_referencia_janelado[indice_linha]
        
        # A função metodo_desconvolucao_vetor_amplitude_estimada retorna o vetor da amplitude estimada.
        vetor_amplitude_estimada = metodo_desconvolucao_vetor_amplitude_estimada(vetor_pulsos_sinais, Matriz_H)
        
        # Percorre o vetor da amplitude estimada e localiza os índices dos elementos que possuem valores menores que a amplitude mínima. Esses índices são armazenados na lista lista_indices_amplitudes_baixas.
        lista_indices_amplitudes_baixas = [indice for indice, valor_amplitude in enumerate(vetor_amplitude_estimada) if valor_amplitude < valor_minimo_amplitude]
        
        # A váriável valor_indice_pulso_central armazena o valor do índice associado a linah da matriz H que contém o pulso central.
        valor_indice_pulso_central = localizar_indice_pulso_central(n_janelamento, Matriz_H, linha_pulso_central)
        
        # Caso o valor do índice asssociado ao pulso central esteja presente na lista dos índices que contém aplitudes baixas.
        if valor_indice_pulso_central in lista_indices_amplitudes_baixas:
            
           # A amplitude estimada é definida como aquela de índice igual ao valor do índice do pulso central do vetor da amplitude estimada.
           amplitude_estimada = vetor_amplitude_estimada[valor_indice_pulso_central]
          
        # Caso contrário. 
        else:
            
           # Remoção da matriz H das linhas cujos índices estão presentes na lista lista_indices_amplitudes_baixas.
           Matriz_H_linhas_removidas = np.delete(Matriz_H, lista_indices_amplitudes_baixas, axis=0)
           
           # A váriável valor_indice_pulso_central armazena o valor do índice associado a linnha da matriz H formatada que contém o pulso central.
           valor_indice_pulso_central = localizar_indice_pulso_central(n_janelamento, Matriz_H_linhas_removidas, linha_pulso_central)
           
           # A função metodo_desconvolucao_vetor_amplitude_estimada retorna o vetor da amplitude estimada.
           vetor_amplitude_estimada = metodo_desconvolucao_vetor_amplitude_estimada(vetor_pulsos_sinais, Matriz_H_linhas_removidas)
           
           # A amplitude estimada é definida como aquela de índice igual ao valor do índice do pulso central do vetor da amplitude estimada.
           amplitude_estimada = vetor_amplitude_estimada[valor_indice_pulso_central]
         
        # Cálculo do erro de estimação da amplitude.
        erro_amplitude = valor_amplitude_referencia-amplitude_estimada
    
        # O elemento erro_estimacao_amplitude é adicionado na lista correspondente.    
        lista_erro_estimacao_amplitude.append(erro_amplitude)

    # A função retorna a lista lista_erro_estimacao_amplitude.
    return lista_erro_estimacao_amplitude

### -------------------------------------------------------------------------------------------------------------------------------------------- ###
