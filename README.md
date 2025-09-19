# ProjetoFinalTCC
\documentclass{article}
\DeclareUnicodeCharacter{03F5}{\ensuremath{\varepsilon}}
\usepackage[utf8]{inputenc}

% Language setting
% Replace `english' with e.g. `spanish' to change the document language

\usepackage[utf8]{inputenc} % Define a codificação de caracteres como UTF-8, necessária para o português
\usepackage[T1]{fontenc} % Define a codificação de fontes como T1, necessária para caracteres acentuados
\usepackage[portuguese]{babel} % Configura o idioma para português
\usepackage{float}
\usepackage{graphicx}

% Set page size and margins
% Replace `letterpaper' with `a4paper' for UK/EU standard size
\usepackage[letterpaper,top=2cm,bottom=2cm,left=3cm,right=3cm,marginparwidth=1.75cm]{geometry}

% Useful packages
\usepackage{amsmath}
\usepackage{graphicx}
\usepackage[colorlinks=true, allcolors=blue]{hyperref}

% Biblioteca para criação de referências

\usepackage{biblatex}
%\addbibresource{p-value.bib}
%\addbibresource{stepwise.bib}
%\addbibresource{kmeans.bib}
%\addbibresource{elbow.bib}
%\addbibresource{DBscan.bib}
%%\addbibresource{DBscan Analise.bib}
%\addbibresource{haversine.bib}
%\addbibresource{redes.bib}
%\addbibresource{redesferroviarias.bib}
%\addbibresource{redesformula.bib}
%\addbibresource{modelologistico.bib}
%\addbibresource{distribuicaoz.bib}

\addbibresource{allreferences.bib}








\title{Modelo Logístico preditivo para apoiar a tomada de decisões estratégicas em um sistema metroviário. }
\author{José Henrique Alves de Oliveira}

\begin{document}
\maketitle


\begin{abstract}
Este trabalho realiza uma análise dos fatores que podem influenciar o tempo de atraso em uma malha ferroviária, utilizando dados da "NJ Transit", localizada nos Estados Unidos. A base de dados utilizada está disponível publicamente na plataforma "Kaggle". Foram identificadas e separadas variáveis qualitativas e quantitativas, e realizados testes para análise de significância estatística dessas variáveis, como o teste do p-value. Ao final, foi desenvolvido um modelo binomial para estimar e classificar se uma viagem até uma estação irá ou não sofrer atraso. Os resultados indicaram que o principal fator contribuinte para os atrasos, nessa base de dados específica, é a categoria "Estação de destino", sugerindo que medidas devem ser tomadas em certas estações para melhorar a operação e reduzir os tempos de atraso em relação aos tempos de viagem planejados.
\end{abstract}

\section{Introdução}

O sistema ferroviário do NJ Transit é uma das maiores redes de transporte público dos Estados Unidos, composto por 11 linhas principais que conectam diversas regiões de Nova Jersey às grandes cidades de Nova York e Filadélfia. Com mais de 160 estações ao longo dessas linhas, o NJ Transit desempenha um papel fundamental na mobilidade de centenas de milhares de passageiros diariamente, oferecendo uma alternativa eficiente ao trânsito rodoviário. Entre suas linhas mais relevantes estão a Northeast Corridor, que liga Trenton a Nova York, e a North Jersey Coast Line, que percorre a costa do estado, além de outras que servem áreas suburbanas e industriais. A importância do NJ Transit vai além do transporte de passageiros, pois ele facilita a conexão entre comunidades, impulsiona a economia regional e contribui significativamente para a redução do congestionamento nas estradas, promovendo uma mobilidade mais sustentável e acessível para a população de Nova Jersey e de cidades vizinhas.
Dada essa importância, estudar o desempenho da linha através da análise de tempos de atrasos em viagens é de extrema importância, pois eles têm um impacto significativo na eficiência do sistema e na experiência dos passageiros.
Podemos ver na Figura \ref{fig:Mapa}  abaixo um esquemático que mostra a complexidade da malha em questão.

\begin{figure}[H]
\centering
\includegraphics[width=1\linewidth]{Mapa Metro.png}
\caption{\label{fig:Mapa} Malha Ferroviária NJ Transit.}
\end{figure}

O gerenciamento de uma malha complexa e de alto fluxo de passageiros exige um planejamento robusto. Analisar as causas e prever atrasos com base nas características dos itinerários, linhas e estações permite aos administradores do sistema identificar os principais fatores que impactam a operação. Com isso, é possível adotar medidas para reduzir atrasos e melhorar a qualidade do serviço para os passageiros. 
	
A pesquisa em questão foi escolhida pois a base de dados apresentada é robusta, apresenta uma topologia de rede complexa para uma malha ferroviária, e dessa maneira seus aprendizados podem ser usados como referência para análises de linhas mais, ou menos complexas ao redor de todo o mundo.


\section{Objetivo}

O objetivo do estudo em questão é analisar a relevância de variáveis explicativas relacionadas a fatores temporais, sazonais, geográficos e de características de rede no estudo de tempos de atraso em uma malha ferroviária complexa e desenvolver um modelo  preditivo para apoiar a tomada de decisões estratégicas em um sistema metroviário. 
Para tal será usada uma malha ferroviária complexa contendo 11 linhas e 165 estações, situada nos estados de Nova York, Nova Jersey e Filadélfia nos Estados unidos.


\section{Metódos}

A seguinte seção tem como objetivo detalhar os métodos estátisticos e matemáticos, além de alguns conceitos de fundamental importância para desenvolvimento do estudo.


\subsection{Análise de significância : p-value: Distribuição Z}


A distribuição Z é utilizada em testes que envolvem a distribuição normal padrão.
Comumente aplicada na regressão logística, onde os erros são presumidos ao seguir uma distribuição normal.

O \textit{Z}-score é calculado como:
\[
z = \frac{X - \mu}{\sigma}
\]

Onde:

\begin{itemize}
    \item \( z \) = Z-Score
    \item \( X \) = Valor da observação.
    \item \( \mu \) = Média das observações.
    \item \( \sigma \) = Desvio padrão.
\end{itemize}

Um Z-score representa quantos desvios padrão um valor está acima ou abaixo da média da distribuição. Um "Z-score" positivo indica que o valor está acima da média, enquanto um "Z-score negativo indica que está abaixo da média\\


O "P-value" (\(p>\mid Z \mid\)) é a probabilidade de obter um valor absoluto de \(Z\) tão extremo ou mais extremo, assumindo que a hipótese nula (\(H_0\) = 0) é verdadeira (Definida em \ref{sec: Análise de significância : p-value :} ). Em general queremos que esse valor de probabilidade seja baixo, para recusar a hipótese nula e afirmar que a variável possue significancia estatística no contexto do modelo.


\subsubsection{Análise de significância : p-value : \(p>\mid Z \mid\)}
\label{sec: Análise de significância : p-value :}

Informalmente, o p-value é a probabilidade, sob um modelo estatístico especificado, de que um resumo estatístico dos dados (por exemplo, a diferença média da amostra entre dois grupos comparados) seja igual ou mais extremo do que o valor observado.\cite{wasserstein2016asa} \\

O p-value, é um conceito fundamental em estatística utilizado para testar hipóteses e determinar a significância dos resultados. \\

Para analisar a influência de variáveis preditoras na variável alvo, usaremos as seguinte hipóteses: 

\subsection*{Hipótese Nula (\(H_0\))}

\(H_0\): O coeficiente da variável independente é igual a zero.

\subsection*{Hipótese Alternativa (\(H_1\))}

\(H_1\): O coeficiente da variável independente é diferente de zero.\\




Para um intervalo de confiança de 0.95 (Usualmente adotado):

\begin{itemize}
    \item P-value < 0.05: Rejeitamos a hipótese nula, indicando que a variável preditora tem um efeito significativo na variável dependente e, portanto, é relevante para a análise.\\
    \item P-value > 0.05: Não rejeitamos a hipótese nula, indicando que não há evidências suficientes para afirmar que a variável preditora tem um efeito significativo na variável dependente, sugerindo que a variável pode não ser relevante para a análise.

\end{itemize}








Para todas as variáveis preditoras analisadas posteriormente será realizado o teste do "p-value" para identificar se a variável preditora tem um efeito significativo na análise da variável dependente, no contexto do modelo de regressão logística representado pela distribuição binomial.





\subsection{Análise de significância : Seleção Stepwise}
\label{sec: Análise de significância : Seleção Stepwise}

O procedimento "stepwise" é uma abordagem iterativa utilizada para selecionar variáveis explicativas em modelos estatísticos, visando otimizar o ajuste do modelo e reduzir sua complexidade. Este método pode incluir mecanismos de adição ou remoção de variáveis, com base em critérios como AIC, BIC ou "p-values" \cite{akaike1974}. Em cada etapa, uma variável é adicionada ou removida com base em critérios estatísticos definidos (No trabalho, usaremos a métrica de "p-value" das variáveis como critério de seleção). O modelo é continuamente testado para assegurar que as variáveis incluídas são as mais significativas.\\



Ao final do trabalho, será aplicado o procedimento stepwise para remoção de variáveis pouco significantes, no contexto do modelo desenvolvido.


\subsection{Clusterização : K-means}

O K-means é um dos algoritmos mais utilizados para a clusterização de dados. A clusterização é uma técnica de aprendizado de máquina não supervisionado que agrupa dados em clusters, onde cada cluster contém objetos que são mais similares entre si do que aos objetos de outros clusters. O K-means especificamente visa partitionar n observações em k clusters, com cada observação pertencendo ao cluster com o centroide mais próximo.\cite{bishop2006pattern}.

\subsubsection{Clusterização : K-means: Método de parada}
\label{sec:Clusterização : K-means: Método de parada}

O método do 'Elbow' é uma técnica utilizada para determinar o número ótimo de clusters ao executar o K-means, traçando a soma das quadráticas dentro do cluster (WCSS) para diferentes valores de 
k e identificando o ponto onde a redução da WCSS diminui drasticamente. \cite{james2013introduction}

Esse método será usado no próximo capitulo \ref{sec:Variável explicativa : Clusterização espacial : Kmeans} para a clusterização geográfica de estações da malha ferroviária.

\subsection{Clusterização : DBSCAN}

O DBSCAN (Density-Based Spatial Clustering of Applications with Noise) é um método de clusterização usado para agrupar pontos de dados com base em densidades de vizinhança e identificar pontos de dados como ruídos se eles não pertencem a qualquer cluster.

A clusterização DBSCAN começa selecionando um ponto aleatório e verificando se ele contém o mínimo de pontos vizinhos dentro do raio Epsilon. Se sim, o ponto é considerado um ponto núcleo e um novo cluster é iniciado. O algoritmo continua expandindo o cluster, adicionando todos os vizinhos na vizinhança de EPS. Pontos ruídos são simplesmente ignorados.\cite{DBSCAN1996}

Esse método será utilizado para clusterização geográfica, pois em geral o seu uso é recomendado para aplicações geográficas e espaciais. Na seção \ref{sec:Variável explicativa : Clusterização espacial : DBscan} utilizamos esse método para classificar geograficamente os dados de longitude e latitude das estações da linha.

\subsubsection{Clusterização : K-means: Escolha de parâmetros }

O método de parada utilizando a "Distância do Vizinho Mais Próximo" no contexto do DBSCAN pode ser integrado para determinar valores apropriados de parâmetros como ϵ (Epsilon). A quantidade mínima de pontos vizinhos para a formação de um cluster será determinada baseada na quantidade de variáveis usadas na formação do cluster. Embora o DBSCAN tradicionalmente utilize critérios de densidade para formar clusters, o conceito de distância do vizinho mais próximo pode ajudar a definir ϵ de maneira mais robusta. \Cite{ZakiMeira2014}


\subsection{Análise de redes}

Análise de redes é um campo de estudo interdisciplinar que examina a estrutura e os comportamentos de redes compostas por nós (ou vértices) e arestas (ou ligações). Essas redes podem representar diversas coisas, incluindo redes sociais, redes de comunicação, redes de transporte, redes biológicas, entre outros. O objetivo da modelagem utilizando redes é entender como os elementos da rede interagem, identificar padrões, detectar comunidades e analisar a influência dos nós. Nesse contexto uma malha ferroviária pode ser interpretada e analisada como uma rede.\cite{WattsStrogatz1998}\\

O Objetivo dessa seção é introduzir alguns conceitos relacionados a análise de redes, para posteriormente aplicar-los na análise dos tempos de atrasos da malha "NJ transit", assim como realizado em \cite{Lu2016}.

\subsubsection{Análise de redes : Betweenness Centrality  (C_B) }

Mede quantas vezes um nó atua como um ponte em caminhos mais curtos entre outros dois nós. Em resumo essa métrica nos diz quão central é um nó e nos ajuda a identificar os nós mais críticos da rede. Quanto maior o seu valor, mais caminhos curtos passam sobre esse nó, indicando maior importância do mesmo.
\\Essa é uma métrica que varia entre 0 e 1, e valores mais proximos de 1 indicam nós com maior importância no deslocamento pela rede. 

A Centralidade de Intermediação de um nó \( v \) é calculada como:

\[
C_B(v) = \sum_{s \neq v \neq t} \frac{\sigma_{st}(v)}{\sigma_{st}}
\]

Onde:

\(\sigma_{st}\) é o número de caminhos mais curtos entre os nós \( s \) e \( t \).

\(\sigma_{st}(v)\) é o número desses caminhos que passam pelo nó \( v \).




\subsubsection{Análise de redes : Closeness Centrality (C_C)}

A centralidade de proximidade (Closeness Centrality) mede o quão perto um nó está de todos os outros nós na rede, calculando a inversa da soma das distâncias mais curtas de um nó a todos os outros nós. Um nó com alta centralidade de proximidade pode alcançar outros nós mais rapidamente.

\textbf{Fórmula}

A centralidade de proximidade de um nó \( v \) é dada por:

\[
C_C(v) = \frac{1}{\sum_{u} d(u, v)}
\]

Onde:

\( d(u, v) \) é a distância mais curta entre os nós \( u \) e \( v \).

A soma é feita sobre todos os nós \( u \) na rede.

Um nó com alto valor de proximidade tem acesso rápido a todos os outros nós da rede. Isso significa que a posição desse nó é estratégica para a disseminação de informações ou influências.
Em redes de transporte, pode indicar que o nó representa um ponto central de tráfego fácil e rápido.


\subsubsection{Análise de redes : Clustering coeficient (C)}

O coeficiente de aglomeração (Clustering coeficient) mede a tendência dos nós em uma rede para formar clusters ou grupos densos. Ele indica a probabilidade de que dois vizinhos de um nó também sejam vizinhos entre si. Essa métrica nos ajuda a entender quais os nós que fazem a ligação entre subredes dentro da rede e quais são os pontos que ligam elas. 

Para um nó \( v \):

\[
C(v) = \frac{2T(v)}{k_v(k_v - 1)}
\]

Onde \( T(v) \) é o número de triângulos através do nó \( v \) e \( k_v \) é o grau do nó \( v \).


\subsubsection{Análise de redes : Degree ( D )}

O grau (Degree) de um nó é o número de arestas incidentes sobre o nó. Em uma rede não-direcionada, é simplesmente a contagem das conexões.

Para um nó \( v \):

\[
D_v = \sum_{u \in N(v)} 1
\]

Onde \( N(v) \) é o conjunto de vizinhos de \( v \).


\subsection{ Regressão logística }
\label{sec:Regressão logística}

O modelo logístico, também conhecido como regressão logística, é um tipo de modelo estatístico utilizado para prever a probabilidade de um evento ocorrer. É particularmente útil em situações onde a variável dependente é categórica, ou seja, representa classes ou categorias. A regressão logística é frequentemente usada para modelar binários (eventos) que têm dois possíveis resultados: sucesso/falha, sim/não, presença/ausência, etc.\\

Esse modelo Prevé a probabilidade de um determinado resultado, através da função logística. \cite{Hosmer2013}

 
\[ 
P(Y = 1 \mid X) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 X_1 + \beta_2 X_2 + \cdots + \beta_k X_k)}} 
\]

Onde:

\begin{itemize}
    \item \(P(Y = 1 \mid X)\) é a probabilidade de a variável dependente \(Y\) ser 1 dado os valores das variáveis independentes \(X_1, X_2, \ldots, X_k\).
    \item \(\beta_0\) é o intercepto do modelo.
    \item \(\beta_1, \beta_2, \ldots, \beta_k\) são os coeficientes das variáveis independentes \(X_1, X_2, \ldots, X_k\).
\end{itemize}

A função logit é a relação entre a função logística e a probabilidade:

\[
\text{logit}(P) = \ln\left(\frac{P}{1 - P}\right) = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \cdots + \beta_k X_k
\]


Esse modelo será utilizado no capitulo \ref{Sec:Modelagem} para estimar a probabilidade de atrasos e classificação de atrasos em eventos e não eventos.

\subsubsection{Regressão logística: Sensitividade, Especificidade e acurácia }

Essas medidas são utilizadas para mensurar a taxa de acerto do modelo de regressão logística, e são extremamente dependentes do corte escolhido para determinar se uma observação vai ser classificada como evento ou não, baseado na probabilidade de ocorrência. 

\subsubsection*{Sensibilidade}
 A sensibilidade mede a proporção de verdadeiros positivos que são corretamente identificados pelo modelo. Em outras palavras, é a capacidade do modelo de detectar corretamente os casos positivos.

\[
\text{Sensibilidade} = \frac{\text{Verdadeiros Positivos}}{\text{Verdadeiros Positivos} + \text{Falsos Negativos}}
\]

\subsubsection*{Especificidade}
Especificidade é a medida da proporção de verdadeiros negativos que são corretamente identificados pelo modelo. Ele avalia a capacidade do modelo de identificar corretamente os casos negativos.

\[
\text{Especificidade} = \frac{\text{Verdadeiros Negativos}}{\text{Verdadeiros Negativos} + \text{Falsos Positivos}}
\]

\subsubsection*{Acurácia}
Acurácia é uma medida global do desempenho do modelo, indicando a proporção de todas as previsões (positivas e negativas) que foram corretas. Em outras palavras, é a proporção de verdadeiros positivos e verdadeiros negativos do total de casos avaliados.

\[
\text{Acurácia} = \frac{\text{Verdadeiros Positivos} + \text{Verdadeiros Negativos}}{\text{Verdadeiros Positivos} + \text{Verdadeiros Negativos} + \text{Falsos Positivos} + \text{Falsos Negativos}}
\]


\subsubsection{Regressão logística: Curva ROC e coeficiente de Ginni }

\subsubsection*{Curva ROC (Receiver Operating Characteristic)}
A Curva ROC é uma ferramenta gráfica usada para avaliar o desempenho de um modelo de classificação binária, ilustrando a relação entre a taxa de verdadeiros positivos (sensibilidade) e a taxa de falsos positivos (1 - especificidade) para diferentes pontos de corte no limiar da previsão.

Interpretação:
\begin{itemize}
    \item Uma curva ROC que segue a diagonal (linha de 45 graus) representa um modelo sem poder discriminativo, ou seja, um modelo aleatório.
    \item Quanto mais a curva ROC se aproxima do canto superior esquerdo do gráfico, melhor o desempenho do modelo.
\end{itemize}

\subsubsection*{Área Sob a Curva ROC (AUC - Area Under the Curve)}
\label{sec:Área Sob a Curva ROC (AUC - Area Under the Curve)}
A AUC é uma medida quantitativa baseada na Curva ROC que sumariza o desempenho do modelo em um único valor:
\begin{itemize}
    \item \textbf{0.5}: Modelo aleatório.
    \item \textbf{0.5-0.7}: Desempenho ruim do modelo.
    \item \textbf{0.7-0.8}: Desempenho aceitável.
    \item \textbf{0.8-0.9}: Ótimo desempenho.
    \item \textbf{0.9-1}: Excelente desempenho.
\end{itemize}

\subsubsection*{Coeficiente de Gini}
O Coeficiente de Gini é uma medida derivada da AUC da Curva ROC. Ele é usado para quantificar a capacidade de discriminação de um modelo.

\subsection*{Cálculo:}
O Coeficiente de Gini é definido como:
\[
Gini = 2 \times \text{AUC} - 1
\]



\section{Variáveis alvo e explicativas}
\label{sec:Variáveis alvo e explicativas}

O objetivo desse capitulo é realizar a descrição da variável alvo de análise do estudo, e das variáveis explicativas que serão usadas na construção do modelo. Os dados adquiridos para a pesquisa são abertos e divulgados na plataforma “Keggle”, de autoria do usuário Pranav Badami e pode ser encontrada na seguinte referência: \cite{badami2023nj} \\

	
Outros dados relativos a topologia da malha, informações relativas a estações e linhas serão obtidas diretamente do site da administradora da NJ Transit, sendo essas informações públicas.


\subsection{Variável Alvo : Tempo de atraso ( Atr )}
\label{sec:Variável Alvo : Tempo de atraso ( Atr )}


\begin{figure}[H]
\centering
\includegraphics[width=1\linewidth]{Figura variável preditora.drawio.png}
\caption{\label{fig:variavel_y} Definição do tempo de atraso.}
\end{figure}



\begin{figure}[H]
\centering
\includegraphics[width=0.5\linewidth]{Contagem.png}
\caption{\label{fig:Atrasos} } Contagem dos tempos de atrasos arredondados.
\end{figure}





A variável alvo do estudo, será o tempo de atraso em uma viagem entre duas estações. Podemos ver na figura \ref{fig:variavel_y} que o tempo de atraso entre duas estações "A" e "B" em um segmento da viagem é dado pela diferença entre o tempo efetivo de chegada e o tempo previsto, que geralmente é definido pelo cronograma de operação da linha. \\
No Banco de dados em questão não foram computados atrasos negativos (Que representam adiantamento) e portanto quando o tempo é respeitado o valor 0 é utilizado.


\begin{align}
Atr &= Hefe - Hpre   & \text{(se Hefe > Hpre)} \\
Atr &= 0 & \text{(se Hefe < Hpre)}
\end{align}


A imagem da figura \ref{fig:variavel_y_exemplo} mostra na coluna denominada como "delay minutes" os tempos de atraso calculados de acordo com as equações (1) e (2). A coluna "To" representa a estação destino do segmento de viagem, denominado como "B" no mesmo diagrama. \\

A imagem da figura \ref{fig:Atrasos} mostra a distribuição dos atrasos de maneira arredondada. Atrasos maiores que 30 minutos foram representados no final da curva para facilitar a visualização.


\subsubsection{Variável Alvo : Uso no modelo Binomial (AtrEvent)}
\label{sec:Variável Alvo : Uso no modelo Binomial(AtrEvent)}
Para uso em um modelo de classificação Binária, que é realizado no capítulo \ref{Sec:Modelagem} foi decidido um corte, onde atrasos maiores que esse corte serão classificados como "evento", e atrasos menores que esse corte como "não eventos".

\begin{align}
Corte &=  1.0 m  & \text{(Corte para definição de evento de atraso em minutos)} \\
Evento &=  1   & \text{(se Atr > Corte)} \\
Evento &=  0 & \text{(se Atr < Corte)}
\end{align}



A princípio foi escolhido um corte de um minuto, pois entende-se que para uma linha como "NJ Trasit" esse tempo de espera impacta a experiência do usuário de maneira negativa. Porém esse corte é variável, e poderíam ser escolhidos outros valores para definição do corte de evento, como mostrado na seção \ref{sec:Influência da seleção de cuttof para definição de evento}.



\begin{figure}[H]
\centering
\includegraphics[width=1\linewidth]{Variável preditora Y.png}
\caption{\label{fig:variavel_y_exemplo} Exemplo da formatação dos dados na base.}
\end{figure}



\subsection{Variável explicativa : Linha( L ) }


A variável explicativa e qualitativa \textit{Linha} foi utilizada para analisar se itinerários pertencentes a diferentes linhas da malha ferroviária impactam diretamente o comportamento de atraso das viagens. A base de dados contém 11 linhas distintas, representadas na Figura~\ref{tab:njtransit}, juntamente com a quantidade de estações associadas a cada uma.\\

Para inclusão nos modelos a serem estimados a seguir, a variável foi dummificada. A categoria de referência adotada na dummificação corresponde à linha \textit{Atl City Line}.\\

A Tabela~\ref{table:line_usage} apresenta um resumo descritivo do tempo de atraso (em minutos) em função das linhas da malha ferroviária.






\begin{table}[h]
\centering
\begin{tabular}{|c|c|}
\hline
\textbf{Line Name} & \textbf{Number of Stations} \\ \hline
Atl. City Line & 9 \\ \hline
Bergen Co. Line & 25 \\ \hline
Gladstone Branch & 25 \\ \hline
Main Line & 26 \\ \hline
Montclair-Boonton & 28 \\ \hline
Morristown Line & 27 \\ \hline
No Jersey Coast & 28 \\ \hline
Northeast Corrdr & 16 \\ \hline
Pascack Valley & 18 \\ \hline
Princeton Shuttle & 2 \\ \hline
Raritan Valley & 21 \\ \hline
\end{tabular}
\caption{Linhas da malha "NJ transit" e número de estações}
\label{tab:njtransit}
\end{table}


\begin{table}[h]
\centering
\begin{tabular}{|c|c|c|c|c|c|c|c|c|c|}
\hline
\textbf{line} & \textbf{count} & \textbf{mean} & \textbf{std} & \textbf{min} & \textbf{25\%} & \textbf{50\%} & \textbf{75\%} & \textbf{max} \\ \hline
Atl\_City\_Line & 34236.0 & 4.665933 & 8.292705 & 0.0 & 0.216667 & 2.183333 & 5.166667 & 119.683333 \\ \hline
Bergen\_Co\_Line & 244363.0 & 3.688596 & 5.335199 & 0.0 & 1.100000 & 2.216667 & 4.233333 & 115.366667 \\ \hline
Gladstone\_Branch & 258981.0 & 3.738217 & 6.863046 & 0.0 & 0.400000 & 2.133333 & 4.166667 & 117.783333 \\ \hline
Main\_Line & 259034.0 & 4.026545 & 5.161872 & 0.0 & 1.266667 & 3.083333 & 5.083333 & 119.050000 \\ \hline
Montclair\_Boonton & 232553.0 & 4.265919 & 6.388445 & 0.0 & 1.133333 & 2.650000 & 5.183333 & 153.133333 \\ \hline
Morristown\_Line & 427822.0 & 4.154907 & 6.657040 & 0.0 & 1.100000 & 2.366667 & 5.050000 & 108.366667 \\ \hline
No\_Jersey\_Coast & 404085.0 & 4.782426 & 6.795765 & 0.0 & 1.116667 & 3.083333 & 6.066667 & 326.000000 \\ \hline
Northeast\_Corrdr & 448642.0 & 4.205772 & 6.383304 & 0.0 & 0.350000 & 2.233333 & 5.216667 & 114.550000 \\ \hline
Pascack\_Valley & 176234.0 & 3.324965 & 4.850361 & 0.0 & 1.050000 & 2.166667 & 4.150000 & 114.583333 \\ \hline
Princeton\_Shuttle & 32738.0 & 0.149508 & 1.904024 & 0.0 & 0.000000 & 0.000000 & 0.150000 & 118.466667 \\ \hline
Raritan\_Valley & 204921.0 & 4.644285 & 7.849721 & 0.0 & 1.083333 & 2.333333 & 5.100000 & 116.866667 \\ \hline
\end{tabular}
\caption{Descriptive Statistics of Line Usage}
\label{table:line_usage}
\end{table}










\subsubsection{Variável explicativa : Linha : Testes de análise de significancia estatística }


Para obtenção dos valores de p-values correspondentes a cada uma das categorias criadas na dummificação, foi ajustado um modelo de regressão logística conforme o código apresentado na Equação~\ref{eq:regressaol}. A mesma metodologia será aplicada na análise de todas as variáveis qualitativas que serão discutidas nas subseções seguintes. O resumo do modelo ajustado, bem como os respectivos valores de p-value, são apresentados na Figura \ref{fig:Line}.

Ao analisar os p-values obtidos, observa-se que o contexto da linha é significativo para a explicação dos atrasos, uma vez que todos os p-values são inferiores a 0.05, conforme o critério de significância definido na Seção \ref{sec: Análise de significância : p-value :}.





\begin{figure}[H]
\centering
\includegraphics[width=1\linewidth]{new_p-value_line.png}
\caption{\label{fig:Line} Resultado do teste estatístico p-value para o contexto linha usando intervalo de confiança de 0.95.}
\end{figure}


\subsection{Variável explicativa : Mês do ano ( M ) }






\begin{figure}[H]
\centering
\includegraphics[width=1\linewidth]{new-p-value-Month.png}
\caption{\label{fig:Month} Resultado do teste estatístico p-value para o contexto Mês usando intervalo de confiança de 0.95.}
\end{figure}


\begin{table}[h]
\centering
\begin{tabular}{|c|c|}
\hline
\textbf{Código} & \textbf{Mês} \\ 
\hline
1 & Janeiro \\ 
\hline
2 & Fevereiro \\ 
\hline
3 & Março \\ 
\hline
4 & Abril \\ 
\hline
5 & Maio \\ 
\hline
6 & Junho \\ 
\hline
7 & Julho \\ 
\hline
8 & Agosto \\ 
\hline
9 & Setembro \\ 
\hline
10 & Outubro \\ 
\hline
11 & Novembro \\ 
\hline
12 & Dezembro \\ 
\hline
\end{tabular}
\caption{Tabela de meses do ano codificados de 1 a 12}
\label{tab:meses}
\end{table}



\begin{table}[h]
\centering
\begin{tabular}{|c|c|c|c|c|c|c|c|c|}
\hline
\textbf{Month} & \textbf{count} & \textbf{mean} & \textbf{std} & \textbf{min} & \textbf{25\%} & \textbf{50\%} & \textbf{75\%} & \textbf{max} \\ \hline
1 & 202167.0 & 4.215319 & 5.793056 & 0.0 & 1.133333 & 2.566667 & 5.200000 & 153.133333 \\ \hline
2 & 186858.0 & 4.113015 & 6.115421 & 0.0 & 1.116667 & 2.416667 & 5.116667 & 326.000000 \\ \hline
3 & 234781.0 & 3.532170 & 6.685616 & 0.0 & 0.216667 & 2.100000 & 4.116667 & 111.183333 \\ \hline
4 & 234490.0 & 3.501576 & 6.115938 & 0.0 & 1.000000 & 2.133333 & 4.133333 & 108.116667 \\ \hline
5 & 245216.0 & 3.646849 & 5.654374 & 0.0 & 1.050000 & 2.200000 & 4.216667 & 101.416667 \\ \hline
6 & 230635.0 & 3.529184 & 5.314992 & 0.0 & 0.350000 & 2.150000 & 4.216667 & 100.083333 \\ \hline
7 & 237444.0 & 3.918536 & 5.569611 & 0.0 & 1.050000 & 2.300000 & 5.066667 & 99.000000 \\ \hline
8 & 244180.0 & 4.156501 & 7.003173 & 0.0 & 0.983333 & 2.283333 & 5.000000 & 119.683333 \\ \hline
9 & 214183.0 & 3.751553 & 5.985820 & 0.0 & 1.033333 & 2.183333 & 4.233333 & 110.050000 \\ \hline
10 & 219152.0 & 4.637056 & 7.950685 & 0.0 & 1.083333 & 2.916667 & 5.150000 & 119.050000 \\ \hline
11 & 203820.0 & 5.362490 & 7.557191 & 0.0 & 1.150000 & 3.183333 & 6.333333 & 117.000000 \\ \hline
12 & 436.0 & 3.526338 & 3.155593 & 0.0 & 1.083333 & 3.066667 & 5.150000 & 23.600000 \\ \hline
\end{tabular}
\caption{Estatística descritiva dos atrasos em minutos para a categoria Mês do ano }
\label{table:monthly_usage}
\end{table}



A variável explicativa e qualitativa \textit{Mês do ano} foi utilizada para investigar se itinerários realizados em diferentes meses impactam diretamente o comportamento de atraso das viagens. As 12 categorias correspondentes aos meses do ano foram consideradas e estão apresentadas na Tabela \ref{tab:meses}. \\

A Tabela \ref{table:monthly_usage} apresenta um resumo da estatística descritiva do tempo de atraso (em minutos) em função dos meses do ano.\\

\subsubsection{Variável explicativa : Mês do ano: Testes de análise de significancia estatística }

Para a obtenção dos p-values correspondentes a cada uma das categorias criadas na dummificação, foi ajustado um modelo de regressão logística conforme o código apresentado na Equação~\ref{eq:regressaol}. A categoria de referência adotada foi o Mês 1 (Janeiro). O resumo do modelo ajustado, bem como os respectivos valores de p-value, são apresentados na Figura~\ref{fig:Month}.\\



Ao analisar os p-values obtidos, observa-se que o contexto dos meses do ano é, em geral, significativo para a explicação dos atrasos. A exceção é o mês de dezembro, cujos resultados não passaram no teste de significância, indicando que essa categoria pode ser descartada.



\subsection{Variável explicativa : Padrão Horário ( P ) }


\begin{figure}[H]
\centering
\includegraphics[width=1\linewidth]{new_P-value_Pattern.png}
\caption{\label{fig:p-value_Padrao} Resultado do teste estatístico p-value para um intervalo de confiança de 0,95.}
\end{figure}


A variável explicativa e qualitativa \textit{Padrão de horários (Data Pattern)} foi utilizada para investigar se itinerários realizados em diferentes períodos do dia impactam diretamente o comportamento de atraso das viagens. Para essa análise, foram considerados seis intervalos de 4 horas cada, abrangendo os seguintes períodos: 0h–4h, 4h–8h, 8h–12h, 12h–16h, 16h–20h e 20h–24h.\\

A Tabela \ref{table:data_pattern_usage} apresenta um resumo da estatística descritiva do tempo de atraso (em minutos) em função do padrão horário.



\subsubsection{Variável explicativa : Padrão Horário : Testes de análise de significancia estatística }

Para a obtenção dos p-values correspondentes a cada uma das categorias criadas na dummificação, foi ajustado um modelo de regressão logística, conforme o código apresentado na Equação~\ref{eq:regressaol}. A categoria de referência adotada corresponde ao intervalo de horário compreendido entre 0h e 4h. O resumo do modelo ajustado, bem como os respectivos valores de p-value, é apresentado na Figura~\ref{fig:p-value_Padrao}.

A análise dos resultados do teste de significância dos p-values indica que o contexto do padrão horário é relevante para a explicação do padrão de atrasos.\\ 


\begin{table}[h]
\centering
\begin{tabular}{|c|c|c|c|c|c|c|c|c|}
\hline
\textbf{Month} & \textbf{count} & \textbf{mean} & \textbf{std} & \textbf{min} & \textbf{25\%} & \textbf{50\%} & \textbf{75\%} & \textbf{max} \\ \hline
        Antes 4          & 88.661  & 4,88  & 8,66  & 0,00  & 0,50  & 2,30  & 6,03  & 326,00 \\
        Entre 4 e 8    & 419.348 & 2,68  & 3,80  & 0,00  & 0,43  & 2,07  & 3,25  & 114,55 \\
        Entre 8 e 12   & 521.914 & 4,24  & 6,15  & 0,00  & 1,12  & 2,43  & 5,13  & 117,78 \\
        Entre 12 e 16  & 439.056 & 3,91  & 5,73  & 0,00  & 1,07  & 2,25  & 5,07  & 147,73 \\
        Entre 16 e 20  & 666.010 & 4,42  & 6,93  & 0,00  & 1,07  & 2,58  & 5,22  & 153,13 \\
        Entre 20 e 24  & 401.105 & 4,55  & 7,82  & 0,00  & 1,05  & 2,32  & 5,13  & 117,00 \\
\end{tabular}
\caption{Estatística descritiva dos atrasos em minutos para a categoria padrão horário }
\label{table:data_pattern_usage}
\end{table}

  





\subsection{Variável explicativa : Estações( Sta ) }


A variável explicativa e qualitativa \textit{Estações} foi utilizada para investigar se itinerários com destino a estações específicas impactam diretamente o comportamento de atraso das viagens. Foram consideradas as 165 estações presentes na base de dados como categorias dessa variável. As tabelas apresentadas no Apêndice \ref{table:results} mostram os resultados e os nomes das estações que permaneceram no modelo.


\subsubsection{Variável explicativa : Estações : Testes de análise de significancia estatística }

Para a obtenção dos p-values correspondentes a cada uma das categorias criadas na dummificação, foi ajustado um modelo de regressão logística conforme o código apresentado na Equação~\ref{eq:regressaol}. A categoria de referência adotada corresponde à estação \textit{Aberdeen-Matawan}.\\

De maneira geral, observa-se que as categorias associadas aos nomes das estações apresentam p-values inferiores a 0{,}05, indicando que o contexto de estação é relevante para a análise a ser realizada. Algumas categorias, entretanto, não passaram no teste de significância, sendo possível removê-las do modelo final por meio da aplicação de um procedimento stepwise.



\subsection{Variável explicativa : Sequência de paradas ( Seq ) }

A variável explicativa e qualitativa \textit{Sequência de paradas} foi utilizada para investigar se a posição de uma viagem dentro de um itinerário específico influencia o tempo de atraso. Em outras palavras, busca-se compreender se o fato de um trecho estar no início ou no final de um itinerário impacta diretamente os tempos de atraso. Essa variável é tratada como categórica, com categorias variando de 1 a 26, sendo 1 a primeira estação e 26 a última estação de cada itinerário.


\subsubsection{Variável explicativa : Sequência de paradas: Testes de análise de significancia estatística }

Para a obtenção dos p-values correspondentes a cada uma das categorias criadas na dummificação, foi ajustado um modelo de regressão logística, conforme o código apresentado na Equação~\ref{eq:regressaol}. A categoria de referência adotada corresponde à primeira estação do itinerário (stop sequence 1).

Observa-se que as categorias relacionadas à sequência de paradas apresentam p-values inferiores a 0.05 indicando que esse contexto é relevante para a análise. Os resultados obtidos podem ser visualizados na Figura~\ref{fig:p-value_seq}.



\begin{figure}[H]
\centering
\includegraphics[width=1\linewidth]{New_P-value_stopsequence.png}
\caption{\label{fig:p-value_seq} Resultado do teste estatístico p-value para o contexto Sequência de paradas usando intervalo de confiança de 0.95.}
\end{figure}










\subsection{Variável explicativa : Clusterização geográfica (Cg) }


As variáveis explicativas e qualitativas \textit{Clusterização geográfica} foram utilizadas para investigar se a localização geográfica de uma estação pode influenciar os tempos de atraso em uma linha.

Foi proposta uma clusterização baseada nas coordenadas de latitude e longitude, empregando dois métodos distintos: o método \textit{k-means} e o método \textit{DBSCAN}.

Ambas as abordagens serão apresentadas, sendo selecionada, ao final, aquela que apresentar melhor desempenho na construção do modelo.



\subsubsection{Variável explicativa : Clusterização espacial : Kmeans }
\label{sec:Variável explicativa : Clusterização espacial : Kmeans}

Utilizando as variáveis \textit{latitude} e \textit{longitude} referentes à posição geográfica de cada estação, foram calculados os respectivos clusters, conforme ilustrado na Figura~\ref{fig:Clusterk-means mapa}.

A Tabela~\ref{table:kmeans_clusters} apresenta um resumo descritivo do tempo de atraso, em minutos, para cada um dos clusters formados pelo método \textit{k-means}.


\begin{figure}[H]
\centering
\includegraphics[width=1\linewidth]{k-means.png}
\caption{\label{fig:Clusterk-means mapa} 8 Clusters criados na clusterização por k-means.}
\end{figure}

\begin{table}[h]
\centering
\begin{tabular}{|c|c|c|c|c|c|c|c|c|}
\hline
\textbf{cluster\_kmeans} & \textbf{count} & \textbf{mean} & \textbf{std} & \textbf{min} & \textbf{25\%} & \textbf{50\%} & \textbf{75\%} & \textbf{max} \\ \hline
0 & 248839.0 & 3.626307 & 6.611997 & 0.0 & 0.033333 & 1.300000 & 4.250000 & 118.466667 \\ \hline
1 & 196605.0 & 4.706683 & 6.676863 & 0.0 & 1.133333 & 3.083333 & 6.000000 & 326.000000 \\ \hline
2 & 226540.0 & 3.826557 & 7.093974 & 0.0 & 0.450000 & 2.133333 & 4.166667 & 117.000000 \\ \hline
3 & 34236.0 & 4.665933 & 8.292705 & 0.0 & 0.216667 & 2.183333 & 5.166667 & 119.683333 \\ \hline
4 & 45106.0 & 4.967763 & 6.707136 & 0.0 & 1.000000 & 3.300000 & 6.183333 & 104.033333 \\ \hline
5 & 834282.0 & 3.915531 & 6.098008 & 0.0 & 0.700000 & 2.233333 & 5.000000 & 153.133333 \\ \hline
6 & 720593.0 & 4.573561 & 6.849335 & 0.0 & 1.150000 & 3.050000 & 5.216667 & 326.000000 \\ \hline
7 & 417408.0 & 3.744723 & 5.126842 & 0.0 & 1.150000 & 2.300000 & 4.316667 & 107.283333 \\ \hline
\end{tabular}
\caption{Estatística descritiva dos atrasos em minutos para a categoria Clusterização K-Means}
\label{table:kmeans_clusters}
\end{table}






Para a definição da quantidade de clusters, foi utilizado o método do \textit{cotovelo} (\textit{Elbow Method}). O gráfico correspondente pode ser visualizado na Figura~\ref{fig:elbow}. Com base na análise do gráfico, optou-se pela escolha de 8 clusters. O método de escolha da quantidade de clusters é descrito em \ref{sec:Clusterização : K-means: Método de parada}.



\begin{figure}[H]
\centering
\includegraphics[width=1\linewidth]{elbow.png}
\caption{\label{fig:elbow} Gráfico elbow utilizado para seleção da quantidade de clusters.}
\end{figure}


\subsubsection{Variável explicativa : Clusterização espacial : Avaliação de significancia estatística k-means }

Para a obtenção dos p-values correspondentes a cada uma das categorias criadas na dummificação, foi ajustado um modelo de regressão logística, conforme o código apresentado na Equação~\ref{eq:regressaol}. A categoria de referência adotada corresponde ao \textit{Cluster 0}.

O resumo do modelo ajustado, bem como os valores dos p-values obtidos, estão apresentados na Figura~\ref{fig:p-valueKmeans}.



\begin{figure}[H]
\centering
\includegraphics[width=1\linewidth]{new-pvalue-kmeans.png}
\caption{\label{fig:p-valueKmeans} P-values para as variáveis de clusterização k-means.}
\end{figure}







\subsubsection{Variável explicativa : Clusterização espacial : DBscan }
\label{sec:Variável explicativa : Clusterização espacial : DBscan}

Utilizando as variáveis \textit{latitude} e \textit{longitude} referentes à posição geográfica de cada estação, e adotando como métrica de distância a distância de Haversine — escolhida por sua capacidade de calcular distâncias com precisão considerando a curvatura da Terra, sendo essencial em aplicações que envolvem dados geoespaciais~\cite{Sinnott1984} —, foram formados os clusters a partir do método \textit{DBSCAN}, conforme ilustrado na Figura~\ref{fig:Cluster-DBscan}.

A Tabela~\ref{table:dbscan_clusters} apresenta um resumo descritivo do tempo de atraso, em minutos, em função dos clusters criados com o método \textit{DBSCAN}.






\begin{figure}[H]
\centering
\includegraphics[width=1\linewidth]{DBscan.png}
\caption{\label{fig:Cluster-DBscan} Aplicação do método DBscan para a formação de 4 Clusteres.}
\end{figure}

Para conseguir encontrar esses clusteres, foram utilizadas as seguinte métricas de parametrização:

ϵ = 0.18
MinPts = 4

A curva obtida utilizando o método do \textit{Nearest Neighbor}, em conjunto com a identificação do ponto de inflexão (\textit{Joelho}), está apresentada na Figura~\ref{fig:Nerest-Neighbor}.



\begin{figure}[H]
\centering
\includegraphics[width=1\linewidth]{Neireghst neigbor.png}
\caption{\label{fig:Nerest-Neighbor} Aplicação da identificação de joelho para parametrização do dbscan.}
\end{figure}


\subsubsection{Variável explicativa : Clusterização espacial : Avaliação de significancia estatística DB-scan }

Para a obtenção dos p-values correspondentes a cada uma das categorias criadas na dummificação, foi ajustado um modelo de regressão logística, conforme o código apresentado na Equação~\ref{eq:regressaol}. A categoria de referência adotada corresponde ao \textit{Cluster 0}.

O resumo do modelo ajustado, bem como os valores dos p-values obtidos, estão apresentados na Figura~\ref{fig:p-valueDbscan}.


\begin{figure}[H]
\centering
\includegraphics[width=1\linewidth]{new_p-value dbscan.png}
\caption{\label{fig:p-valueDbscan} P-values para as variáveis de clusterização Dbscan.}
\end{figure}

\begin{table}[h]
\centering
\begin{tabular}{|c|c|c|c|c|c|c|c|c|}
\hline
\textbf{cluster\_DBscan} & \textbf{count} & \textbf{mean} & \textbf{std} & \textbf{min} & \textbf{25\%} & \textbf{50\%} & \textbf{75\%} & \textbf{max} \\ \hline
0 & 19020.0 & 5.003146 & 8.242052 & 0.0 & 1.100000 & 3.016667 & 5.483333 & 119.683333 \\ \hline
1 & 15216.0 & 4.244417 & 8.336699 & 0.0 & 0.033333 & 1.316667 & 4.516667 & 100.216667 \\ \hline
2 & 2562658.0 & 4.170338 & 6.393837 & 0.0 & 1.100000 & 2.350000 & 5.100000 & 326.000000 \\ \hline
3 & 126715.0 & 2.816788 & 5.831591 & 0.0 & 0.000000 & 0.283333 & 3.233333 & 118.466667 \\ \hline
\end{tabular}
\caption{Estatística descritiva dos atrasos em minutos para a categoria Clusterização DBSCAN}
\label{table:dbscan_clusters}
\end{table}

\subsection{Variável explicativa : Variáveis Retiradas da Análise de redes (SNA) }

O objetivo desta seção é analisar a influência de métricas obtidas por meio de uma análise de redes sobre o comportamento dos tempos de atraso das viagens. Para isso, foi realizada uma modelagem da estrutura da malha ferroviária utilizando o software \textit{Gephi}~\cite{bastian2009gephi} e a biblioteca \textit{NetworkX} em Python~\cite{hagberg2008exploring}. 

A Figura~\ref{fig:rede} apresenta um esboço da rede construída, utilizando as estações como nós, e suas conexões como ligações.


\begin{figure}[H]
\centering
\includegraphics[width=0.5\linewidth]{rede.png}
\caption{\label{fig:rede} Esboço da interconexão entre nós da malha ferróviaria usando o software Gephi.}
\end{figure}




A partir da análise de redes, foram obtidas as seguintes conclusões:\\

A malha ferroviária da NJ Transit constitui uma rede com baixa densidade, apresentando um valor de aproximadamente 0.013. O comprimento médio do caminho mais curto (\textit{Average Shortest Path Length}) é de cerca de 19.30, o que indica que a rede é extensa, exigindo a travessia de muitos nós para se deslocar de um ponto a outro.

Observou-se também que algumas estações desempenham papéis mais centrais na rede, segundo a métrica de \textit{Betweenness Centrality}. A Tabela~\ref{table:centrality} apresenta a lista das estações mais centrais, ordenadas em ordem decrescente de centralidade.



\subsubsection{Variável explicativa : Variáveis Retiradas da Análise de redes (SNA): Análise de significância estatísitica.
}

Por fim, concluímos a análise com a obtenção das seguintes variáveis quantitativas, derivadas da análise de redes:


\begin{enumerate}
    \item Betweenness Centrality (CB)
    \item Closeness Centrality (CC)
    \item Clustering Coefficient (C)
    \item Degree (D)
\end{enumerate}

Para avaliar a significância estatística de cada uma dessas variáveis, foi executado um modelo de regressão logística, utilizando o código apresentado na Equação~\ref{eq:regressaol}.\\

O resumo do modelo executado e os valores de p-value obtidos estão apresentados na Figura~\ref{fig:network}.\\

Os resultados indicam que todas as variáveis analisadas passam no teste de significância (p-value < 0,05) e, portanto, podem ser utilizadas como variáveis explicativas em modelos preditivos. 



\begin{table}[h]
\centering
\begin{tabular}{l c}

\textbf{Station} & \textbf{Centrality} \\

Hoboken              & 0.380254777070064 \\
New York Penn Station & 0.382165605095541 \\
Newark Broad Street  & 0.39140127388535 \\
Linden               & 0.397452229299363 \\
Elizabeth            & 0.398089171974522 \\
North Elizabeth      & 0.398726114649682 \\
Newark Airport       & 0.399363057324841 \\
Secaucus Upper Lvl   & 0.412101910828025 \\
Rahway               & 0.42484076433121 \\
Secaucus Lower Lvl   & 0.428025477707006 \\
Newark Penn Station  & 0.457324840764331 \\ 

\end{tabular}
\caption{Centralidade das Estações}
\label{table:centrality}
\end{table}


\begin{figure}[H]
\centering
\includegraphics[width=1\linewidth]{new_p-value_network.png}
\caption{\label{fig:network} Resultado do teste estatístico p-value para um intervalo de confiança de 0,95.}
\end{figure}


\section{Modelagem}
\label{Sec:Modelagem}

Nesta seção, será desenvolvida uma modelagem para a previsão de atrasos, utilizando a regressão logística binária como modelo preditivo. 


\subsection{Regressão logística.}


O objetivo desta seção é desenvolver um modelo capaz de prever se um trecho de viagem apresentará um atraso superior a um minuto, com base nas variáveis explicativas definidas na Seção~\ref{sec:Variáveis alvo e explicativas}.O modelo utilizado será a regressão logística binária.\\


Conforme descrito na Seção~\ref{sec:Variável Alvo : Uso no modelo Binomial(AtrEvent)}, será estabelecido um ponto de corte para a variável de atraso, classificando trechos com atraso maior ou igual a um minuto como eventos, e trechos com atraso inferior a um minuto como não eventos.

O ajuste do modelo de regressão logística será realizado conforme o código em Python apresentado na Equação~\ref{eq:regressaol}.


\begin{equation}
\begin{split}
\text{modelo\_Logistico\_all\_variables} &= \text{smf.glm(formula=formula\_dummies\_modelo\_Logistico,} \\
&\phantom{=} \text{data=df\_all\_variables\_Logistico, family=sm.families.Binomial()).fit()}
\end{split}
\label{eq:regressaol}
\end{equation}



O modelo criado é exemplificado pela equação descrita no Capítulo~\ref{sec:Regressão logística}.

Após a aplicação do procedimento stepwise para a remoção de variáveis sem significância estatística, conforme descrito na Seção~\ref{sec: Análise de significância : Seleção Stepwise}, os resultados detalhados do modelo ajustado podem ser consultados no Apêndice~\ref{sec:Generalized Linear Model Regression Results}.\\

\textbf{Observação:} Por questões de desempenho computacional, foi utilizada uma quantidade reduzida de observações da base de dados para o cálculo dos valores de p-value e para o processamento final do modelo após a aplicação do procedimento stepwise.


\subsection{Regressão logística: Modelo usando todas as variáveis explicativas}


\subsubsection{Função de probabilidade do evento }

Após a execução do modelo contendo todas as variáveis selecionadas pelo procedimento stepwise, conforme descrito na Seção~\ref{sec:Generalized Linear Model Regression Results}, obtivemos os seguintes resultados:

A relação entre a probabilidade de ocorrência de um evento e o logito, conforme discutido na Seção~\ref{sec:Regressão logística}, é apresentada na Figura~\ref{fig:PxLogito}.


\begin{figure}[H]
\centering
\includegraphics[width=0.5\linewidth]{Prbabilidade x logit.png}
\caption{\label{fig:PxLogito} Probabilidade de ocorrência do evento em função do logito}
\end{figure}

\subsubsection{Sensibilidade, Especificidade e acurácia }

As curvas de Sensibilidade e Especificidade em função do valor de cutoff são apresentadas na Figura~\ref{fig:Sensxespecif}.\\

Analisando a figura, observa-se que a adoção de um cutoff em aproximadamente 0.81 permite maximizar tanto a especificidade quanto a sensibilidade do modelo. Esse valor será adotado como ponto de corte, pois, embora não maximize a acurácia total, proporciona um melhor balanceamento entre a taxa de acertos dos eventos e dos não eventos.





\begin{figure}[H]
\centering
\includegraphics[width=0.5\linewidth]{sensibilidade x especificidade.png}
\caption{\label{fig:Sensxespecif} Curva Especificadade ou sensibilidade x cutoff (Definição de evento) }
\end{figure}

Nesse ponto, os principais indicadores de desempenho do modelo são:

\begin{itemize}
    \item \textbf{Cutoff:} 0.81
    \item \textbf{Sensibilidade:} 0.702
    \item \textbf{Especificidade:} 0.684
    \item \textbf{Acurácia:} 0.697
\end{itemize}



\subsubsection{Curva ROC}

A curva ROC do modelo logístico é apresentada na Figura~\ref{fig:roc}.

Os principais resultados obtidos foram:
\begin{itemize}
    \item \textbf{Área abaixo da curva ROC (AUC):} 0.7662
    \item \textbf{Coeficiente de Gini:} 0.5323
\end{itemize}

Observa-se que a área de 0.76 abaixo da curva ROC indica que o modelo apresenta boa capacidade preditiva, conforme discutido na Seção~\ref{sec:Área Sob a Curva ROC (AUC - Area Under the Curve)}.



\begin{figure}[H]
\centering
\includegraphics[width=0.5\linewidth]{curca roc.png}
\caption{\label{fig:roc} Curva ROC para o modelo utilizando todas as variavéis preditivas e uma definição de evento de um minuto }
\end{figure}

\subsection{Regressão Logística: Modelo Utilizando as Variáveis \textit{Linha}, \textit{Meses} e \textit{Padrão horário}}


Para realizar uma comparação direta entre as variáveis que mais influenciam o comportamento dos atrasos, foram ajustados modelos separados, considerando diferentes conjuntos de variáveis preditoras.\\

Ao ajustar um modelo apenas com as variáveis categóricas \textit{Linha}, \textit{Meses} e \textit{Padrão de Horário}, obteve-se a seguinte curva ROC, apresentada na Figura~\ref{fig:roc2}.



\begin{figure}[H]
\centering
\includegraphics[width=0.5\linewidth]{curva roc2.png}
\caption{\label{fig:roc2} Curva ROC para o modelo utilizando Mês, Linha e Padrão horário como variáveis preditoras e uma definição de evento de um minuto. }
\end{figure}

Observa-se que, embora essas variáveis tenham apresentado significância estatística nos testes realizados, sua contribuição para o poder preditivo do modelo é limitada. Isso é evidenciado pela considerável redução da área sob a curva ROC ao utilizar apenas essas variáveis preditoras, indicando que possuem menor relevância na construção do modelo.


\subsection{Regressão Logística: Uso de métricas de rede}

Ao executar um modelo considerando apenas as variáveis quantitativas \textit{Betweenness Centrality}, \textit{Closeness Centrality}, \textit{Clustering Coefficient} e \textit{Degree}, foi obtida a curva ROC apresentada na Figura~\ref{fig:roc3}.



\begin{figure}[H]
\centering
\includegraphics[width=0.5\linewidth]{curva roc3.png}
\caption{\label{fig:roc3} Curva ROC para o modelo utilizando métricas de rede como variáveis preditoras e uma definição de evento de um minuto.}
\end{figure}

Observa-se que essas variáveis também apresentam baixa influência na capacidade preditiva do modelo.


\subsection{ Modelo Utilizando a Variável da categoria \textit{Estação}}

Ao executar um modelo considerando apenas as variáveis categóricas relacionadas à dummyzação do destino de viagem (estações), foi obtida a curva ROC apresentada na Figura~\ref{fig:roc4}.


\begin{figure}[H]
\centering
\includegraphics[width=0.5\linewidth]{curva roc 4.png}
\caption{\label{fig:roc4} Curva ROC para o modelo utilizando a categoria \textit{Estação} como variável preditora e uma definição de evento de um minuto. }
\end{figure}

Observa-se que essa variável categórica apresenta o maior impacto na capacidade preditiva do modelo, indicando que o comportamento de atrasos superiores a 1 minuto está fortemente associado a estações específicas que, por diversos fatores, contribuem para a ocorrência de atrasos nas linhas. Esse resultado é evidenciado pela elevada área sob a curva ROC obtida utilizando apenas essa variável.



\subsection{Regressão Logística:Modelo Utilizando a Variável da categoria \textit{Sequência de parada}}

Ao executar um modelo utilizando apenas as variáveis categóricas relacionadas à dummyzação da variável "sequência de estações", obtivemos a



\begin{figure}[H]
\centering
\includegraphics[width=0.5\linewidth]{curva roc5.png}
\caption{\label{fig:roc5} Curva ROC para o modelo utilizando a categoria \textit{Sequência de parada} como variável preditora e uma definição de evento de um minuto. }
\end{figure}

Podemos observar que a variável categórica \textit{sequência de parada} também apresenta um forte comportamento preditivo. Contudo, esse resultado pode ser explicado pelo fato de que as estações, em geral, possuem um posicionamento fixo na sequência de paradas, o que implica em uma forte correlação entre essa variável e a variável categórica de \textit{estações}.



\subsection{Regressão Logística:Influência da seleção do corte para definição de evento}
\label{sec:Influência da seleção de cuttof para definição de evento}

Foi escolhido um valor de atraso superior a 1 minuto para a definição de evento de atraso. No entanto, surge a questão: como o modelo se comportaria caso adotássemos um critério diferente? A capacidade preditiva se manteria a mesma? \\

As figuras \ref{fig:roc_evolucao_2}, \ref{fig:roc_evolucao_3}, \ref{fig:roc_evolucao_4} e \ref{fig:roc_evolucao_5} mostram a evolução do gráfico da curva ROC para definições de atraso variando entre 1 e 3 minutos.\\

Analisando essas figuras, podemos observar que a área sob a curva ROC diminui à medida que aumentamos o tempo utilizado como critério para definir um atraso. Isso indica que as variáveis disponíveis possuem boa capacidade preditiva para explicar a ocorrência de pequenos atrasos. Entretanto, conforme o critério de atraso aumenta, a capacidade explicativa do modelo diminui, sugerindo que não há variáveis suficientemente fortes para prever atrasos mais longos.


\begin{figure}[H]
\centering
\begin{minipage}{0.45\linewidth}
    \centering
    \includegraphics[width=0.95\linewidth]{curvaroc1.0.png}
    \caption{\label{fig:roc_evolucao_2} Curva ROC para o modelo utilizando todas as variavéis preditivas e uma definição de evento de 1 minuto}
\end{minipage}
\hfill
\begin{minipage}{0.45\linewidth}
    \centering
    \includegraphics[width=0.95\linewidth]{curva roc 1.5.png}
    \caption{\label{fig:roc_evolucao_3} Curva ROC para o modelo utilizando todas as variavéis preditivas e uma definição de evento de 1.5 minutos}
\end{minipage}
\end{figure}

\begin{figure}[H]
\centering
\begin{minipage}{0.45\linewidth}
    \centering
    \includegraphics[width=0.95\linewidth]{curva roc 2.0.png}
    \caption{\label{fig:roc_evolucao_4} Curva ROC para o modelo utilizando todas as variavéis preditivas e uma definição de evento de 2 minutos}
\end{minipage}
\hfill
\begin{minipage}{0.45\linewidth}
    \centering
    \includegraphics[width=0.95\linewidth]{curva roc 3.0.png}
    \caption{\label{fig:roc_evolucao_5} Curva ROC para o modelo utilizando todas as variavéis preditivas e uma definição de evento de 3 minutos}
\end{minipage}
\end{figure}


\subsection{Regressão Logística:Análise de fatores que mais Influênciam na probabilidade de ocorrência de evento}

\begin{table}[h]
\centering
\caption{Tabela de Variáveis, Coeficientes e Comentários}
\label{Tab:analise}
\begin{tabular}{|l|c|p{8cm}|}
\hline
\textbf{Variável} & \textbf{Coeficiente} & \textbf{Comentário} \\ \hline
Centrality & 1.6008 & O parâmetro de centralidade nos indica que viagens realizadas em estações centrais da linha têm uma maior probabilidade de atrasos maiores que 1 minuto. \\ \hline
Sequencia de parada 26 & 3.0421 & O parâmetro de stop sequence 26 nos indica que viagens realizadas nessa posição têm uma alta probabilidade de sofrerem atrasos de mais de 1 minuto. \\ \hline
Linha Princeton Shuttle & -3.5961 & Nos indica que viagens realizadas nessa linha têm baixa probabilidade de atrasos maiores que 1 minuto. \\ \hline
Hackettstown & -2.4420 & Nos indica que viagens realizadas nessa estação possuem baixa probabilidade de atrasos maiores que 1 minuto. \\ \hline
Main\_Line & 0.5994 & Nos indica que viagens realizadas nessa linha possuem uma probabilidade de atraso considerável (maior entre todas as linhas). \\ \hline
Lindenwold & 1.4527 & Nos indica que viagens realizadas nessa estação possuem alta probabilidade de atrasos maiores que 1 minuto. \\ \hline
\end{tabular}
\end{table}

    
Analisando o gráfico apresentado na Figura \ref{fig:PxLogito}, podemos observar que fatores que aumentam a probabilidade de ocorrência do evento (atraso) são aqueles que contribuem positivamente para o valor do logito. \\

Com base nessa observação e na análise dos coeficientes estimados, apresentados no Capítulo \ref{sec:Generalized Linear Model Regression Results}, é possível extrair algumas conclusões, resumidas na Tabela \ref{Tab:analise}.\\

Ao final, a análise apresentada na Tabela \ref{Tab:analise} auxilia na identificação dos principais fatores que influenciam a geração de atrasos na linha estudada, com base nos dados disponíveis.







\section{Conclusão}

Este trabalho realizou uma análise da influência de diversos fatores no atraso de viagens em uma malha ferroviária de passageiros, utilizando a "NJ Transit" como base de estudo. 

Ressalta-se que a análise não contemplou todos os fatores que podem impactar os atrasos no dia a dia, como variáveis ausentes na base de dados ou fatores pontuais e caóticos, de difícil mensuração convencional.\\

Os resultados obtidos foram satisfatórios, evidenciando que os principais fatores que influenciam os atrasos estão associados às características específicas de cada estação, capturadas pela categorização \textit{Estações}.\\

Técnicas similares podem ser aplicadas em outras redes ferroviárias ao redor do mundo, desde que seja possível realizar uma mensuração adequada dos tempos de atraso e das variáveis explicativas associadas.


\section{Referências}
Seção dedicada as referências bibliográfica.

\printbibliography[heading=none]

\section{Apêndice}
\subsection{Generalized Linear Model Regression Results}
\label{sec:Generalized Linear Model Regression Results}

\begin{tabular}{l l}
Dep. Variable: & delay\_minutes\_Event \\
No. Observations: & 122522 \\
Model: & GLM \\
Df Residuals: & 122379 \\
Model Family: & Binomial \\
Df Model: & 142 \\
Link Function: & Logit \\
Scale: & 1.0000 \\
Method: & IRLS \\
Log-Likelihood: & -54126 \\
Date: & Sun, 13 Apr 2025 \\
Deviance: & 1.0825e+05 \\
Time: & 22:17:29 \\
Pearson chi2: & 1.24e+05 \\
No. Iterations: & 11 \\
Pseudo R-squ. (CS): & 0.1875 \\
Covariance Type: & nonrobust \\
\end{tabular}

\begin{table}[h]
\centering
\begin{tabular}{l c c c c c c}

\textbf{Variable} & \textbf{Coef} & \textbf{Std Err} & \textbf{z} & \textbf{P>|z|} & \textbf{[0.025} & \textbf{0.975]} \\


Intercept                              & -0.3009 & 0.047 & -6.444 & 0.000 & -0.392 & -0.209 \\
Q('cluster kmeans 1')                  & 0.4853 & 0.113 & 4.311 & 0.000 & 0.265 & 0.706 \\
Q('cluster kmeans 3')                  & 0.3029 & 0.105 & 2.875 & 0.004 & 0.096 & 0.509 \\
Q('line Bergen Co Line')               & 0.3108 & 0.041 & 7.594 & 0.000 & 0.231 & 0.391 \\
Q('line Gladstone Branch')             & 0.1912 & 0.042 & 4.566 & 0.000 & 0.109 & 0.273 \\
Q('line Main Line')                    & 0.5994 & 0.046 & 13.130 & 0.000 & 0.510 & 0.689 \\
Q('line Montclair Boonton')            & 0.5104 & 0.042 & 12.011 & 0.000 & 0.427 & 0.594 \\
Q('line Morristown Line')              & 0.4463 & 0.038 & 11.645 & 0.000 & 0.371 & 0.521 \\
Q('line No Jersey Coast')              & 0.5469 & 0.047 & 11.749 & 0.000 & 0.456 & 0.638 \\
Q('line Northeast Corrdr')             & 0.5978 & 0.048 & 12.545 & 0.000 & 0.504 & 0.691 \\
Q('line Pascack Valley')               & 0.3445 & 0.045 & 7.606 & 0.000 & 0.256 & 0.433 \\
Q('line Princeton Shuttle')            & -3.5961 & 0.259 & -13.897 & 0.000 & -4.103 & -3.089 \\
Q('line Raritan Valley')               & -0.5548 & 0.076 & -7.296 & 0.000 & -0.704 & -0.406 \\
Q('Month 10')                          & 0.1318 & 0.029 & 4.589 & 0.000 & 0.076 & 0.188 \\
Q('Month 11')                          & 0.1856 & 0.030 & 6.260 & 0.000 & 0.128 & 0.244 \\
Q('Month 3')                           & -0.3153 & 0.026 & -12.291 & 0.000 & -0.366 & -0.265 \\
Q('Month 6')                           & -0.1993 & 0.026 & -7.578 & 0.000 & -0.251 & -0.148 \\
Q('Month 8')                           & -0.0898 & 0.026 & -3.400 & 0.001 & -0.142 & -0.038 \\
Q('Data Pattern Entre 12 e 16')        & 0.0772 & 0.022 & 3.504 & 0.000 & 0.034 & 0.120 \\
Q('Data Pattern Entre 4 e 8')          & -0.2094 & 0.021 & -9.740 & 0.000 & -0.252 & -0.167 \\
Q('Data Pattern Entre 8 e 12')        & 0.2105 & 0.021 & 10.067 & 0.000 & 0.170 & 0.252 \\
Q('to Absecon')                       & -0.8268 & 0.189 & -4.370 & 0.000 & -1.198 & -0.456 \\
Q('to Allenhurst')                    & -0.7150 & 0.177 & -4.040 & 0.000 & -1.062 & -0.368 \\
Q('to Annandale')                     & 0.9176 & 0.214 & 4.290 & 0.000 & 0.498 & 1.337 \\
Q('to Asbury Park')                   & -0.8756 & 0.165 & -5.305 & 0.000 & -1.199 & -0.552 \\
Q('to Atlantic City Rail Terminal')   & -2.1186 & 0.227 & -9.340 & 0.000 & -2.563 & -1.674 \\
Q('to Basking Ridge')                 & 0.8989 & 0.139 & 6.490 & 0.000 & 0.627 & 1.170 \\
Q('to Bay Head')                      & -1.1830 & 0.147 & -8.053 & 0.000 & -1.471 & -0.895 \\
Q('to Bay Street')                    & -0.4268 & 0.097 & -4.410 & 0.000 & -0.617 & -0.237 \\
Q('to Berkeley Heights')              & -0.6790 & 0.096 & -7.070 & 0.000 & -0.867 & -0.491 \\

\end{tabular}
\caption{Resumo dos Resultados de Coeficientes}
\label{table:results}
\end{table}

\begin{table}[h]
\centering
\begin{tabular}{l c c c c c c}

\textbf{Variable} & \textbf{Coef} & \textbf{Std Err} & \textbf{z} & \textbf{P>|z|} & \textbf{[0.025} & \textbf{0.975]} \\


Q('to Bound Brook')                   & 1.0448 & 0.136 & 7.658 & 0.000 & 0.777 & 1.312 \\
Q('to Bridgewater')                   & 1.3597 & 0.153 & 8.912 & 0.000 & 1.061 & 1.659 \\
Q('to Chatham')                       & 0.3073 & 0.100 & 3.074 & 0.002 & 0.111 & 0.503 \\
Q('to Cherry Hill')                   & 0.9549 & 0.300 & 3.188 & 0.001 & 0.368 & 1.542 \\
Q('to Clifton')                       & 0.9796 & 0.170 & 5.763 & 0.000 & 0.646 & 1.313 \\
Q('to Convent Station')               & 0.2698 & 0.099 & 2.732 & 0.006 & 0.076 & 0.463 \\
Q('to Cranford')                      & 1.1094 & 0.142 & 7.812 & 0.000 & 0.831 & 1.388 \\
Q('to Delawanna')                     & 1.1248 & 0.169 & 6.638 & 0.000 & 0.793 & 1.457 \\
Q('to Denville')                      & -0.2801 & 0.079 & -3.554 & 0.000 & -0.435 & -0.126 \\
Q('to Dover')                         & -1.1916 & 0.071 & -16.747 & 0.000 & -1.331 & -1.052 \\
Q('to Dunellen')                     & 1.1667 & 0.142 & 8.239 & 0.000 & 0.889 & 1.444 \\
Q('to East Orange')                  & -0.5326 & 0.097 & -5.510 & 0.000 & -0.722 & -0.343 \\
Q('to Edison')                       & -0.7732 & 0.086 & -8.953 & 0.000 & -0.943 & -0.604 \\
Q('to Egg Harbor City')              & -0.4269 & 0.206 & -2.072 & 0.038 & -0.831 & -0.023 \\
Q('to Elizabeth')                    & -0.4190 & 0.096 & -4.388 & 0.000 & -0.606 & -0.232 \\
Q('to Emerson')                      & -0.3056 & 0.123 & -2.483 & 0.013 & -0.547 & -0.064 \\
Q('to Essex Street')                 & -0.2734 & 0.124 & -2.209 & 0.027 & -0.516 & -0.031 \\
Q('to Fanwood')                      & 1.5455 & 0.162 & 9.567 & 0.000 & 1.229 & 1.862 \\
Q('to Garfield')                     & 1.2528 & 0.238 & 5.262 & 0.000 & 0.786 & 1.719 \\
Q('to Garwood')                      & 1.4710 & 0.212 & 6.949 & 0.000 & 1.056 & 1.886 \\
Q('to Gillette')                     & 0.4157 & 0.117 & 3.563 & 0.000 & 0.187 & 0.644 \\
Q('to Gladstone')                    & -1.2176 & 0.108 & -11.321 & 0.000 & -1.428 & -1.007 \\
Q('to Glen Ridge')                   & 0.2759 & 0.128 & 2.150 & 0.032 & 0.024 & 0.527 \\
Q('to Glen Rock Boro Hall')          & 0.6507 & 0.148 & 4.392 & 0.000 & 0.360 & 0.941 \\
Q('to Glen Rock Main Line')          & 0.8360 & 0.162 & 5.168 & 0.000 & 0.519 & 1.153 \\
Q('to Hackettstown')                 & -2.4420 & 0.238 & -10.272 & 0.000 & -2.908 & -1.976 \\
Q('to Hamilton')                     & -1.0784 & 0.081 & -13.361 & 0.000 & -1.237 & -0.920 \\
Q('to Hawthorne')                    & 0.9129 & 0.167 & 5.480 & 0.000 & 0.586 & 1.239 \\
Q('to High Bridge')                  & -1.0051 & 0.216 & -4.659 & 0.000 & -1.428 & -0.582 \\
Q('to Ho Ho Kus')                    & 0.4382 & 0.102 & 4.294 & 0.000 & 0.238 & 0.638 \\


\end{tabular}
\caption{Resumo dos Resultados de Coeficientes}
\label{table:results}
\end{table}


\begin{table}[h]
\centering
\begin{tabular}{l c c c c c c}

\textbf{Variable} & \textbf{Coef} & \textbf{Std Err} & \textbf{z} & \textbf{P>|z|} & \textbf{[0.025} & \textbf{0.975]} \\

Q('to Hoboken')                        & -2.0710 & 0.057 & -36.409 & 0.000 & -2.183 & -1.960 \\
Q('to Jersey Avenue')                  & -1.4446 & 0.100 & -14.514 & 0.000 & -1.640 & -1.250 \\
Q('to Kingsland')                      & 0.6686 & 0.153 & 4.364 & 0.000 & 0.368 & 0.969 \\
Q('to Lake Hopatcong')                 & -0.4684 & 0.145 & -3.226 & 0.001 & -0.753 & -0.184 \\
Q('to Lebanon')                        & 0.7942 & 0.235 & 3.385 & 0.001 & 0.334 & 1.254 \\
Q('to Linden')                         & -0.3967 & 0.097 & -4.071 & 0.000 & -0.588 & -0.206 \\
Q('to Lindenwold')                     & 1.4527 & 0.344 & 4.228 & 0.000 & 0.779 & 2.126 \\
Q('to Little Falls')                   & 0.8813 & 0.282 & 3.129 & 0.002 & 0.329 & 1.433 \\
Q('to Little Silver')                  & -0.6825 & 0.137 & -4.975 & 0.000 & -0.951 & -0.414 \\
Q('to Long Branch')                    & -2.3124 & 0.121 & -19.066 & 0.000 & -2.550 & -2.075 \\
Q('to Lyndhurst')                      & 1.0214 & 0.172 & 5.941 & 0.000 & 0.684 & 1.358 \\
Q('to Madison')                        & 0.6537 & 0.111 & 5.884 & 0.000 & 0.436 & 0.872 \\
Q('to Maplewood')                      & 0.4902 & 0.092 & 5.350 & 0.000 & 0.311 & 0.670 \\
Q('to Metropark')                      & -0.5027 & 0.091 & -5.537 & 0.000 & -0.681 & -0.325 \\
Q('to Metuchen')                       & -0.6323 & 0.089 & -7.088 & 0.000 & -0.807 & -0.457 \\
Q('to Millburn')                       & 0.2935 & 0.086 & 3.394 & 0.001 & 0.124 & 0.463 \\
Q('to Montvale')                       & -0.3495 & 0.116 & -3.003 & 0.003 & -0.578 & -0.121 \\
Q('to Morristown')                     & 0.2658 & 0.099 & 2.691 & 0.007 & 0.072 & 0.459 \\
Q('to Mount Tabor')                    & -0.7317 & 0.110 & -6.625 & 0.000 & -0.948 & -0.515 \\
Q('to Mountain Station')               & -0.3655 & 0.097 & -3.774 & 0.000 & -0.555 & -0.176 \\

\end{tabular}
\caption{Resumo dos Resultados de Coeficientes}
\label{table:results}
\end{table}

\begin{table}[h]
\centering
\begin{tabular}{l c c c c c c}

\textbf{Variable} & \textbf{Coef} & \textbf{Std Err} & \textbf{z} & \textbf{P>|z|} & \textbf{[0.025} & \textbf{0.975]} \\
Q('to Mountain View')                 & 0.8632 & 0.281 & 3.073 & 0.002 & 0.313 & 1.414 \\
Q('to Murray Hill')                   & -0.4648 & 0.093 & -5.006 & 0.000 & -0.647 & -0.283 \\
Q('to Netherwood')                    & 1.5026 & 0.160 & 9.374 & 0.000 & 1.188 & 1.817 \\
Q('to New Brunswick')                 & -0.8186 & 0.084 & -9.739 & 0.000 & -0.983 & -0.654 \\
Q('to New Providence')                & -0.9143 & 0.091 & -10.078 & 0.000 & -1.092 & -0.737 \\
Q('to New York Penn Station')         & -2.3241 & 0.063 & -37.168 & 0.000 & -2.447 & -2.202 \\
Q('to Newark Airport')                & -0.4655 & 0.090 & -5.188 & 0.000 & -0.641 & -0.290 \\
Q('to Newark Penn Station')           & -1.2179 & 0.081 & -15.115 & 0.000 & -1.376 & -1.060 \\
Q('to North Elizabeth')               & -0.3989 & 0.121 & -3.291 & 0.001 & -0.636 & -0.161 \\
Q('to Oradell')                       & -0.5414 & 0.120 & -4.520 & 0.000 & -0.776 & -0.307 \\
Q('to Passaic')                       & 1.1956 & 0.187 & 6.384 & 0.000 & 0.829 & 1.563 \\
Q('to Paterson')                      & 1.0026 & 0.174 & 5.775 & 0.000 & 0.662 & 1.343 \\
Q('to Peapack')                       & 0.6545 & 0.127 & 5.135 & 0.000 & 0.405 & 0.904 \\
Q('to Perth Amboy')                   & 0.3501 & 0.124 & 2.822 & 0.005 & 0.107 & 0.593 \\
Q('to Philadelphia')                  & -1.0324 & 0.196 & -5.278 & 0.000 & -1.416 & -0.649 \\
Q('to Plainfield')                    & 1.3396 & 0.150 & 8.906 & 0.000 & 1.045 & 1.634 \\
Q('to Point Pleasant Beach')          & -0.9051 & 0.157 & -5.774 & 0.000 & -1.212 & -0.598 \\
Q('to Port Jervis')                   & -1.2126 & 0.123 & -9.858 & 0.000 & -1.454 & -0.972 \\
Q('to Princeton')                     & -1.5904 & 0.455 & -3.494 & 0.000 & -2.482 & -0.698 \\
Q('to Princeton Junction')            & -1.2398 & 0.082 & -15.091 & 0.000 & -1.401 & -1.079 \\
Q('to Rahway')                        & -1.3254 & 0.086 & -15.356 & 0.000 & -1.495 & -1.156 \\
Q('to Raritan')                       & 0.7571 & 0.121 & 6.265 & 0.000 & 0.520 & 0.994 \\
Q('to Red Bank')                      & -0.6223 & 0.140 & -4.438 & 0.000 & -0.897 & -0.347 \\
Q('to Roselle Park')                  & 0.5665 & 0.135 & 4.192 & 0.000 & 0.302 & 0.831 \\
Q('to Secaucus Upper Level')          & -0.2063 & 0.075 & -2.740 & 0.006 & -0.354 & -0.059 \\
Q('to Short Hills')                   & 0.2117 & 0.083 & 2.548 & 0.011 & 0.049 & 0.375 \\
Q('to Somerville')                    & 1.3678 & 0.144 & 9.488 & 0.000 & 1.085 & 1.650 \\
Q('to Spring Valley')                 & -0.9541 & 0.111 & -8.614 & 0.000 & -1.171 & -0.737 \\
Q('to Suffern')                       & -0.9067 & 0.072 & -12.625 & 0.000 & -1.047 & -0.766 \\
Q('to Summit')                        & -0.6213 & 0.058 & -10.651 & 0.000 & -0.736 & -0.507 \\
Q('to Towaco')                       & 0.7510 & 0.267 & 2.817 & 0.005 & 0.229 & 1.274 \\
Q('to Trenton')                      & -1.1508 & 0.080 & -14.313 & 0.000 & -1.308 & -0.993 \\
Q('to Union')                        & 0.4963 & 0.129 & 3.854 & 0.000 & 0.244 & 0.749 \\
Q('to Watchung Avenue')              & 0.2954 & 0.128 & 2.311 & 0.021 & 0.045 & 0.546 \\
Q('to Westfield')                    & 1.7199 & 0.167 & 10.298 & 0.000 & 1.393 & 2.047 \\
Q('to White House')                  & 1.0001 & 0.227 & 4.405 & 0.000 & 0.555 & 1.445 \\
Q('to Wood Ridge')                   & 0.6406 & 0.185 & 3.464 & 0.001 & 0.278 & 1.003 \\
Q('to Woodbridge')                   & 0.3486 & 0.123 & 2.833 & 0.005 & 0.107 & 0.590 \\
Q('stop sequence 10')                & 1.3426 & 0.045 & 29.980 & 0.000 & 1.255 & 1.430 \\
Q('stop sequence 11')                & 1.2811 & 0.045 & 28.194 & 0.000 & 1.192 & 1.370 \\
Q('stop sequence 12')                & 1.3287 & 0.046 & 28.819 & 0.000 & 1.238 & 1.419 \\
Q('stop sequence 13')                & 1.1540 & 0.046 & 25.198 & 0.000 & 1.064 & 1.244 \\
Q('stop sequence 14')                & 1.0100 & 0.048 & 21.079 & 0.000 & 0.916 & 1.104 \\
Q('stop sequence 15')                & 1.1321 & 0.053 & 21.465 & 0.000 & 1.029 & 1.235 \\
Q('stop sequence 16')                & 1.1766 & 0.053 & 22.058 & 0.000 & 1.072 & 1.281 \\
Q('stop sequence 17')                & 1.1548 & 0.057 & 20.422 & 0.000 & 1.044 & 1.266 \\
Q('stop sequence 18')                & 0.9618 & 0.059 & 16.262 & 0.000 & 0.846 & 1.078 \\
Q('stop sequence 19')                & 0.9749 & 0.081 & 12.036 & 0.000 & 0.816 & 1.134 \\
\end{tabular}
\caption{Resumo dos Resultados de Coeficientes}
\label{table:results}
\end{table}


\begin{table}[h]
\centering
\begin{tabular}{l c c c c c c}

\textbf{Variable} & \textbf{Coef} & \textbf{Std Err} & \textbf{z} & \textbf{P>|z|} & \textbf{[0.025} & \textbf{0.975]} \\


Q('stop sequence 2')                 & 1.4290 & 0.048 & 29.963 & 0.000 & 1.335 & 1.522 \\
Q('stop sequence 20')                & 1.0854 & 0.093 & 11.703 & 0.000 & 0.904 & 1.267 \\
Q('stop sequence 21')                & 1.4541 & 0.115 & 12.654 & 0.000 & 1.229 & 1.679 \\
Q('stop sequence 22')                & 1.5935 & 0.138 & 11.588 & 0.000 & 1.324 & 1.863 \\
Q('stop sequence 23')                & 1.2564 & 0.150 & 8.399 & 0.000 & 0.963 & 1.550 \\
Q('stop sequence 24')                & 1.3397 & 0.129 & 10.357 & 0.000 & 1.086 & 1.593 \\
Q('stop sequence 25')                & 0.7398 & 0.217 & 3.403 & 0.001 & 0.314 & 1.166 \\
Q('stop sequence 26')                & 3.0421 & 0.317 & 9.600 & 0.000 & 2.421 & 3.663 \\
Q('stop sequence 3')                 & 1.8991 & 0.048 & 39.438 & 0.000 & 1.805 & 1.993 \\
Q('stop sequence 4')                 & 1.6089 & 0.047 & 34.055 & 0.000 & 1.516 & 1.701 \\
Q('stop sequence 5')                 & 1.4600 & 0.047 & 30.961 & 0.000 & 1.368 & 1.552 \\
Q('stop sequence 6')                 & 1.4096 & 0.046 & 30.719 & 0.000 & 1.320 & 1.500 \\
Q('stop sequence 7')                 & 1.5376 & 0.048 & 32.231 & 0.000 & 1.444 & 1.631 \\
Q('stop sequence 8')                 & 1.4947 & 0.046 & 32.180 & 0.000 & 1.404 & 1.586 \\
Q('stop sequence 9')                 & 1.4184 & 0.048 & 29.710 & 0.000 & 1.325 & 1.512 \\
Q('Centrality')                      & 1.6008 & 0.146 & 10.959 & 0.000 & 1.315 & 1.887 \\

\end{tabular}
\caption{Resumo dos Resultados de Coeficientes}
\label{table:results}
\end{table}





\end{document}