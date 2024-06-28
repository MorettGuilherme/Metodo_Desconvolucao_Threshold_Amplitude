# EXPERIMENTO ATLAS - Reconstrução de sinal - Método de Desconvolução de Sinal - Estimação da amplitude.
# Autor: Guilherme Barroso Morett.
# Data: 28 de junho de 2024.

# Objetivo do código: implementação da validação cruzada para o método de Desconvolução de Sinal.

""" 
Organização do código:

Importação de arquivos.
Leitura dos dados de ocupação: leitura_dados_ocupacao_desconvolucao.py
Método da Desconvolução: metodo_desconvolucao_P_igual_N.py

Funções presentes:

1) Instrução para salvar em arquivos os dados estatísticos pela validação cruzada k-Fold.
Entrada: número de ocupação, número do janelamento, média do dado estatístico, variância do dado estatístico, desvio padrão do dado estatístico de interesse.
Saída: nada.

2) Instrução da validação cruzada K-Fold.
Entrada: matriz com os pulsos de sinais e o vetor das amplitudes de referência.
Saída: nada.

3) Instrução principal do código.
Entrada: nada.
Saída: nada.
"""

# Importação de bibliotecas.
import numpy as np
import os
from tqdm import tqdm
import time
from termcolor import colored

# Importação dos arquivos.
from leitura_dados_ocupacao_desconvolucao import leitura_dados_ocupacao, retirada_pedestal, amostras_pulsos_e_referencia, amostras_janelamento 
from metodo_desconvolucao_P_igual_N import *

# Impressão de uma linha que representa o início do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")

# Título do programa.

# A variável titulo_programa armazena o título em negrito.
titulo_programa = colored("Geração de arquivos de saída pela técnica de validação cruzada K-Fold para o método de Desconvolução de Sinal - P = N:\n", attrs=["bold"])

# Impressão do título do programa.
print(titulo_programa)


### ----------------------------------------- 1) INSTRUÇÃO PARA SALVAR OS DADOS ESTATÍSTICOS DO K-FOLD ----------------------------------------- ###

# Definição da função para salvar as médias dos dados estatísticos dos blocos em um arquivo de saída.
def arquivo_saida_dados_estatisticos_k_fold_erro(n_ocupacao, n_janelamento, media_dado_erro, var_dado_erro, DP_dado_erro, dado):

    # Definição do título presente no arquivo de saída.
    titulo_arquivo_saida = f"janelamento,media_{dado}_erro,var_{dado}_erro,DP_{dado}_erro\n"

    # Definição da pasta que contém o arquivo de saída.
    pasta_saida = f"K_Fold_{dado}_Dados_Estatisticos_Desconvolucao_OC"

    # Caso a pasta não exista.
    if not os.path.exists(pasta_saida):
        
        # Criação da pasta de saída.
        os.makedirs(pasta_saida)

    # Nome do arquivo de saida.
    arquivo_saida = f"k_fold_{dado}_dados_estatisticos_desconvolucao_OC_{n_ocupacao}.txt"

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
            arquivo_saida_dados_estatisticos.write(f"{n_janelamento},{media_dado_erro},{var_dado_erro},{DP_dado_erro}\n")
    # Excessão.
    except Exception as e:
        # Impressão de mensagem de alerta.
        print("Ocorreu um erro ao atualizar o arquivo de saída dos dados estatísticos:", str(e))

### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### ----------------------------------------------- 2) INSTRUÇÃO PARA A VALIDAÇÃO CRUZADA K-FOLD ----------------------------------------------- ###

# Definição da instrução da técnica de validação cruzada K-Fold.
def K_fold(Matriz_Pulsos_Sinais, vetor_parametro_referencia, n_ocupacao, n_janelamento):
    
    # A variável quantidade_blocos armazena o número de blocos desejado.
    quantidade_blocos = 100
    
    # A variável elementos_bloco armazena o número de elementos presente em cada bloco.
    elementos_bloco = len(Matriz_Pulsos_Sinais) // quantidade_blocos
    
    # Definição da lista vazia lista_bloco_media_erro.
    lista_blocos_media_erro = []
    
    # Definição da lista vazia lista_bloco_var_erro.
    lista_blocos_var_erro = []
    
    # Definição da lista vazia lista_bloco_DP_erro.
    lista_blocos_DP_erro = []
     
    # Para indice_bloco zero até o tamanho da matriz de dados de entrada com incremento igual a quantidade de elementos no bloco.
    for indice_bloco in range(0, len(Matriz_Pulsos_Sinais), elementos_bloco):
        
        # Definição do bloco que contém a matriz dos pulsos de sinais.
        Bloco_pulsos_sinais = Matriz_Pulsos_Sinais[indice_bloco : indice_bloco+elementos_bloco]
            
        # Definição do bloco que contém o vetor da amplitude de referência.
        Bloco_vetor_amplitude_referencia = vetor_parametro_referencia[indice_bloco : indice_bloco+elementos_bloco]
        
        # A variável bloco_lista_erro_amplitude recebe o valor de retorno da função desconvolucao_P_igual_N.
        Bloco_lista_erro_amplitude = metodo_desconvolucao_P_igual_N(Bloco_pulsos_sinais, Bloco_vetor_amplitude_referencia, n_janelamento)
        
        # Cálculo dos dados estatísticos de cada bloco.
        bloco_media_erro = np.mean(Bloco_lista_erro_amplitude)
        bloco_var_erro = np.var(Bloco_lista_erro_amplitude)
        bloco_DP_erro = np.std(Bloco_lista_erro_amplitude)
        
        # Adiciona essas informações em suas respectivas listas.    
        lista_blocos_media_erro.append(bloco_media_erro)
        lista_blocos_var_erro.append(bloco_var_erro)
        lista_blocos_DP_erro.append(bloco_DP_erro)
        
    # Cálculo dos dados estatísticos da média.
    media_media_blocos_erro = np.mean(lista_blocos_media_erro)
    var_media_blocos_erro_amplitude = np.var(lista_blocos_media_erro)
    DP_media_blocos_erro_amplitude = np.std(lista_blocos_media_erro)
     
    # Salva a informação dos dados estatísticos da média do erro de estimação da amplitude em seus respectivos arquivos de saída.   
    arquivo_saida_dados_estatisticos_k_fold_erro(n_ocupacao, n_janelamento, media_media_blocos_erro, var_media_blocos_erro_amplitude, DP_media_blocos_erro_amplitude, dado = "media")
        
    # Cálculo dos dados estatísticos da variância.
    media_var_blocos_erro_amplitude = np.mean(lista_blocos_var_erro)
    var_var_blocos_erro_amplitude = np.var(lista_blocos_var_erro)
    DP_var_blocos_erro_amplitude = np.std(lista_blocos_var_erro)
      
    # Salva a informação dos dados estatísticos da variância do erro de estimação da amplitude em seus respectivos arquivos de saída.  
    arquivo_saida_dados_estatisticos_k_fold_erro(n_ocupacao, n_janelamento, media_var_blocos_erro_amplitude, var_var_blocos_erro_amplitude , DP_var_blocos_erro_amplitude, dado = "var")
        
    # Cálculo dos dados estatísticos do desvio padrão.
    media_DP_blocos_erro_amplitude = np.mean(lista_blocos_DP_erro)
    var_DP_blocos_erro_amplitude = np.var(lista_blocos_DP_erro)
    DP_DP_blocos_erro_amplitude = np.std(lista_blocos_DP_erro)
    
    # Salva a informação dos dados estatísticos do desvio padrão do erro de estimação da amplitude em seus respectivos arquivos de saída.
    arquivo_saida_dados_estatisticos_k_fold_erro(n_ocupacao, n_janelamento, media_DP_blocos_erro_amplitude, var_DP_blocos_erro_amplitude , DP_DP_blocos_erro_amplitude, dado = "DP")
    
### -------------------------------------------------------------------------------------------------------------------------------------------- ### 

### ----------------------------------------- 3) INSTRUÇÃO PARA APLICAR O K-FOLD EM TODAS AS OCUPAÇÕES ----------------------------------------- ###
  
# Definição da função principal (main) do código.
def principal_K_fold():
    
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
    
    # Para o número de ocupações de 0 até 100 com incremento de 10. 
    for numero_ocupacao in tqdm(range(ocupacao_inicial, ocupacao_final+1, incremento_ocupacao)):
    
        # Para o número de janelamento de 7 até 19 com incremento de 2.
        for n_janelamento in tqdm(range(n_janelamento_inicial, n_janelamento_final+1, incremento_janelamento)):
    
            # Chamada ordenada das funções.
    
            Matriz_Dados_OC = leitura_dados_ocupacao(numero_ocupacao)
        
            Matriz_Dados_OC_Sem_Pedestal = retirada_pedestal(Matriz_Dados_OC)
    
            vetor_amostras_pulsos, vetor_amplitude_referencia, _ = amostras_pulsos_e_referencia(Matriz_Dados_OC_Sem_Pedestal)
        
            Matriz_Dados_Pulsos, vetor_parametro_referencia = amostras_janelamento(vetor_amostras_pulsos, vetor_amplitude_referencia, n_janelamento)
    
            K_fold(Matriz_Dados_Pulsos, vetor_parametro_referencia, numero_ocupacao, n_janelamento)
     
# Chamada da função principal do código.
principal_K_fold()
       
### -------------------------------------------------------------------------------------------------------------------------------------------- ###

# Impressão de uma linha que representa o fim do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")