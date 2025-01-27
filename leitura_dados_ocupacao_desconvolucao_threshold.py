# EXPERIMENTO ATLAS - Reconstrução de sinal - Método de Desconvolução de Sinal Versão Threshold Caso P = N - Estimação da amplitude.
# Autor: Guilherme Barroso Morett.
# Data: 29 de julho de 2024.

# Objetivo do código: realização da leitura dos dados de ocupação no formato free running.

""" 
Organização do código:

Leitura dos dados de entrada de acordo com o janelamento desejado.
Os dados de entrada das ocupações no formato de arquivo texto (txt) contém informações sobre os pulsos de sinais (ADC Count), a amplitude de referência (ADC Count) e a fase de referência (ns).
O valor de referência considerado para o pedestal foi 30 ADC Count.

Funções presentes:

1) Função para a leitura dos dados de ocupação.
Entrada: número de ocupação.
Saída: matriz dos dados de ocupação.

2) Função para a retirada do pedestal dos pulsos de sinais.
Entrada: matriz dos dados de ocupação.
Saída: matriz dos dados de ocupação sem o valor do pedestal na coluna dos pulsos de sinais.

3) Função para a construção da matriz dos pulsos de sinais e o vetor do parâmetro de referência.
Entrada: Matriz dos dados de ocupação.
Saída: Matriz dos pulsos de sinais com a quantidade de linhas de acordo com o janelamento proposto, vetor da amplitude de referência e o vetor da fase de referência.

"""

# Importação das bibliotecas.
import numpy as np
import os

### ---------------------------------------- 1) FUNÇÃO PARA A LEITURA DOS DADOS DE OCUPAÇÃO -------------------------------------------------- ###

# Definição da função para a leitura dos dados de ocupação no formato free running.
def leitura_dados_ocupacao(n_ocupacao):

    # Nome da pasta em que se encontra o arquivo de entrada das ocupações.
    pasta_dados_ocupacao = "Dados_Ocupacoes_Free_Running"

    # Nome do arquivo de entrada das ocupações.
    arquivo_dados_ocupacao = f"OC_{n_ocupacao}.txt"

    # O caminho para esse arquivo de entrada das ocupações.
    caminho_arquivo_dados_ocupacao = os.path.join(pasta_dados_ocupacao, arquivo_dados_ocupacao)

    # Caso o caminho especificado exista.
    if os.path.exists(caminho_arquivo_dados_ocupacao):
    
        # Abre o aquivo de entrada no modo leitura.
        with open(caminho_arquivo_dados_ocupacao,"r") as arquivo_entrada_ocupacoes:
        
            # Armazena os dados na variável Matriz_Dados_OC.
            Matriz_Dados_OC = np.array(np.loadtxt(arquivo_entrada_ocupacoes, skiprows = 1, dtype = 'double', delimiter = ','))
 
    # Caso contrário.       
    else:
    
        # Impressão de mensagem que o arquivo de entrada não existe.
        print(f"O arquivo {arquivo_dados_ocupacao} não existe na pasta {pasta_dados_ocupacao}.")

    # Obs.: da forma que o programa está escrito, os arquivos de entrada devem estar em uma pasta em que está o código do programa.
    # Caso deseja-se alterar isso basta mudar o endereço do arquivo.
    
    # A função retorna a matriz Matriz_Dados_OC.
    return Matriz_Dados_OC

### ------------------------------------------------------------------------------------------------------------------------------------------ ###

### ---------------------------------- 2) FUNÇÃO PARA A RETIRADA DO PEDESTAL DOS PULSOS DE SINAIS -------------------------------------------- ###

# Definição da função para a retirada do pedestal dos dados de entrada dos pulsos de sinais.
def retirada_pedestal(Matriz_Dados_OC):

    # A variável linhas_Matriz_Dados_OC armazena a quantidade de linhas da matriz Matriz_Dados_OC.
    linhas_Matriz_Dados_OC = len(Matriz_Dados_OC)

    # Construção de uma matriz em que a coluna unitária corresponde ao pulsos de sinais do arquivo de entrada.
    Matriz_Pedestal = [[0, 1, 0, 0] for i in range(linhas_Matriz_Dados_OC)]

    # Conversão dessa matriz para o tipo numpy array.
    Matriz_Pedestal = np.array(Matriz_Pedestal)

    # Definição do valor do pedestal.
    valor_pedestal = 30

    # Pedestal é uma matriz em que a coluna não nula correponde aos pulsos de sinais do arquivo de entrada.
    Pedestal = valor_pedestal*Matriz_Pedestal

    # Subtração dos pulsos de sinais o valor do pedestal e armazenamento na matriz Matriz_Dados_OC_sem_pedestal.
    Matriz_Dados_OC_Sem_Pedestal =  Matriz_Dados_OC-Pedestal
    
    # A função retorna a Matriz_Dados_OC sem o valor do pedestal.
    return Matriz_Dados_OC_Sem_Pedestal

### ------------------------------------------------------------------------------------------------------------------------------------------ ###

### ---------------- 3) FUNÇÃO PARA A CONSTRUÇÃO DA MATRIZ DOS PULSOS DE SINAIS E O VETOR DO PARÂMETRO DE REFERÊNCIA ------------------------- ###

# Definição da função que separa o vetor das amostras de pulsos de sinais e os pulsos de referência.
def amostras_pulsos_e_referencia(Matriz_Dados_OC):

    # A variável indice_pulsos_sinais armazena o índice da coluna que contém os pulsos de sinais.
    indice_pulsos_sinais = 1
    
    # A variável indice_amplitude_referencia armazena o índice da coluna que contém as amplitudes de referência.
    indice_amplitude_referencia = 2
    
    # A variável indice_fase_referencia armazena o índice da coluna que contém as fases de referência.
    indice_fase_referencia = 3

    # Definição do vetor das amostras de pulsos de sinais.
    vetor_amostras_pulsos = Matriz_Dados_OC[:, indice_pulsos_sinais]

    # Definição do vetor que contém os valores de referência para a amplitude.
    vetor_amplitude_referencia = Matriz_Dados_OC[:, indice_amplitude_referencia]
    
    # Definição do vetor que contém os valores de referência para a fase.
    vetor_fase_referencia = Matriz_Dados_OC[:, indice_fase_referencia]
    
    # A função retorna os vetores das amostras de pulsos, amplitude de referência e a fase de referência.
    return vetor_amostras_pulsos, vetor_amplitude_referencia, vetor_fase_referencia

# Definição da função amostras_janelamento para a construção da matriz de pulsos de sinais e o vetor de parâmetros de referência de acordo com o janelamento.
def amostras_janelamento(amostras, parametro_referencia, n_janelamento):

    # Criação da lista vazia Matriz_dados_pulsos.
    Matriz_dados_pulsos = []

    # Criação da lista vazia vetor_parametro_referencia.
    vetor_parametro_referencia = []

    # Criação do índice j que inicialmente é atribuído como nulo.
    j = 0

    # Enquanto o índice j for menor ou igual ao número de amostras menos a quantidade de janelamento.
    while j <= (len(amostras)-n_janelamento):

        # O dado especificado (uma lista que forma as linhas da matriz) é acrescentado a lista Matriz_dados_pulsos.
        Matriz_dados_pulsos.append(amostras[j : j+n_janelamento])
        # Acréscimo unitário no índice j.
        j += 1

    # Conversão da lista Matriz_dados_pulsos para um array (matriz).   
    Matriz_Dados_Pulsos = np.array(Matriz_dados_pulsos)

    # Definição do índice i.
    i = (n_janelamento-1)//2

    # Criação do índice k que inicialmente é atribuído como nulo.
    k = 0

    # Enquanto k for menor ou igual a quantidade de amostras menos o janelamento.
    while k <= (len(amostras)-n_janelamento):
    
        # O dado especificado é acrescentado na lista vetor_parametro_referencia. 
        vetor_parametro_referencia.append(parametro_referencia[i])
    
        # Incremento unitário no índice i.
        i += 1
    
        # Incremento unitário no índice k.
        k += 1

    # Conversão da lista vetor_parametro_referencia para um array (vetor).
    vetor_parametro_referencia = np.array(vetor_parametro_referencia)

    # A função retorna a matriz Matriz_Dados_Pulsos e o vetor vetor_parametro_referencia.
    return Matriz_Dados_Pulsos, vetor_parametro_referencia

### ------------------------------------------------------------------------------------------------------------------------------------------ ###