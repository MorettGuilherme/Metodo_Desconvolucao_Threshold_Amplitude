O método da desconvolução de sinais para o sistema linear invariante no tempo na estimação da amplitude independe do efeito de empilhamento. Matematicamente, isso quer dizer que durante a etapa de estimação, não há a utilização dos dados de ruídos. De fato, o processo é bem simples, pois para obter o vetor de amplitude estimadas (a amplitude estimada é a central), basta calcular a inversa da matriz que contém os pulsos de referência deslocados (matriz de desconvolução) e multiplicar pelo vetor de pulsos de sinais janelados.
Nesse trabalho, o objetivo é determinar o janelamento mais adquado  apartir da análise média do erro de estimação da amplitude e o desvio padrão (noção da dispersão dos dados em realçaõ a média).
O resultados foi que o janelamento 15 pode ser considerado como ideal.

A seguir são listadas as pastas e também os arquivos contidos nesse repositório, assim como suas respectivas funções:

1) Dados_Estatisticos_Desconvolucao_OC
- Essa pasta contém os dados estatísticos (média, variância e desvio padrão) do erro de estimação ao decorrer das ocupações para cada um dos janelamentos. O formato dos arquivos é txt.

2) Dados_Ocupacoes_Free_Running
- Essa pasta contém os dados organizados em colunas; respectivamente tempo (ns), pulsos de sinais (ADC Count), amplitude de referência (ADC Count) e fase de referência (ns) para cada uma das ocupações. O formato dos arquivos é txt.

3) K_Fold_DP_Dados_Estatisticos_Desconvolucao_OC
- Essa pasta contém os dados estatísticos (média, variância e desvio padrão) para o desvio padrão pela aplicação da técnica de validação cruzada K-Fold.

4) K_Fold_Media_Dados_Estatisticos_Desconvolucao_OC
- Essa pasta contém os dados estatísticos (média, variância e desvio padrão) para a média pela aplicação da técnica de validação cruzada K-Fold.

5) K_Fold_Var_Dados_Estatisticos_Desconvolucao_OC
- Essa pasta contém os dados estatísticos (média, variância e desvio padrão) para a variância pela aplicação da técnica de validação cruzada K-Fold.

6) Resultados_Desconvolucao_Amplitude
- Essa pasta contém as pastas que apresentam os gráficos do tipo A (Grafico_A_K_Fold) e B (Grafico_B_K_Fold) para a validação cruzada K-Fold, tambpém há os histogramas para cada um dos janelamentos e ocupações (Histogramas).

7) arquivo_saida_dados_estatisticos_desconvolucao.py
- Cálculo dos dados estatístico do erro de estimação;
- Salvar os dados estatísticos do erro de estimação para determinada ocupação em uma arquivo de saída.

8) grafico_dado_estatistico_janelamento_desconvolucao.py
- Leitura dos dados estatísticos de todas as ocupações para um determinado janelamento;
- Plote do gráfico do dado estatístico ao longo das ocupações para um determinado janelamento.

9) grafico_k_fold_desconvolucao.py
- Leitura dos dados estatísticos da validação cruzada K-Fold;
- Construção do gráfico tipo A da validação cruzada K-Fold (esse gráfico mostra a média do dado estatatístico com as barras de erro para cada um dos janelamentos ao decorrer das ocupações);
- Construção do gráfico tipo B da validação cruzada K-Fold (esse gráfico mostra a média do dado estatatístico com as barras de erro para cada uma das ocupações ao decorrer do janelamento).

10) histograma_erro_amplitude_desconvolucao.py
- Cálculo da estatística do erro de estimação;
- Salvar os dados estatísticos do erro de estimação para determinada ocupação em uma arquivo de saída;
- Plote do histograma do erro de estimação.

11) k_fold_desconvolucao.py
- Salvar em arquivos os dados estatísticos pela validação cruzada k-Fold;
- Validação cruzada K-Fold (cem blocos).

12) leitura_dados_ocupacao_desconvolucao.py
- Leitura dos dados de ocupação;
- Retirada do pedestal dos pulsos de sinais;
- Construção da matriz dos pulsos de sinais e o vetor do parâmetro de referência.

13) metodo_desconvolucao_P_igual_N.py
- Construção da matriz H a partir dos dados dos pulsos de referência;
- Método da desconvolução para o caso N = P.

IMPORTANTE: os dados das ocupações foram simulados computacionalmente.
As características das distribuições são:
- Distribuição amplitude: exponencial com média 100 ADC Count.
- Distribuição Fase: uniforme com números inteiros no intervalo de -5 a 5 ADC Count.
- Pedestal: 30 ADC Counts.
- Nível de deformação: 0,01 ADC Count.
- Número de eventos: 2000000.
  


    

  
