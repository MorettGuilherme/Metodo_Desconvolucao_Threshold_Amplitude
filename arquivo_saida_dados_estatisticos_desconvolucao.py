# EXPERIMENTO ATLAS - Reconstrução de sinal - Método de Desconvolução de Sinal - Estimação da amplitude.
# Autor: Guilherme Barroso Morett.
# Data: 28 de junho de 2024.

# Objetivo do código: geração de arquivos de saída baseados nos dados estatísticos dos histogramas do erro de estimação pelo método de Desconvolução de Sinal.

""" 
Organização do Código:

Importação de arquivos.
Leitura dos dados de ocupação: leitura_dados_ocupacao_desconvolucao.py
Método de Desconvolução: metodo_desconvolucao.py
Histograma do erro da estimação da amplitude pelo método de Desconvolução: histograma_erro_amplitude_desconvolucao.py

Funções presentes:

1) Função para o cálculo dos dados estatístico do erro de estimação da amplitude.
Entrada: lista com o erro de estimação da amplitude.
Saída: a média, a variância e o desvio padrão do erro de estimação.

2) Instrução para salvar os dados estatísticos do erro de estimação da amplitude para determinada ocupação em um arquivo de saída.
Entrada: a média, a variância e o desvio padrão do erro de estimação da amplitude.
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
from tqdm import tqdm
import time

# Importação dos arquivos.
from leitura_dados_ocupacao_desconvolucao import *
from metodo_desconvolucao_P_igual_N import *

# Impressão de uma linha que representa o início do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")

# Título do programa.

# A variável titulo_programa armazena o título em negrito.
titulo_programa = colored("Geração de arquivos de saída baseados nos dados estatísticos dos histogramas do erro de estimação pelo método de Desconvolução de Sinal - P = N:\n", attrs=["bold"])

# Impressão do título do programa.
print(titulo_programa)

### -------------------------- 1) FUNÇÃO PARA O CÁLCULO DOS DADOS ESTATÍSTICOS DO ERRO DE ESTIMAÇÃO DA AMPLITUDE ------------------------------- ###

# Definição da função para o cálculo dos dados estatísticos do erro de estimação da amplitude.
def dados_estatisticos_erro_amplitude(lista_erro_amplitude):
    
    # A lista do erro da amplitude é convertida para o tipo numpy array.
    vetor_erro_amplitude = np.array(lista_erro_amplitude)

    # Cálculo da média do erro de estimação da amplitude.
    media_erro_amplitude = np.mean(vetor_erro_amplitude)

    # Cálculo da variância do erro de estimação da amplitude.
    var_erro_amplitude = np.var(vetor_erro_amplitude)

    # Cálculo do desvio padrão do erro de estimação da amplitude.
    desvio_padrao_erro_amplitude = np.std(vetor_erro_amplitude)
    
    # A função retorna a média, a variância e o desvio padrão dos dados do erro de estimação da amplitude.
    return media_erro_amplitude, var_erro_amplitude, desvio_padrao_erro_amplitude
    
### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### ---------------- 2) INSTRUÇÃO PARA A IMPRESSÃO DOS DADOS ESTATÍSTICOS DO ERRO DE ESTIMAÇÃO DA AMPLITUDE EM UM ARQUIVO DE SAÍDA ------------- ###

# Definição da função para salvar os dados estatísticos do erro de estimação da amplitude em arquivo de saída.
def arquivo_saida_dados_estatisticos_erro_amplitude(n_ocupacao, n_janelamento, media_erro_amplitude, var_erro_amplitude, desvio_padrao_erro_amplitude):

    # Definição do título presente no arquivo de saída.
    titulo_arquivo_saida = "Oc,media_erro,var_Erro,desvio_padrao_erro\n"

    # Definição da pasta que contém o arquivo de saída.
    pasta_saida = "Dados_Estatisticos_Desconvolucao_OC"

    # Caso a pasta não exista.
    if not os.path.exists(pasta_saida):
        # Criação da pasta de saída.
        os.makedirs(pasta_saida)

    # Nome do arquivo de saída.
    arquivo_saida = f"dados_estatisticos_desconvolucao_janelamento_{n_janelamento}.txt"

    # Caminho completo para o arquivo de saída.
    caminho_arquivo_saida = os.path.join(pasta_saida, arquivo_saida)

    # Verifica se o arquivo existe e está vazio
    try:
        with open(caminho_arquivo_saida, 'r') as arquivo_saida_dados_estatisticos:
            primeiro_caractere = arquivo_saida_dados_estatisticos.read(1)
            if not primeiro_caractere:
                # Arquivo está vazio, escreva o título
                with open(caminho_arquivo_saida, 'a') as file:
                    file.write(titulo_arquivo_saida)
    except FileNotFoundError:
        # Se o arquivo não existe, cria e escreve o título
        with open(caminho_arquivo_saida, 'w') as file:
            file.write(titulo_arquivo_saida)

    # Comando para tentar realizar uma operação.
    try:
        # Abre o arquivo de saída no modo de acrescentar (append).
        with open(caminho_arquivo_saida, "a") as arquivo_saida_dados_estatisticos:
            # Escrita dos dados de interesse.
            arquivo_saida_dados_estatisticos.write(f"{n_ocupacao},{media_erro_amplitude},{var_erro_amplitude},{desvio_padrao_erro_amplitude}\n")
        
    # Excessão.
    except Exception as e:
        # Impressão de mensagem de alerta.
        print("Ocorreu um erro ao atualizar o arquivo de saída dos dados estatísticos:", str(e))

### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### -------------------------------------- 3) INSTRUÇÃO PRINCIPAL DO CÓDIGO (MAIN) ------------------------------------------------------------- ###

# Definição da função principal (main) para esse código.
def principal_arquivo_saida_dados_estatisticos_desconvolucao():
    
    # A variável ocupacao_inicial armazena o valor inicial da ocupação que é 0.
    ocupacao_inicial = 0
    
    # A variável ocupacao_final armazena o valor final da ocupação que é 100.
    ocupacao_final = 100
    
    # A variável incremento_ocupacao armazena o valor de incremento entre as ocupações.
    incremento_ocupacao = 10
    
    # A variável n_janelamento_inicial armazena o valor inicial do janelamento que é 7.
    n_janelamento_inicial = 7
    
    # A variável n_janelamento_final armazena o valor final do janelamento que é 19.
    n_janelamento_final = 19
    
    # A variável incremento_janelamento armazena o valor do incremento entre os janelamentos.
    incremento_janelamento = 2
    
    # Para o número de janelamento inicial de 7 até 19 com incremento de 2.
    for n_janelamento in tqdm(range(n_janelamento_inicial, n_janelamento_final+1, incremento_janelamento)):
    
        # Para o número de ocupação de 0 até 100 com incremento de 10.
        for numero_ocupacao in tqdm(range(ocupacao_inicial, ocupacao_final+1, incremento_ocupacao)):
    
            # Chamada ordenada das funções.
    
            Matriz_Dados_OC = leitura_dados_ocupacao(numero_ocupacao)
    
            Matriz_Dados_OC_Sem_Pedestal = retirada_pedestal(Matriz_Dados_OC)
    
            vetor_amostras_pulsos, vetor_amplitude_referencia, _ = amostras_pulsos_e_referencia(Matriz_Dados_OC_Sem_Pedestal)
    
            Matriz_Dados_Pulsos, vetor_parametro_referencia = amostras_janelamento(vetor_amostras_pulsos, vetor_amplitude_referencia, n_janelamento)
    
            lista_erro_amplitude = metodo_desconvolucao_P_igual_N(Matriz_Dados_Pulsos, vetor_parametro_referencia, n_janelamento)
    
            media_erro_amplitude, var_erro_amplitude, desvio_padrao_erro_amplitude = dados_estatisticos_erro_amplitude(lista_erro_amplitude)
    
            arquivo_saida_dados_estatisticos_erro_amplitude(numero_ocupacao, n_janelamento, media_erro_amplitude, var_erro_amplitude, desvio_padrao_erro_amplitude)
            
### -------------------------------------------------------------------------------------------------------------------------------------------- ###

# Chamada da função principal do código.
principal_arquivo_saida_dados_estatisticos_desconvolucao()

# Impressão de uma linha que representa o fim do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")