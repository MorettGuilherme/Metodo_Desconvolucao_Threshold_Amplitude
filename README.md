O método de Desconvolução de Sinal para o sistema linear invariante no tempo na estimação da amplitude independe do efeito de empilhamento. Matematicamente, isso quer dizer que durante a etapa de estimação, não há a utilização dos dados de ruídos. De fato, o processo é bem simples, pois para obter o vetor de amplitude estimadas (a amplitude estimada é a central), basta calcular a inversa da matriz que contém os pulsos de referência deslocados (matriz de desconvolução) e multiplicar pelo vetor de pulsos de sinais janelados.
Nesse trabalho, o objetivo é determinar o janelamento mais adequado a partir da análise média do erro de estimação da amplitude e o desvio padrão.
O resultado foi que o janelamento 15 pode ser considerado como ideal.

A seguir estão listadas as pastas e também os arquivos contidos nesse repositório, assim como suas respectivas funções:

1) Dados_Estatisticos_Desconvolucao_OC
- Essa pasta contém os dados estatísticos (média, variância e desvio padrão) do erro de estimação ao decorrer das ocupações para cada um dos janelamentos. O formato dos arquivos é txt.

2) Dados_Ocupacoes_Free_Running
- Essa pasta contém os dados organizados em colunas; respectivamente tempo (ns), pulsos de sinais (ADC Count), amplitude de referência (ADC Count) e fase de referência (ns) para cada uma das ocupações. O formato dos arquivo é txt.

3) K_Fold_amplitude_DP_Desempenho_Desconvolucao_OC
- Essa pasta contém os dados organizados em colunas; respectivamente tempo (ns), pulsos de sinais (ADC Count), amplitude de referência (ADC Count) e fase de referência (ns) para cada uma das ocupações. O formato dos arquivo é txt.

4) K_Fold_amplitude_EME_Desempenho_Desconvolucao_OC
- Essa pasta contém os dados organizado em colunas; respectivamente número de ocupação, média do EME, variância do EME, desvio padrão do EME. O formato do arquivo é txt.

5) K_Fold_amplitude_MAE_Desempenho_Desconvolucao_OC
- Essa pasta contém os dados organizado em colunas; respectivamente número de ocupação, média do MAE, variância do MAE, desvio padrão do MAE. O formato do arquivo é txt.

6) K_Fold_amplitude_MSE_Desempenho_Desconvolucao_OC
- Essa pasta contém os dados organizado em colunas; respectivamente número de ocupação, média do MSE, variância do MSE, desvio padrão do MSE. O formato do arquivo é txt.

7) K_Fold_amplitude_SNR_Desempenho_Desconvolucao_OC
- Essa pasta contém os dados organizado em colunas; respectivamente número de ocupação, média do SNR, variância do SNR, desvio padrão do SNR. O formato do arquivo é txt.

8) K_Fold_DP_Dados_Estatisticos_Desconvolucao_OC
- Essa pasta contém os dados estatísticos (média, variância e desvio padrão) para o desvio padrão pela aplicação da técnica de validação cruzada K-Fold.

9) K_Fold_Media_Dados_Estatisticos_Desconvolucao_OC
- Essa pasta contém os dados estatísticos (média, variância e desvio padrão) para a média pela aplicação da técnica de validação cruzada K-Fold.

10) K_Fold_Var_Dados_Estatisticos_Desconvolucao_OC
- Essa pasta contém os dados estatísticos (média, variância e desvio padrão) para a variância pela aplicação da técnica de validação cruzada K-Fold.

11) Resultados_Desconvolucao_Amplitude
- Essa pasta contém as pastas que apresentam os gráficos do tipo A (Grafico_A_K_Fold) e B (Grafico_B_K_Fold) para a validação cruzada K-Fold, tambpém há os histogramas para cada um dos janelamentos e ocupações (Histogramas).

12) Workshop_Slides
- Essa pasta contém os slides da apresentação realizada no grupo ATLAS/Brasil.

13) analise_desempenho_desconvolucao.py
- Instrução para salvar em arquivos os dados estatísticos do desempenho do método de Desconvolução de Sinal;
- Função para o cálculo do desempenho do Desconvolução de Sinal pelo Erro Médio de Estimação (EME);
- Função para o cálculo do desempenho do método de Desconvolução de Sinal pelo Erro Médio Quadrático (Mean Squared Error - MSE);
- Função para o cálculo do desempenho do método de Desconvolução de Sinal pelo Erro Médio Absoluto (Mean Absolute Error - MAE);
- Função para o cálculo do desempenho do método de Desconvolução de Sinal pela Relação Sinal-Ruído (Signal-to-Noise-Ratio - SNR);
- Função para o cálculo do desempenho do método de Desconvolução de Sinal pelo desvio padrão (DP);
- Instrução da validação cruzada K-Fold adaptada para o cálculo do desempenho do método de desconvolução de sinal;
- Instrução principal do código.

14) arquivo_saida_dados_estatisticos_desconvolucao.py
- Cálculo dos dados estatístico do erro de estimação;
- Salvar os dados estatísticos do erro de estimação para determinada ocupação em uma arquivo de saída;
- Instrução principal do código.

15) grafico_dado_estatistico_janelamento_desconvolucao.py
- Leitura dos dados estatísticos de todas as ocupações para um determinado janelamento;
- Plote do gráfico do dado estatístico ao longo das ocupações para um determinado janelamento;
- Instrução principal do código.

16) grafico_desempenho_desconvolucao.py
- Função para a leitura dos dados do desempenho do método de Desconvolução de Sinal de todas as ocupações para o janelamento ideal;
- Instrução para o plote do gráfico do desempenho do método de Desconvolução de Sinal ao longo das ocupações para o janelamento ideal;
- Instrução principal do código.

17) grafico_k_fold_desconvolucao.py
- Leitura dos dados estatísticos da validação cruzada K-Fold;
- Construção do gráfico tipo A da validação cruzada K-Fold (esse gráfico mostra a média do dado estatatístico com as barras de erro para cada um dos janelamentos ao decorrer das ocupações);
- Construção do gráfico tipo B da validação cruzada K-Fold (esse gráfico mostra a média do dado estatatístico com as barras de erro para cada uma das ocupações ao decorrer do janelamento);
- Instrução principal do código.

18) histograma_erro_amplitude_desconvolucao.py
- Cálculo da estatística do erro de estimação;
- Salvar os dados estatísticos do erro de estimação para determinada ocupação em uma arquivo de saída;
- Plote do histograma do erro de estimação;
- Instrução principal do código.

19) k_fold_desconvolucao.py
- Salvar em arquivos os dados estatísticos pela validação cruzada k-Fold;
- Validação cruzada K-Fold (cem blocos);
- Instrução principal do código.

20) leitura_dados_ocupacao_desconvolucao.py
- Leitura dos dados de ocupação;
- Retirada do pedestal dos pulsos de sinais;
- Construção da matriz dos pulsos de sinais e o vetor do parâmetro de referência.

21) metodo_desconvolucao_P_igual_N.py
- Construção da matriz H a partir dos dados dos pulsos de referência;
- Método da desconvolução para o caso N = P.

IMPORTANTE: os dados das ocupações foram simulados computacionalmente.
As características das distribuições são:
- Distribuição amplitude: exponencial com média 100 ADC Count.
- Distribuição Fase: uniforme com números inteiros no intervalo de -5 a 5 ns.
- Pedestal: 30 ADC Count.
- Nível de deformação: 0,01 ADC Count.
- Número de eventos: 2000000.
  


    

  
