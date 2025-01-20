# EXPERIMENTO ATLAS - Reconstrução de sinal - Método de Desconvolução de Sinal Versão Threshold Caso P = N - Estimação da amplitude.
# Autor: Guilherme Barroso Morett.
# Data: 29 de julho de 2024.

# Objetivo do código: gráfico dos dados estatísticos ao longo das ocupações de acordo com o janelamento para o método de Desconvolução de Sinal Versão Threshold.

""" 
Organização do Código:

Leitura dos dados estatísticos de todas as ocupações para um determinado janelamento.

Funções presentes:

1) Função para a leitura dos dados estatísticos de todas as ocupações para um determinado janelamento pelo método de Desconvolução de Sinal Versão Threshold.
Entrada: número de janelamento.
Saída: Matriz com os dados de entrada organizados de acordo com a coluna (número da ocupação, média, variância e desvio padrão do erro de estimação da amplitude).

2) Instrução para o plote do gráfico do dado estatístico ao longo das ocupações para um determinado janelamento pelo método de Desconvolução de Sinal Versão Threshold.
Entrada: dado estatístico desejado (média, variância ou desvio padrão) e a matriz dos dados.
Saída: nada.

3) Instrução principal do código.
Entrada: nada.
Saída: nada.
"""

# Importação das bibliotecas.
import numpy as np
import matplotlib.pyplot as plt
import os
from termcolor import colored

# Impressão de uma linha que representa o início do programa.
print("\n-------------------------------------------------------------------------------------------------------------------------------------\n")

# Título do programa.

# A variável titulo_programa armazena o título em negrito.
titulo_programa = colored("Plote do gráfico do dado estatístico do erro de estimação da amplitude ao longo das ocupações para um determinado janelamento pelo método de Desconvolução de Sinal Versão Threshold:\n", attrs=["bold"])

# Impressão do título do programa.
print(titulo_programa)

### --- 1) FUNÇÃO PARA A LEITURA DOS DADOS ESTATÍSTICOS DE TODAS AS OCUPAÇÕES PARA UM DETERMINADO JANELAMENTO PELO MÉTODO DESCONVOLUÇÃO DE SINAL THRESHOLD --- ###

# Definição da função para a leitura dos dados estatísticos de todas as ocupações para um determinado janelamento pelo método de Desconvolução de Sinal Versão Threshold.
def leitura_dados_estatisticos_janelamento_amplitude_desconvolucao_threshold(n_janelamento):

    # Nome da pasta em que se encontra o arquivo de entrada dos dados estatísticos de acordo com o janelamento.
    pasta_dados_estatisticos_janelamento = "Dados_Estatisticos_Desconvolucao_Threshold_OC"

    # Nome do arquivo de entrada dos dados estatísticos de acordo com o janelamento.
    arquivo_dados_estatisticos_janelamento = f"dados_estatisticos_desconvolucao_threshold_janelamento_{n_janelamento}.txt"

    # O caminho para esse arquivo de entrada das ocupações.
    caminho_arquivo_dados_estatisticos_janelamento = os.path.join(pasta_dados_estatisticos_janelamento, arquivo_dados_estatisticos_janelamento)

    # Caso o caminho especificado exista.
    if os.path.exists(caminho_arquivo_dados_estatisticos_janelamento):
    
        # Abre o aquivo de entrada no modo leitura.
        with open(caminho_arquivo_dados_estatisticos_janelamento,"r") as arquivo_entrada_dados_estatisticos_janelamento:
        
            # Armazena os dados na variável Matriz_Dados_Estatisticos_Janelamento.
            Matriz_Dados_Estatisticos_Janelamento = np.array(np.loadtxt(arquivo_entrada_dados_estatisticos_janelamento, skiprows = 1, dtype = 'double', delimiter = ','))
 
    # Caso contrário.       
    else:
    
        # Impressão de mensagem que o arquivo de entrada não existe.
        print(f"O arquivo {arquivo_dados_estatisticos_janelamento} não existe na pasta {pasta_dados_estatisticos_janelamento}.")

    # Obs.: da forma que o programa está escrito, os arquivos de entrada devem estar em uma pasta em que está o código do programa.
    # Caso deseja-se alterar isso basta mudar o endereço do arquivo.
    
    # A função retorna a matriz Matriz_Dados_Estatisticos_Janelamento.
    return Matriz_Dados_Estatisticos_Janelamento

### ------------------------------------------------------------------------------------------------------------------------------------------ ###

### --- 2) INSTRUÇÃO PARA O PLOTE DO GRÁFICO DOS DADOS ESTATÍSTICOS AO LONGO DAS OCUPAÇÕES PARA UM DETERMINADO JANELAMENTO PELO MÉTODO DESCONVOLUÇÃO DE SINAL THRESHOLD ------ ###

# Definição da instrução para o plote do gráfico do dado estatístico ao longo das ocupações para um determinado janelamento pelo método de Desconvolução de Sinal Versão Threshold.
def grafico_dado_estatistico_janelamento_amplitude_desconvolucao_threshold(dado_estatistico, Matriz_Dados_Estatisticos_Janelamento):
    
    # Definição da variável indice_coluna_ocupações que armazena o valor do índice da coluna das ocupações.
    indice_coluna_ocupacoes = 0
    
    # Definição da variável indice_coluna_media que armazena o valor do índice da coluna das médias.
    indice_coluna_media = 1
    
    # Definição da variável indice_coluna_var que armazena o valor do índice da coluna das variâncias.
    indice_coluna_var = 2
    
    # Definição da variável indice_coluna_DP que armazena o valor do índice da coluna dos desvios padrão.
    indice_coluna_DP = 3
    
    # Definição do eixo das abscissas.
    vetor_ocupacoes = Matriz_Dados_Estatisticos_Janelamento[: , indice_coluna_ocupacoes]
    
    # Comando para o nome do eixo das abscissas.
    plt.xlabel("Ocupação", fontsize = 18)
    
    # Definição do tamanho dos números presentes no eixo das abscissas.
    plt.xticks(fontsize = 16)
    
    # Caso a variável dado_estatatístico seja 1 (média).
    if dado_estatistico == 1:
        
        # Definição do vetor dos dados estatísticos.
        vetor_dados = Matriz_Dados_Estatisticos_Janelamento[: , indice_coluna_media]
        
        # Comando para o nome do eixo das ordenadas.
        plt.ylabel("Média do erro de estimação da amplitude (ADC Count)", fontsize = 18)
        
    # Caso a variável dado_estatístico seja 2 (variância).
    elif dado_estatistico == 2:
        
        # Definição do vetor dos dados estatísticos.
        vetor_dados = Matriz_Dados_Estatisticos_Janelamento[: , indice_coluna_var]
        
        # Comando para o nome do eixo das ordenadas.
        plt.ylabel("Var. do erro de estimação da amplitude (ADC Count)", fontsize = 18)
        
    # Caso a variável dado_estatistico seja 3 (desvio padrão).
    elif dado_estatistico == 3:
        
        # Definição do vetor dos dados estatísticos.
        vetor_dados = Matriz_Dados_Estatisticos_Janelamento[: , indice_coluna_DP]
        
        # Comando para o nome do eixo das ordenadas.
        plt.ylabel("DP. do erro de estimação da amplitude (ADC Count)", fontsize = 18)
        
    # Definição do tamanho dos números do eixo das ordenadas.
    plt.yticks(fontsize = 16)
    
    # Comando para o plote do gráfico.
    plt.plot(vetor_ocupacoes, vetor_dados, color='blue', linestyle='--', marker='o')
    
    # Comando para o grid.
    plt.grid()
    
    # Comando para o plote.
    plt.show()
        
### ------------------------------------------------------------------------------------------------------------------------------------------ ###        
        
### -------------------------------------------------- 3) INSTRUÇÃO PRINCIPAL DO CÓDIGO ------------------------------------------------------ ###

# Definição da instrução principal do código.
def principal_grafico_dado_estatistico_janelamento_desconvolucao_threshold():
    
    # Impressão de mensagem no terminal.
    print("Opções de análise:\nMédia: 1\nVariância: 2\nDesvio padrão: 3\n")

    # A variável dado_estatistico armazena o número do tipo inteiro digitado pelo usuário via terminal.
    dado_estatistico = int(input("Digite o número da opção desejada: "))

    # A variável valores_dados é uma lista com os valores aceitáveis para opcao.
    valores_dados = list(range(1,4,1))

    # Caso o valor digitado armazenado na variável dado_estatistico não estiver presente na lista valores_dados.
    if dado_estatistico not in valores_dados:
    
        # Exibição de uma mensagem de alerta de que a opcao solicitada é inválida.
        print("Essa opção é inválida!")
        print("---------------------------------------------------------------------------------------------------------------------------------")
        # A execução do programa é interrompida.
        exit(1)
    
    # A variável n_janelamento armazena a quantidade de janelamento especificada no terminal pelo usuário.
    n_janelamento = int(input("Digite a quantidade de janelamento: "))

    # A variável valores_janelamento é uma lista com os valores aceitáveis do janelamento de 7 até 19 com incremento de dois.
    valores_janelamento = list(range(7,20,2))

    # Caso o valor digitado armazenado na variável n_janelamento não estiver presente na lista valores_janelamento.
    if n_janelamento not in valores_janelamento:
    
        # Exibição de uma mensagem de alerta de que a quantidade de janelamento solicitada é inválida.
        print("Quantidade de janelamento inválida! Opções de janelamento: 7, 9, 11, 13, 15, 17, 19.")
        print("---------------------------------------------------------------------------------------------------------------------------------")
        # A execução do programa é interrompida.
        exit(1)
        
    # Chamada das funções.
    
    Matriz_Dados_Estatisticos_Janelamento = leitura_dados_estatisticos_janelamento_amplitude_desconvolucao_threshold(n_janelamento)
    
    grafico_dado_estatistico_janelamento_amplitude_desconvolucao_threshold(dado_estatistico, Matriz_Dados_Estatisticos_Janelamento)
    
# Chamada da instrução principal do código.
principal_grafico_dado_estatistico_janelamento_desconvolucao_threshold()

### ------------------------------------------------------------------------------------------------------------------------------------------ ###

# Impressão de uma linha que representa o fim do programa.
print("\n-------------------------------------------------------------------------------------------------------------------------------------\n")
    
    
            
    
    
    
    