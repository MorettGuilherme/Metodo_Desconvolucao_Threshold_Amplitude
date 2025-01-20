# EXPERIMENTO ATLAS - Reconstrução de sinal - Método de Desconvolução de Sinal Versão Threshold Caso P = N - Estimação da amplitude.
# Autor: Guilherme Barroso Morett.
# Data: 29 de julho de 2024.

# Objetivo do código: análise do erro de estimação da amplitude pelo método de Desconvolução de Sinal Versão Threshold.

"""
Organização do Código:

Importação de arquivos.
Leitura dos dados de ocupação: leitura_dados_ocupacao_desconvolucao_threshold.py
Método de Desconvolução: metodo_desconvolucao_threshold.py

Funções presentes:

1) Função para o cálculo da estatística do erro de estimação da amplitude pelo método de Desconvolução de Sinal Versão Threshold.
Entrada: lista com os erros de estimação da amplitude.
Saída: a média, a variância e o desvio padrão do erro de estimação da amplitude.

2) Instrução para o plote do histograma do erro de estimação da amplitude pelo método de Desconvolução de Sinal Versão Threshold.
Entrada: lista com os erros de estimação da amplitude e seus dados estatísticos.
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

# Importação dos arquivos.
from leitura_dados_ocupacao_desconvolucao_threshold import *
from metodo_desconvolucao_P_igual_N_threshold import *

# Impressão de uma linha que representa o início do programa.
print("\n-------------------------------------------------------------------------------------------------------------------------------------\n")

# Título do programa.

# A variável titulo_programa armazena o título em negrito.
titulo_programa = colored("Análise do erro de estimação da amplitude pelo método de Desconvolução de Sinal Versão Threshold:\n", attrs=["bold"])

# Impressão do título do programa.
print(titulo_programa)

### ----- 1) FUNÇÃO PARA O CÁLCULO DOS DADOS ESTATÍSTICOS DO ERRO DE ESTIMAÇÃO DA AMPLITUDE PELO MÉTODO DE DESCONVOLUÇÃO DE SINAL THRESHOLD ----- ###

# Definição da função para o cálculo dos dados estatísticos do erro de estimação da amplitude pelo método de Desconvolução de Sinal Versão Threshold.
def dados_estatisticos_erro_estimacao_amplitude_desconvolucao_threshold(lista_erro_estimacao_amplitude):
    
    # A lista do erro de estimação da amplitude é convertida para o tipo numpy array.
    vetor_erro_estimacao_amplitude = np.array(lista_erro_estimacao_amplitude)

    # Cálculo da média do erro de estimação da amplitude.
    media_erro_estimacao_amplitude = np.mean(vetor_erro_estimacao_amplitude)

    # Cálculo da variância do erro de estimação da amplitude.
    var_erro_estimacao_amplitude = np.var(vetor_erro_estimacao_amplitude)

    # Cálculo do desvio padrão do erro de estimação da amplitude.
    desvio_padrao_erro_estimacao_amplitude = np.std(vetor_erro_estimacao_amplitude)
    
    # A função retorna a média, a variância e o desvio padrão dos dados do erro de estimação da amplitude.
    return media_erro_estimacao_amplitude, var_erro_estimacao_amplitude, desvio_padrao_erro_estimacao_amplitude
    
### ------------------------------------------------------------------------------------------------------------------------------------------ ###

### --- 2) INSTRUÇÃO PARA A CONSTRUÇÃO DO HISTOGRAMA DO TIPO A DO ERRO DE ESTIMAÇÃO DA AMPLITUDE PELO MÉTODO DE DESCONVOLUÇÃO DE SINAL THRESHOLD --- ###

# Definição da instrução para a confecção do histograma do tipo A do erro de estimação da amplitude pelo método de Desconvolução de Sinal Versão Threshold.
def histograma_A_erro_estimacao_amplitude_desconvolucao_threshold(n_ocupacao, lista_erro_estimacao_amplitude, media_erro_estimacao_amplitude, var_erro_estimacao_amplitude, desvio_padrao_erro_estimacao_amplitude):
    
    # A lista do erro de estimação da amplitude é convertida para o tipo numpy array.
    vetor_erro_estimacao_amplitude = np.array(lista_erro_estimacao_amplitude)

    # Nomeação do eixo x de acordo com o termo da amplitude.
    plt.xlabel('Erro de estimação da amplitude (ADC Count)', fontsize = 18)

    # Definição do tamanho dos números do eixo x.    
    plt.xticks(fontsize = 16)

    # Nomeação do eixo y.
    plt.ylabel('Número de eventos', fontsize = 18)
    
    # Definição do tamanho dos números do eixo y.
    plt.yticks(fontsize = 16)
    
    # A variável n_bins recebe a quantidade de bins presente no histograma.
    n_bins = 100
    
    # A variável x_inf recebe o valor inferior do eixo das abscissas para a amplitude.
    x_inf = -300
    
    # A variável x_sup recebe o valor superior do eixo das abscissas para a amplitude.
    x_sup = 300

    # Definição do tamanho dos números do eixo x.    
    plt.xticks(fontsize = 16)

    # Nomeação do eixo y.
    plt.ylabel('Número de eventos', fontsize = 18)
    
    # Definição do tamanho dos números do eixo y.
    plt.yticks(fontsize = 16)
    
    # A variável n_bins recebe a quantidade de bins presente no histograma.
    n_bins = 100
    
    # Conversão das variáveis para strings adaptadas para o sistema numérico brasileiro.

    media_erro_estimacao_amplitude = round(media_erro_estimacao_amplitude, 6)
    media_erro_estimacao_amplitude = str(media_erro_estimacao_amplitude).replace('.', ',')
    
    var_erro_estimacao_amplitude = round(var_erro_estimacao_amplitude, 6)
    var_erro_estimacao_amplitude= str(var_erro_estimacao_amplitude).replace('.', ',')
    
    desvio_padrao_erro_estimacao_amplitude = round(desvio_padrao_erro_estimacao_amplitude, 6)
    desvio_padrao_erro_estimacao_amplitude = str(desvio_padrao_erro_estimacao_amplitude).replace('.', ',')

    # A variável texto recebe uma string com as informações de interesse.
    texto = f"Média: {media_erro_estimacao_amplitude} \n Variância: {var_erro_estimacao_amplitude} \n Desvio padrão: {desvio_padrao_erro_estimacao_amplitude}"

    # Impressão do título do gráfico (recomendável para a apresentação de slides).
    # plt.title(f"Ocupação {n_ocupacao}", fontsize = 18)

    # Definição do histograma a partir do vetor vetor_erro_parametro.
    plt.hist(vetor_erro_estimacao_amplitude, bins = n_bins, range = [x_inf, x_sup], edgecolor = 'black', linewidth = 1.2)
    
    # Posicionamento do texto no gráfico.
    plt.text(0.99, 0.98, texto, horizontalalignment = 'right',
    verticalalignment = 'top',
    transform = plt.gca().transAxes,
    bbox = dict(facecolor = 'white', alpha = 0.5),
    fontsize = 14)

    # Criação de grid.
    plt.grid()

    # Exibição do gráfico.
    plt.show()

### ------------------------------------------------------------------------------------------------------------------------------------------ ###

### ---- 3) INSTRUÇÃO PARA A CONSTRUÇÃO DO HISTOGRAMA DO TIPO B DO ERRO DE ESTIMAÇÃO DA AMPLITUDE PELO MÉTODO DESCONVOLUÇÃO DE SINAL THRESHOLD ---- ###

# Definição de instrução para o plot dos histogramas do tipo B do erro de estimação da amplitude para diferentes janelamentos para uma dada ocupação pelo método Desconvolução de Sinal Versão Threshold.
def histograma_B_erro_estimacao_amplitude_desconvolucao_threshold(n_ocupacao, lista_erro_estimacao_amplitude_J7, media_erro_estimacao_amplitude_J7, var_erro_estimacao_amplitude_J7, desvio_padrao_erro_estimacao_amplitude_J7, lista_erro_estimacao_amplitude_J17, media_erro_estimacao_amplitude_J17, var_erro_estimacao_amplitude_J17, desvio_padrao_erro_estimacao_amplitude_J17, lista_erro_estimacao_amplitude_J19, media_erro_estimacao_amplitude_J19, var_erro_estimacao_amplitude_J19, desvio_padrao_erro_estimacao_amplitude_J19):
    
    # A lista do erro de estimação da amplitude para o janelamento 7 é convertida para o tipo numpy array.
    vetor_erro_estimacao_amplitude_J7 = np.array(lista_erro_estimacao_amplitude_J7)
    
    # A lista do erro de estimação da amplitude para o janelamento 15 é convertida para o tipo numpy array.
    vetor_erro_estimacao_amplitude_J17 = np.array(lista_erro_estimacao_amplitude_J17)
    
    # A lista do erro de estimação da amplitude para o janelamento 19 é convertida para o tipo numpy array.
    vetor_erro_estimacao_amplitude_J19 = np.array(lista_erro_estimacao_amplitude_J19)

    # Nomeação do eixo x de acordo com o termo da amplitude.
    plt.xlabel("Erro de estimação da amplitude (ADC Count)", fontsize = 18)
        
    # Definição do tamanho dos números do eixo x.    
    plt.xticks(fontsize = 16)

    # Nomeação do eixo y.
    plt.ylabel('Número de eventos', fontsize = 18)
    
    # Definição do tamanho dos números do eixo y.
    plt.yticks(fontsize = 16)
    
    # A variável n_bins recebe a quantidade de bins presente no histograma.
    n_bins = 100
    
    # A variável x_inf recebe o valor inferior do eixo das abscissas.
    x_inf = -300
    
    # A variável x_sup recebe o valor superior do eixo das abscissas.
    x_sup = 300
    
    # Conversão das variáveis para strings adaptadas para o sistema numérico brasileiro.
    
    media_erro_estimacao_amplitude_J7 = round(media_erro_estimacao_amplitude_J7, 6)
    media_erro_estimacao_amplitude_J7 = str(media_erro_estimacao_amplitude_J7).replace('.', ',')
    
    var_erro_estimacao_amplitude_J7 = round(var_erro_estimacao_amplitude_J7, 6)
    var_erro_estimacao_amplitude_J7 = str(var_erro_estimacao_amplitude_J7).replace('.', ',')
    
    desvio_padrao_erro_estimacao_amplitude_J7 = round(desvio_padrao_erro_estimacao_amplitude_J7, 6)
    desvio_padrao_erro_estimacao_amplitude_J7 = str(desvio_padrao_erro_estimacao_amplitude_J7).replace('.', ',')
    
    media_erro_estimacao_amplitude_J17 = round(media_erro_estimacao_amplitude_J17, 6)
    media_erro_estimacao_amplitude_J17 = str(media_erro_estimacao_amplitude_J17).replace('.', ',')
    
    var_erro_estimacao_amplitude_J17 = round(var_erro_estimacao_amplitude_J17, 6)
    var_erro_estimacao_amplitude_J17 = str(var_erro_estimacao_amplitude_J17).replace('.', ',')
    
    desvio_padrao_erro_estimacao_amplitude_J17 = round(desvio_padrao_erro_estimacao_amplitude_J17, 6)
    desvio_padrao_erro_estimacao_amplitude_J17 = str(desvio_padrao_erro_estimacao_amplitude_J17).replace('.', ',')
    
    media_erro_estimacao_amplitude_J19 = round(media_erro_estimacao_amplitude_J19, 6)
    media_erro_estimacao_amplitude_J19 = str(media_erro_estimacao_amplitude_J19).replace('.', ',')
    
    var_erro_estimacao_amplitude_J19 = round(var_erro_estimacao_amplitude_J19, 6)
    var_erro_estimacao_amplitude_J19 = str(var_erro_estimacao_amplitude_J19).replace('.', ',')
    
    desvio_padrao_erro_estimacao_amplitude_J19 = round(desvio_padrao_erro_estimacao_amplitude_J19, 6)
    desvio_padrao_erro_estimacao_amplitude_J19 = str(desvio_padrao_erro_estimacao_amplitude_J19).replace('.', ',')
    
    
    # A variável legenda_J7 recebe a legenda do histograma para o janelamento 7.
    legenda_J7 = f'Janelamento 7\nMédia: {media_erro_estimacao_amplitude_J7}\nVariância: {var_erro_estimacao_amplitude_J7}\nDesvio Padrão: {desvio_padrao_erro_estimacao_amplitude_J7}'
    
    # A variável legenda_J15 recebe a legenda do histograma para o janelamento 15.
    legenda_J15 = f'Janelamento 17\nMédia: {media_erro_estimacao_amplitude_J17}\nVariância: {var_erro_estimacao_amplitude_J17}\nDesvio Padrão: {desvio_padrao_erro_estimacao_amplitude_J17}'
    
    # A variável legenda_J19 recebe a legenda do histograma para o janelamento 19.
    legenda_J19 = f'Janelamento 19\nMédia: {media_erro_estimacao_amplitude_J19}\nVariância: {var_erro_estimacao_amplitude_J19}\nDesvio Padrão: {desvio_padrao_erro_estimacao_amplitude_J19}'
    
    # Definição dos histogramas para diferentes janelamentos e uma dada ocupação.
    plt.hist(vetor_erro_estimacao_amplitude_J7, bins = n_bins, color='blue', range = [x_inf, x_sup], histtype = 'step', label = legenda_J7)
    plt.hist(vetor_erro_estimacao_amplitude_J17, bins = n_bins, color='green', range = [x_inf, x_sup], histtype = 'step', label = legenda_J15)
    plt.hist(vetor_erro_estimacao_amplitude_J19, bins = n_bins, color='red', range = [x_inf, x_sup], histtype = 'step', label = legenda_J19)
    
    # Definição do título do histograma.
    plt.title(f"Ocupação {n_ocupacao}", fontsize = 16)
    
    # Definição da legenda do histograma.
    plt.legend(fontsize = 14)

    # Criação de grid.
    plt.grid()

    # Exibição do gráfico.
    plt.show()

### ------------------------------------------------------------------------------------------------------------------------------------------ ###

### ------------------------------------ 3) INSTRUÇÃO PRINCIPAL DO CÓDIGO -------------------------------------------------------------------- ###

# Definição da instrução principal do código.
def principal_histograma_erro_amplitude_desconvolucao_threshold():
    
# A variável n_ocupacao armazena o valor digitado da ocupação desejada no terminal pelo usuário.
    n_ocupacao = float(input("Digite o valor da ocupação desejada: "))

    # A variável valores_ocupacao é uma lista com os valores aceitáveis de ocupação de 0 até 100.
    valores_ocupacao = list(range(0,101,10))

    # Caso o valor digitado armazenado na variável n_ocupacao não estiver presente na lista valores_ocupacao.
    if n_ocupacao not in valores_ocupacao:
    
        # Exibição de uma mensagem de alerta de que a ocupação solicitada é inválida.
        print("\nNúmero de ocupação inválida!\n")
        # A execução do programa é interrompida.
        exit(1) 

    # O tipo da variável n_ocupacao é convertida para inteiro.
    # Obs.: essa conversão possibilita que a leitura do arquivo possa ser feita corretamente.
    n_ocupacao = int(n_ocupacao)
    
    # Impressão de mensagem no terminal.
    print("Opções de histogramas:\nA: histograma para um dado janelamento e ocupação.\nB: histogramas para os janelamentos 7, 15 e 19 para a ocupação desejada.")
    
    # A variável tipo_histograma armazena a string digitada pelo usuário.
    tipo_histograma = str(input("Digite a opção do histograma desejada: "))
    
    # A variável valores_histogramas é uma lista com os valores aceitáveis para a variável tipo_histograma.
    valores_histogramas = ["A", "B"]
    
    # Caso o valor digitado armazenado na variável tipo_histograma não estiver presente na lista valores_histogramas.
    if tipo_histograma not in valores_histogramas:
    
        # Exibição de uma mensagem de alerta de que a opção do tipo de histograma é inválida.
        print("A opção do tipo de histograma digitada é inválida!")
        print("---------------------------------------------------------------------------------------------------------------------------------")
        # A execução do programa é interrompida.
        exit(1)
    
    # Caso a variável tipo_histograma seja "A".
    if tipo_histograma == "A":
    
        # A variável n_janelamento armazena a quantidade de janelamento especificada no terminal pelo usuário.
        n_janelamento = int(input("Digite a quantidade de janelamento: "))

        # A variável valores_janelamento é uma lista com os valores aceitáveis do janelamento de 7 até 19 com incremento de dois.
        valores_janelamento = list(range(7,20,2))

        # Caso o valor digitado armazenado na variável n_janelamento não estiver presente na lista valores_janelamento.
        if n_janelamento not in valores_janelamento:
    
            # Exibição de uma mensagem de alerta de que a quantidade de janelamento solicitada é inválida.
            print("Quantidade de janelamento inválida! Opções de janelamento: 7, 9, 11, 13, 15, 17, 19.")
            print("-----------------------------------------------------------------------------------------------------------------------------")
            # A execução do programa é interrompida.
            exit(1)
            
        # Chamada ordenada das funções.
    
        Matriz_Dados_OC = leitura_dados_ocupacao(n_ocupacao) 
    
        Matriz_Dados_OC_Sem_Pedestal = retirada_pedestal(Matriz_Dados_OC)
    
        vetor_amostras_pulsos, vetor_amplitude_referencia, vetor_fase_referencia = amostras_pulsos_e_referencia(Matriz_Dados_OC_Sem_Pedestal)
        
        Matriz_Pulsos_Sinais_Janelado, vetor_amplitude_referencia_janelado = amostras_janelamento(vetor_amostras_pulsos, vetor_amplitude_referencia, n_janelamento)

        # Chamada ordenada das funções.
    
        lista_erro_estimacao_amplitude = metodo_desconvolucao_threshold_P_igual_N(n_janelamento, Matriz_Pulsos_Sinais_Janelado, vetor_amplitude_referencia_janelado)
        
        media_erro_estimacao_amplitude, var_erro_estimacao_amplitude, desvio_padrao_erro_estimacao_amplitude = dados_estatisticos_erro_estimacao_amplitude_desconvolucao_threshold(lista_erro_estimacao_amplitude)
    
        histograma_A_erro_estimacao_amplitude_desconvolucao_threshold(n_ocupacao, lista_erro_estimacao_amplitude, media_erro_estimacao_amplitude, var_erro_estimacao_amplitude, desvio_padrao_erro_estimacao_amplitude)
    
    # Caso a variável tipo_histograma seja "B".
    elif tipo_histograma == "B":
        
        # A variável n_janelamento_7 recebe a quantidade do janelamento 7.
        n_janelamento_J7 = 7
        # A variável n_janelamento_15 recebe a quantidade do janelamento 17.
        n_janelamento_J17 = 17
        # A variável n_janelamento_19 recebe a quantidade do janelamento 19.
        n_janelamento_J19 = 19
        
        # Chamada ordenada das funções.
    
        Matriz_Dados_OC = leitura_dados_ocupacao(n_ocupacao) 
    
        Matriz_Dados_OC_Sem_Pedestal = retirada_pedestal(Matriz_Dados_OC)
    
        vetor_amostras_pulsos, vetor_amplitude_referencia, vetor_fase_referencia = amostras_pulsos_e_referencia(Matriz_Dados_OC_Sem_Pedestal)
        
        Matriz_Pulsos_Sinais_Janelado_J7, vetor_amplitude_referencia_janelado_J7 = amostras_janelamento(vetor_amostras_pulsos, vetor_amplitude_referencia, n_janelamento_J7)
        Matriz_Pulsos_Sinais_Janelado_J17, vetor_amplitude_referencia_janelado_J17 = amostras_janelamento(vetor_amostras_pulsos, vetor_amplitude_referencia, n_janelamento_J17)
        Matriz_Pulsos_Sinais_Janelado_J19, vetor_amplitude_referencia_janelado_J19 = amostras_janelamento(vetor_amostras_pulsos, vetor_amplitude_referencia, n_janelamento_J19)
        
        # Chamada ordenada das funções.
    
        lista_erro_estimacao_amplitude_J7 = metodo_desconvolucao_threshold_P_igual_N(n_janelamento_J7, Matriz_Pulsos_Sinais_Janelado_J7, vetor_amplitude_referencia_janelado_J7)
        media_erro_estimacao_amplitude_J7, var_erro_estimacao_amplitude_J7, desvio_padrao_erro_estimacao_amplitude_J7 = dados_estatisticos_erro_estimacao_amplitude_desconvolucao_threshold(lista_erro_estimacao_amplitude_J7)
    
        lista_erro_estimacao_amplitude_J17 = metodo_desconvolucao_threshold_P_igual_N(n_janelamento_J17, Matriz_Pulsos_Sinais_Janelado_J17, vetor_amplitude_referencia_janelado_J17)
        media_erro_estimacao_amplitude_J17, var_erro_estimacao_amplitude_J17, desvio_padrao_erro_estimacao_amplitude_J17 = dados_estatisticos_erro_estimacao_amplitude_desconvolucao_threshold(lista_erro_estimacao_amplitude_J17)
    
        lista_erro_estimacao_amplitude_J19 = metodo_desconvolucao_threshold_P_igual_N(n_janelamento_J19, Matriz_Pulsos_Sinais_Janelado_J19, vetor_amplitude_referencia_janelado_J19)
        media_erro_estimacao_amplitude_J19, var_erro_estimacao_amplitude_J19, desvio_padrao_erro_estimacao_amplitude_J19 = dados_estatisticos_erro_estimacao_amplitude_desconvolucao_threshold(lista_erro_estimacao_amplitude_J19)
    
        histograma_B_erro_estimacao_amplitude_desconvolucao_threshold(n_ocupacao, lista_erro_estimacao_amplitude_J7, media_erro_estimacao_amplitude_J7, var_erro_estimacao_amplitude_J7, desvio_padrao_erro_estimacao_amplitude_J7, lista_erro_estimacao_amplitude_J17, media_erro_estimacao_amplitude_J17, var_erro_estimacao_amplitude_J17, desvio_padrao_erro_estimacao_amplitude_J17, lista_erro_estimacao_amplitude_J19, media_erro_estimacao_amplitude_J19, var_erro_estimacao_amplitude_J19, desvio_padrao_erro_estimacao_amplitude_J19)
    
# Chamada da instrução principal do código.
principal_histograma_erro_amplitude_desconvolucao_threshold()

### ------------------------------------------------------------------------------------------------------------------------------------------ ###

# Impressão de uma linha que representa o fim do programa.
print("\n-------------------------------------------------------------------------------------------------------------------------------------\n")