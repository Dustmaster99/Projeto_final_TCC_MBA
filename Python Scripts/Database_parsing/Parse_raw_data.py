# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 21:39:15 2024




@author: eosjo
"""




from PIL import Image
import pyodbc
import pandas as pd
import os

import matplotlib.pyplot as plt
import seaborn as sns

import scipy.stats as stats

import numpy as np

from matplotlib.gridspec import GridSpec # plotagem de gráficos separados
from scipy.stats import gaussian_kde # inserção de KDEs em gráficos
import statsmodels.api as sm # estimação de modelos
from statsmodels.stats.anova import anova_lm
from statstests.process import stepwise

from statstests.tests import shapiro_francia
from scipy.stats import boxcox
import statsmodels.formula.api as smf # estimação do modelo logístico binário


def classificar_hora(hora): 
    if hora < 4:        
        return 'Antes_4'    
    elif hora < 8:       
        return 'Entre_4_e_8'   
    elif hora < 12:       
        return 'Entre_8_e_12' 
    elif hora < 16:       
        return 'Entre_12_e_16' 
    elif hora < 20:       
        return 'Entre_16_e_20' 
    elif hora < 24:        
        return 'Entre_20_e_24' 
    else:        
        return 'erro'
    
from sklearn.metrics import confusion_matrix, accuracy_score,\
    ConfusionMatrixDisplay, recall_score
    
def matriz_confusao(predicts, observado, cutoff):
    
    values = predicts.values
    
    predicao_binaria = []
        
    for item in values:
        if item < cutoff:
            predicao_binaria.append(0)
        else:
            predicao_binaria.append(1)
           
    #cm = confusion_matrix(predicao_binaria, observado)
    #disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    #disp.plot()
    #plt.xlabel('True')
    #plt.ylabel('Classified')
    #plt.gca().invert_xaxis()
    #plt.gca().invert_yaxis()
    #plt.show()
        
    sensitividade = recall_score(observado, predicao_binaria, pos_label=1)
    especificidade = recall_score(observado, predicao_binaria, pos_label=0)
    acuracia = accuracy_score(observado, predicao_binaria)

    #Visualizando os principais indicadores desta matriz de confusão
    indicadores = pd.DataFrame({'Sensitividade':[sensitividade],
                                'Especificidade':[especificidade],
                                'Acurácia':[acuracia]})
    return indicadores   
    


def return_acuracia(predicts, observado, cutoff):
    
    values = predicts.values
    
    predicao_binaria = []
        
    for item in values:
        if item < cutoff:
            predicao_binaria.append(0)
        else:
            predicao_binaria.append(1)
           
    sensitividade = recall_score(observado, predicao_binaria, pos_label=1)
    especificidade = recall_score(observado, predicao_binaria, pos_label=0)
    acuracia = accuracy_score(observado, predicao_binaria)

    #Visualizando os principais indicadores desta matriz de confusão
    indicadores = pd.DataFrame({'Sensitividade':[sensitividade],
                                'Especificidade':[especificidade],
                                'Acurácia':[acuracia]})
   
    return indicadores
    

def espec_sens(observado,predicts):
    
    # Adicionar objeto com os valores dos predicts
    values = predicts.values
    
    # Range dos cutoffs a serem analisados em steps de 0.01
    cutoffs = np.arange(0,1.01,0.01)
    
    # Listas que receberão os resultados de especificidade e sensitividade
    lista_sensitividade = []
    lista_especificidade = []
    lista_acuracia = []
    
    
    for cutoff in cutoffs:
        
        predicao_binaria = []
        
        # Definindo resultado binário de acordo com o predict
        for item in values:
            if item >= cutoff:
                predicao_binaria.append(1)
            else:
                predicao_binaria.append(0)
                
        # Cálculo da sensitividade e especificidade no cutoff
        sensitividade = recall_score(observado, predicao_binaria, pos_label=1)
        especificidadee = recall_score(observado, predicao_binaria, pos_label=0)
        acuracia = accuracy_score(observado, predicao_binaria)
        
        # Adicionar valores nas listas
        lista_sensitividade.append(sensitividade)
        lista_especificidade.append(especificidadee)
        lista_acuracia.append(  acuracia ) 
        
    # Criar dataframe com os resultados nos seus respectivos cutoffs
    resultado = pd.DataFrame({'cutoffs':cutoffs,'sensitividade':lista_sensitividade,'especificidade':lista_especificidade, 'acuracia': lista_acuracia})
    return resultado

    
new_dir = r"C:\Users\eosjo\OneDrive\Área de Trabalho\Filesystem\MBA data science\ProjetoFinalTCC"
os.chdir(new_dir)


SERVER_NAME = 'ZEC'
DATABASE_NAME = 'NJTransit'
USERNAME = 'sa'
PASSWORD = ''
connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER_NAME};DATABASE={DATABASE_NAME};UID={USERNAME};PWD={PASSWORD}'

connection = pyodbc.connect(connectionString)


#Import into databases all Lines Table info

# Database for march of 2018

sql_query_2018_03 = """
      SELECT
       [date]
      ,[train_id]
      ,[stop_sequence]
      ,[from]
      ,[from_id]
      ,[to]
      ,[to_id]
      ,[scheduled_time]
      ,[actual_time]
      ,[delay_minutes]
      ,[status]
      ,[line]
      ,[type]
  FROM [NJTransit].[dbo].[2018_03]
    """

df_2018_03 = pd.read_sql(
    sql_query_2018_03, connection)

# Database for april of 2018
sql_query_2018_04 = """
      SELECT
       [date]
      ,[train_id]
      ,[stop_sequence]
      ,[from]
      ,[from_id]
      ,[to]
      ,[to_id]
      ,[scheduled_time]
      ,[actual_time]
      ,[delay_minutes]
      ,[status]
      ,[line]
      ,[type]
  FROM [NJTransit].[dbo].[2018_04]
    """

df_2018_04 = pd.read_sql(
    sql_query_2018_04, connection)

# Database for may of 2018
sql_query_2018_05 = """
      SELECT
       [date]
      ,[train_id]
      ,[stop_sequence]
      ,[from]
      ,[from_id]
      ,[to]
      ,[to_id]
      ,[scheduled_time]
      ,[actual_time]
      ,[delay_minutes]
      ,[status]
      ,[line]
      ,[type]
  FROM [NJTransit].[dbo].[2018_05]
    """

df_2018_05 = pd.read_sql(
    sql_query_2018_05, connection)


# Database for june of 2018
sql_query_2018_06 = """
      SELECT
       [date]
      ,[train_id]
      ,[stop_sequence]
      ,[from]
      ,[from_id]
      ,[to]
      ,[to_id]
      ,[scheduled_time]
      ,[actual_time]
      ,[delay_minutes]
      ,[status]
      ,[line]
      ,[type]
  FROM [NJTransit].[dbo].[2018_06]
    """

df_2018_06 = pd.read_sql(
    sql_query_2018_06, connection)

# Database for july of 2018	
sql_query_2018_07 = """
      SELECT
       [date]
      ,[train_id]
      ,[stop_sequence]
      ,[from]
      ,[from_id]
      ,[to]
      ,[to_id]
      ,[scheduled_time]
      ,[actual_time]
      ,[delay_minutes]
      ,[status]
      ,[line]
      ,[type]
  FROM [NJTransit].[dbo].[2018_07]
    """

df_2018_07 = pd.read_sql(
    sql_query_2018_07, connection)

# Database for august of 2018	
sql_query_2018_08 = """
      SELECT
       [date]
      ,[train_id]
      ,[stop_sequence]
      ,[from]
      ,[from_id]
      ,[to]
      ,[to_id]
      ,[scheduled_time]
      ,[actual_time]
      ,[delay_minutes]
      ,[status]
      ,[line]
      ,[type]
  FROM [NJTransit].[dbo].[2018_08]
    """

df_2018_08 = pd.read_sql(
    sql_query_2018_08, connection)

# Database for september of 2018
sql_query_2018_09 = """
      SELECT
       [date]
      ,[train_id]
      ,[stop_sequence]
      ,[from]
      ,[from_id]
      ,[to]
      ,[to_id]
      ,[scheduled_time]
      ,[actual_time]
      ,[delay_minutes]
      ,[status]
      ,[line]
      ,[type]
  FROM [NJTransit].[dbo].[2018_09]
    """

df_2018_09 = pd.read_sql(
    sql_query_2018_09, connection)
	

# Database for october 2018			
sql_query_2018_10 = """
      SELECT
       [date]
      ,[train_id]
      ,[stop_sequence]
      ,[from]
      ,[from_id]
      ,[to]
      ,[to_id]
      ,[scheduled_time]
      ,[actual_time]
      ,[delay_minutes]
      ,[status]
      ,[line]
      ,[type]
  FROM [NJTransit].[dbo].[2018_10]
    """

df_2018_10 = pd.read_sql(
    sql_query_2018_10, connection)

# Database for november 2018	
sql_query_2018_11 = """
      SELECT
       [date]
      ,[train_id]
      ,[stop_sequence]
      ,[from]
      ,[from_id]
      ,[to]
      ,[to_id]
      ,[scheduled_time]
      ,[actual_time]
      ,[delay_minutes]
      ,[status]
      ,[line]
      ,[type]
  FROM [NJTransit].[dbo].[2018_11]
    """

df_2018_11 = pd.read_sql(
    sql_query_2018_11, connection)

# Database for december 2018	
sql_query_2018_12 = """
      SELECT
       [date]
      ,[train_id]
      ,[stop_sequence]
      ,[from]
      ,[from_id]
      ,[to]
      ,[to_id]
      ,[scheduled_time]
      ,[delay_minutes]
      ,[status]
      ,[line]
      ,[type]
  FROM [NJTransit].[dbo].[2018_12]
    """

df_2018_12 = pd.read_sql(
    sql_query_2018_12, connection)		

# Database for january 2018	
sql_query_2019_01 = """
      SELECT
       [date]
      ,[train_id]
      ,[stop_sequence]
      ,[from]
      ,[from_id]
      ,[to]
      ,[to_id]
      ,[scheduled_time]
      ,[actual_time]
      ,[delay_minutes]
      ,[status]
      ,[line]
      ,[type]
  FROM [NJTransit].[dbo].[2019_01]
    """

df_2019_01 = pd.read_sql(
    sql_query_2019_01, connection)

# Database for february 2018		
sql_query_2019_02 = """
      SELECT
       [date]
      ,[train_id]
      ,[stop_sequence]
      ,[from]
      ,[from_id]
      ,[to]
      ,[to_id]
      ,[scheduled_time]
      ,[actual_time]
      ,[delay_minutes]
      ,[status]
      ,[line]
      ,[type]
  FROM [NJTransit].[dbo].[2019_02]
    """

df_2019_02 = pd.read_sql(
    sql_query_2019_02, connection)
	

# database for centrality station parameters
sql_query_centrality = """
    SELECT [Station]
      ,[Centrality]
  FROM [NJTransit].[dbo].[centrality]
    """

df_centrality = pd.read_sql(
    sql_query_centrality, connection)

# database for clossenes station parameters
sql_query_closseness = """

    SELECT [Station]
      ,[Closseness]
      FROM [NJTransit].[dbo].[closseness]
    """

df_closseness = pd.read_sql(
    sql_query_closseness, connection)

# database for clustering coeficient parameters
sql_query_clustering_coef = """
    SELECT  [Station]
      ,[Clustering]
  FROM [NJTransit].[dbo].[clustering_coef]
"""

df_clustering_coef = pd.read_sql(
    sql_query_clustering_coef, connection)


# database for station date parameters
sql_query_station_date = """
   SELECT [Line]
         ,[Station]
         ,[Date]
     FROM [NJTransit].[dbo].[datas_inalguracao_estacoes]
"""

df_station_date = pd.read_sql(
    sql_query_station_date, connection)

# database for degree parameters
sql_query_degree = """
  
SELECT [Station]
      ,[Degree]
  FROM [NJTransit].[dbo].[degree]

"""

df_degree = pd.read_sql(
    sql_query_degree, connection)


# database for latitude/longitude parameters
sql_query_lat_long = """
  
SELECT  [LineName]
      ,[StationName]
      ,[Latitude]
      ,[Longitude]
  FROM [NJTransit].[dbo].[Lat_long]

"""

df_lat_long = pd.read_sql(
    sql_query_lat_long, connection)


# database for cluster parameters
sql_query_cluster = """
  
SELECT  [to]
      ,[cluster_Hierarch]
      ,[cluster_kmeans]
      ,[cluster_DBscan]
  FROM [NJTransit].[dbo].[clustering]

"""

df_cluster = pd.read_sql(
    sql_query_cluster, connection)



#df_Yearly  = pd.concat([df_2018_03, df_2018_04])

df_Yearly = pd.concat([df_2018_03, df_2018_04, df_2018_05, df_2018_06, df_2018_07, df_2018_08, df_2018_09, df_2018_10, df_2018_11, df_2018_12,df_2019_01,df_2019_02], axis=0)


# Data processing before join:     
df_lat_long = df_lat_long.drop(columns=['LineName'])
df_station_date = df_station_date.drop(columns=['Line'])
df_lat_long = df_lat_long.drop_duplicates()
df_station_date = df_station_date.drop_duplicates(subset=['Station'])
#drop specific lines that are not contained in for the list of stations :  
df_station_date = df_station_date.loc[df_station_date['Station'].isin(df_Yearly['to'].unique() )]

#concatenate with other databases to get info into Yearly - Database

df_Yearly = df_Yearly.join(df_centrality.set_index('Station'), on='to')
df_Yearly = df_Yearly.join(df_closseness.set_index('Station'), on='to')
df_Yearly = df_Yearly.join(df_cluster.set_index('to'), on='to')
df_Yearly = df_Yearly.join(df_clustering_coef.set_index('Station'), on='to')
df_Yearly = df_Yearly.join(df_degree.set_index('Station'), on='to')
df_Yearly = df_Yearly.join(df_lat_long.set_index('StationName'), on='to')
df_Yearly = df_Yearly.join(df_station_date.set_index('Station'), on='to')




#Data processing for Yearly database

df_Yearly['line'] = np.where(df_Yearly['line'] == 'Atl. City Line', 'Atl_City_Line', df_Yearly['line'])
df_Yearly['line'] = np.where(df_Yearly['line'] == 'Bergen Co. Line ', 'Bergen_Co_Line', df_Yearly['line'])
df_Yearly['line'] = np.where(df_Yearly['line'] == 'Gladstone Branch', 'Gladstone_Branch', df_Yearly['line'])
df_Yearly['line'] = np.where(df_Yearly['line'] == 'Main Line', 'Main_Line', df_Yearly['line'])
df_Yearly['line'] = np.where(df_Yearly['line'] == 'Montclair-Boonton', 'Montclair_Boonton', df_Yearly['line'])
df_Yearly['line'] = np.where(df_Yearly['line'] == 'Morristown Line', 'Morristown_Line', df_Yearly['line'])
df_Yearly['line'] = np.where(df_Yearly['line'] == 'No Jersey Coast', 'No_Jersey_Coast', df_Yearly['line'])
df_Yearly['line'] = np.where(df_Yearly['line'] == 'Northeast Corrdr', 'Northeast_Corrdr', df_Yearly['line'])
df_Yearly['line'] = np.where(df_Yearly['line'] == 'Pascack Valley', 'Pascack_Valley', df_Yearly['line'])
df_Yearly['line'] = np.where(df_Yearly['line'] == 'Princeton Shuttle', 'Princeton_Shuttle', df_Yearly['line'])
df_Yearly['line'] = np.where(df_Yearly['line'] == 'Raritan Valley', 'Raritan_Valley', df_Yearly['line'])


# Cast to datatime
df_Yearly['actual_time'] = pd.to_datetime(df_Yearly['actual_time'])
df_Yearly['actual_time_hours'] =df_Yearly['actual_time'].dt.hour
df_Yearly['Month'] =df_Yearly['actual_time'].dt.month

#df_Yearly['Data_Pattern'] = np.where(((df_Yearly['actual_time_hours'] >=7) & (df_Yearly['actual_time_hours'] <= 9)) | ((df_Yearly['actual_time_hours'] >=17) & (df_Yearly['actual_time_hours'] <= 18)), 'Horario de Pico', 'Fora do horario de pico')

df_Yearly['Data_Pattern'] = df_Yearly['actual_time_hours'].apply(classificar_hora)

#df_Yearly['delay_minutes_rounded'] = df_Yearly['delay_minutes'].round()

df_Yearly['delay_minutes_rounded'] = np.where(df_Yearly['delay_minutes'] >=30, 30, df_Yearly['delay_minutes'])
df_Yearly['line_encoded'] = pd.factorize(df_Yearly['line'])[0]

# Type cast for columns: 
df_Yearly['line'] = df_Yearly['line'].astype('category')
df_Yearly['line_encoded']= df_Yearly['line_encoded'].astype('category')
df_Yearly['Data_Pattern'] = df_Yearly['Data_Pattern'].astype('category')
df_Yearly['Month'] = df_Yearly['Month'].astype(str)
df_Yearly['Month'] = df_Yearly['Month'].astype('category')

df_Yearly['Month'] = df_Yearly['Month'].apply(lambda x: x.replace('.0', ''))
df_Yearly['to'] = df_Yearly['to'].apply(lambda x: x.replace(' ', '_'))
df_Yearly['stop_sequence'] = df_Yearly['stop_sequence'].apply(lambda x: x.replace('.0', ''))

Mean_delay = df_Yearly['delay_minutes'].mean()

#df_Yearly_sample = df_Yearly.sample(frac=0.1).reset_index(drop=True)
#df_Yearly = df_Yearly_sample

#df_Yearly = df_Yearly.dropna()


# In[1.0]: plot Contagem


plt.figure(figsize=(15,10))
sns.histplot(data=df_Yearly['delay_minutes_rounded'], kde=True,
             bins=100, color='deepskyblue')
plt.xlabel('delay_minutes_rounded', fontsize=20)
plt.ylabel('Contagem', fontsize=20)
plt.tick_params(axis='y', labelsize=17)
plt.tick_params(axis='x', labelsize=17)
plt.show()



#----------Análise assumindo um modelo de regressão linear para cada variável a ser analisada -----------#

Line_Statistics = df_Yearly.groupby('line')['delay_minutes'].describe()

# -- Dumyzação da variável "Line" ---- #
df_dummies_Line = pd.get_dummies(df_Yearly, columns=['line'],
                                      dtype=int,
                                      drop_first=True)

df_dummies_Line =(df_dummies_Line.drop(columns=['date','train_id','stop_sequence','from','from_id','to','to_id','scheduled_time','actual_time','status','type','Data_Pattern','Centrality','Closseness','cluster_Hierarch', 'cluster_kmeans','cluster_DBscan', 'Clustering', 'Degree', 'Latitude','Longitude','Date','Month','line_encoded','delay_minutes_rounded','actual_time_hours']))

df_dummies_Line_columns_list = list(df_dummies_Line.drop(columns=['delay_minutes']).columns)


formula_dummies_modelo_Line = ' + '.join(df_dummies_Line_columns_list)
formula_dummies_modelo_Line = "delay_minutes ~ " + formula_dummies_modelo_Line
print("Fórmula utilizada: ",formula_dummies_modelo_Line)


modelo_Linear_Line = sm.OLS.from_formula(formula_dummies_modelo_Line, df_dummies_Line).fit()
print(modelo_Linear_Line.summary(alpha=0.05))


# Parâmetros do 'modelo_corrupcao_dummies'
modelo_Linear_Line.summary()



# R - Squared :O R-quadrado (R²), ou coeficiente de determinação, é uma medida estatística que indica quão bem um modelo de regressão se ajusta aos dados, ou seja, a percentagem da variação na variável dependente que é explicada pela variável independente

path_img = r"C:\Users\eosjo\OneDrive\Área de Trabalho\Filesystem\MBA data science\ProjetoFinalTCC\Relatorios\Imagens"
os.chdir(path_img)
img = Image.open("R-squared.jpg")
img.show()

r_squared_modelo_Linear_Line = modelo_Linear_Line.rsquared

#Teste F -> # Análise de variância para sabe se existe modelo ( P_value <0.05 a 95% de confiança )

F_modelo_Linear_Line = modelo_Linear_Line.fvalue

#anova_lm(modelo_Linear_Line).F

# Definição de p-value associado ao F_calculado: 
    
from scipy.stats import f 

pvalue_modelo_Linear_Line = 1 - f.cdf(F_modelo_Linear_Line,modelo_Linear_Line.df_model,modelo_Linear_Line.df_resid)

print(pvalue_modelo_Linear_Line)
    
## Podemos ver que o p-value é bem pequeno, então é possível dizer que existe modelo usando essas variáveis, porém o r-squared é muito baixo, indicando que essas variáveis não explicam o suficiente do modelo.

# Podemos ver que a significancia de pelo menos um dos parâmetros é diferente de 0, e de fato podemos ver que varios deles possuem pvalue > 0.05 e são estatísticamente significantes:
    
path_img = r"C:\Users\eosjo\OneDrive\Área de Trabalho\Filesystem\MBA data science\ProjetoFinalTCC\Relatorios\Imagens"
os.chdir(path_img)
img = Image.open("pvalue-line.png")
img.show()    

# Teste da estatística T -> #Para análise de relevância de variáveis indivídualmente 

T_modelo_Linear_Line = modelo_Linear_Line.tvalues

p_value_indiv__modelo_Linear_Line = modelo_Linear_Line.pvalues



#-------------------------Teste de aderência a normalidade Shapiro - francia -------------------------------------------------------------#


# Teste de Shapiro-Francia: interpretação
teste_sf = shapiro_francia(modelo_Linear_Line.resid) #criação do objeto 'teste_sf'
teste_sf = teste_sf.items() #retorna o grupo de pares de valores-chave no dicionário
method, statistics_W, statistics_z, p = teste_sf #definição dos elementos da lista (tupla)
print('Statistics W=%.5f, p-value=%.6f' % (statistics_W[1], p[1]))
alpha = 0.05 #nível de significância
if p[1] > alpha:
	print('Não se rejeita H0 - Distribuição aderente à normalidade')
else:
	print('Rejeita-se H0 - Distribuição não aderente à normalidade')



#------------------------------------------------------------------------------------------#
 
    
# Essa variável não parece apresentar uma relação linear com o output

df_Yearly['Month'] = df_Yearly['Month'].apply(lambda x: x.replace('.0', ''))


Month_Statistics = df_Yearly.groupby('Month')['delay_minutes'].describe()
# -- Dumyzação da variável "Month" ---- #
df_dummies_Month = pd.get_dummies(df_Yearly, columns=['Month'],
                                      dtype=int,
                                      drop_first=True)

df_dummies_Month  =(df_dummies_Month .drop(columns=['date','train_id','stop_sequence','from','from_id','to','to_id','scheduled_time','actual_time','status','type','Data_Pattern','Centrality','Closseness','cluster_Hierarch', 'cluster_kmeans','cluster_DBscan', 'Clustering', 'Degree', 'Latitude','Longitude','Date','line','line_encoded','delay_minutes_rounded','actual_time_hours']))

df_dummies_Month_columns_list = list(df_dummies_Month.drop(columns=['delay_minutes']).columns)


formula_dummies_modelo_Month = ' + '.join(df_dummies_Month_columns_list)
formula_dummies_modelo_Month = "delay_minutes ~ " + formula_dummies_modelo_Month
print("Fórmula utilizada: ",formula_dummies_modelo_Month)


modelo_Linear_Month = sm.OLS.from_formula(formula_dummies_modelo_Month, df_dummies_Month).fit()


# Parâmetros do 'modelo_corrupcao_dummies'
print(modelo_Linear_Month.summary(alpha=0.05))


r_squared_modelo_Linear_Month = modelo_Linear_Month.rsquared

#Teste F -> # Análise de variância para sabe se existe modelo ( P_value <0.05 a 95% de confiança )

F_modelo_Linear_Month = modelo_Linear_Month.fvalue

#anova_lm(modelo_Linear_Line).F

# Definição de p-value associado ao F_calculado: 
    
from scipy.stats import f 

pvalue_modelo_Linear_Month = 1 - f.cdf(F_modelo_Linear_Month,modelo_Linear_Month.df_model,modelo_Linear_Month.df_resid)

print(pvalue_modelo_Linear_Month)
    
## Podemos ver que o p-value é bem pequeno, então é possível dizer que existe modelo usando essas variáveis, porém o r-squared é muito baixo, indicando que essas variáveis não explicam o suficiente do modelo.

# Podemos ver que a significancia de pelo menos um dos parâmetros é diferente de 0, e de fato podemos ver que varios deles possuem pvalue > 0.05 e são estatísticamente significantes:
    
path_img = r"C:\Users\eosjo\OneDrive\Área de Trabalho\Filesystem\MBA data science\ProjetoFinalTCC\Relatorios\Imagens"
os.chdir(path_img)
img = Image.open("pvalue-month.png")
img.show()    

# Teste da estatística T -> #Para análise de relevância de variáveis indivídualmente 

T_modelo_Linear_Month = modelo_Linear_Month.tvalues

p_value_indiv__modelo_Linear_Month = modelo_Linear_Month.pvalues



#--------------------------------------------------------------------------------------------------------------
# Teste de Shapiro-Francia: interpretação
teste_sf = shapiro_francia(modelo_Linear_Month.resid) #criação do objeto 'teste_sf'
teste_sf = teste_sf.items() #retorna o grupo de pares de valores-chave no dicionário
method, statistics_W, statistics_z, p = teste_sf #definição dos elementos da lista (tupla)
print('Statistics W=%.5f, p-value=%.6f' % (statistics_W[1], p[1]))
alpha = 0.05 #nível de significância
if p[1] > alpha:
	print('Não se rejeita H0 - Distribuição aderente à normalidade')
else:
	print('Rejeita-se H0 - Distribuição não aderente à normalidade')

#--------------------------------------------------------------------------------------------------------------



Pattern_Statistics = df_Yearly.groupby('Data_Pattern')['delay_minutes'].describe()
# -- Dumyzação da variável "Data Pattern" ---- #
df_dummies_Pattern = pd.get_dummies(df_Yearly, columns=['Data_Pattern'],
                                      dtype=int,
                                      drop_first=True)

df_dummies_Pattern  =(df_dummies_Pattern.drop(columns=['date','train_id','stop_sequence','from','from_id','to','to_id','scheduled_time','actual_time','status','type','Month','Centrality','Closseness','cluster_Hierarch', 'cluster_kmeans','cluster_DBscan', 'Clustering', 'Degree', 'Latitude','Longitude','Date','line','line_encoded','delay_minutes_rounded','actual_time_hours']))

df_dummies_Pattern_columns_list= list(df_dummies_Pattern.drop(columns=['delay_minutes']).columns)


formula_dummies_modelo_Pattern = ' + '.join(df_dummies_Pattern_columns_list)
formula_dummies_modelo_Pattern = "delay_minutes ~ " + formula_dummies_modelo_Pattern
print("Fórmula utilizada: ",formula_dummies_modelo_Pattern)


modelo_Linear_Pattern= sm.OLS.from_formula(formula_dummies_modelo_Pattern, df_dummies_Pattern).fit()


# Parâmetros do 'modelo_corrupcao_dummies'
print(modelo_Linear_Pattern.summary(alpha=0.05))


r_squared_modelo_Linear_Pattern = modelo_Linear_Pattern.rsquared

#Teste F -> # Análise de variância para sabe se existe modelo ( P_value <0.05 a 95% de confiança )

F_modelo_Linear_Pattern = modelo_Linear_Pattern.fvalue

#anova_lm(modelo_Linear_Line).F

# Definição de p-value associado ao F_calculado: 
    
from scipy.stats import f 

pvalue_modelo_Linear_Pattern = 1 - f.cdf(F_modelo_Linear_Pattern,modelo_Linear_Pattern.df_model,modelo_Linear_Pattern.df_resid)

print(pvalue_modelo_Linear_Pattern)
    
## Podemos ver que o p-value é bem pequeno, então é possível dizer que existe modelo usando essas variáveis, porém o r-squared é muito baixo, indicando que essas variáveis não explicam o suficiente do modelo.

# Podemos ver que a significancia de pelo menos um dos parâmetros é diferente de 0, e de fato podemos ver que varios deles possuem pvalue > 0.05 e são estatísticamente significantes:
    
path_img = r"C:\Users\eosjo\OneDrive\Área de Trabalho\Filesystem\MBA data science\ProjetoFinalTCC\Relatorios\Imagens"
os.chdir(path_img)
img = Image.open("pvalue-pattern.png")
img.show()    

# Teste da estatística T -> #Para análise de relevância de variáveis indivídualmente 

# Teste da estatística T -> #Para análise de relevância de variáveis indivídualmente 

T_modelo_Linear_Pattern = modelo_Linear_Pattern.tvalues

p_value_indiv__modelo_Linear_Pattern = modelo_Linear_Pattern.pvalues



#--------------------------------------------------------------------------------------------------------------
# Teste de Shapiro-Francia: interpretação
teste_sf = shapiro_francia(modelo_Linear_Pattern.resid) #criação do objeto 'teste_sf'
teste_sf = teste_sf.items() #retorna o grupo de pares de valores-chave no dicionário
method, statistics_W, statistics_z, p = teste_sf #definição dos elementos da lista (tupla)
print('Statistics W=%.5f, p-value=%.6f' % (statistics_W[1], p[1]))
alpha = 0.05 #nível de significância
if p[1] > alpha:
	print('Não se rejeita H0 - Distribuição aderente à normalidade')
else:
	print('Rejeita-se H0 - Distribuição não aderente à normalidade')

#--------------------------------------------------------------------------------------------------------------


Station_Statistics = df_Yearly.groupby('to')['delay_minutes'].describe()
# -- Dumyzação da variável "Station" ---- #

df_Yearly_provisory = df_Yearly
df_Yearly_provisory['to'] = df_Yearly_provisory['to'].apply(lambda x: x.replace(' ', '_'))
df_Yearly_provisory['to'] = df_Yearly_provisory['to'].apply(lambda x: x.replace('-', '_'))

df_dummies_Station = pd.get_dummies(df_Yearly_provisory, columns=['to'],
                                      dtype=int,
                                      drop_first=True)

df_dummies_Station  =(df_dummies_Station.drop(columns=['date','train_id','stop_sequence','from','from_id','Data_Pattern','to_id','scheduled_time','actual_time','status','type','Month','Centrality','Closseness','cluster_Hierarch', 'cluster_kmeans','cluster_DBscan', 'Clustering', 'Degree', 'Latitude','Longitude','Date','line','line_encoded','delay_minutes_rounded','actual_time_hours']))

df_dummies_Station_columns_list= list(df_dummies_Station.drop(columns=['delay_minutes']).columns)


formula_dummies_modelo_Station = ' + '.join(df_dummies_Station_columns_list)
formula_dummies_modelo_Station = "delay_minutes ~ " + formula_dummies_modelo_Station
print("Fórmula utilizada: ",formula_dummies_modelo_Station)


modelo_Linear_Station= sm.OLS.from_formula(formula_dummies_modelo_Station, df_dummies_Station).fit()


# Parâmetros do 'modelo_corrupcao_dummies'
print(modelo_Linear_Station.summary(alpha=0.05))


r_squared_modelo_Linear_Station = modelo_Linear_Station.rsquared

#Teste F -> # Análise de variância para sabe se existe modelo ( P_value <0.05 a 95% de confiança )

F_modelo_Linear_Station = modelo_Linear_Station.fvalue

#anova_lm(modelo_Linear_Line).F

# Definição de p-value associado ao F_calculado: 
    
from scipy.stats import f 

pvalue_modelo_Linear_Station = 1 - f.cdf(F_modelo_Linear_Station,modelo_Linear_Station.df_model,modelo_Linear_Station.df_resid)

print(pvalue_modelo_Linear_Station)
    
## Podemos ver que o p-value é bem pequeno, então é possível dizer que existe modelo usando essas variáveis, porém o r-squared é muito baixo, indicando que essas variáveis não explicam o suficiente do modelo.

# Podemos ver que a significancia de pelo menos um dos parâmetros é diferente de 0, e de fato podemos ver que varios deles possuem pvalue > 0.05 e são estatísticamente significantes:
    
path_img = r"C:\Users\eosjo\OneDrive\Área de Trabalho\Filesystem\MBA data science\ProjetoFinalTCC\Relatorios\Imagens"
os.chdir(path_img)
#img = Image.open("pvalue-Station.png")
img.show()    

# Teste da estatística T -> #Para análise de relevância de variáveis indivídualmente 

# Teste da estatística T -> #Para análise de relevância de variáveis indivídualmente 

T_modelo_Linear_Station = modelo_Linear_Station.tvalues

p_value_indiv__modelo_Linear_Station = modelo_Linear_Station.pvalues


#--------------------------------------------------------------------------------------------------------------
# Teste de Shapiro-Francia: interpretação
teste_sf = shapiro_francia( modelo_Linear_Station.resid) #criação do objeto 'teste_sf'
teste_sf = teste_sf.items() #retorna o grupo de pares de valores-chave no dicionário
method, statistics_W, statistics_z, p = teste_sf #definição dos elementos da lista (tupla)
print('Statistics W=%.5f, p-value=%.6f' % (statistics_W[1], p[1]))
alpha = 0.05 #nível de significância
if p[1] > alpha:
	print('Não se rejeita H0 - Distribuição aderente à normalidade')
else:
	print('Rejeita-se H0 - Distribuição não aderente à normalidade')

#--------------------------------------------------------------------------------------------------------------




Stop_seq_Statistics = df_Yearly.groupby('stop_sequence')['delay_minutes'].describe()
# -- Dumyzação da variável "Stop_Seq" ---- #


df_Yearly_provisory = df_Yearly
df_Yearly_provisory['stop_sequence'] = df_Yearly_provisory['stop_sequence'].apply(lambda x: x.replace('.0', ''))



df_dummies_Stop_Seq = pd.get_dummies(df_Yearly_provisory, columns=['stop_sequence'],
                                      dtype=int,
                                      drop_first=True)

df_dummies_Stop_Seq  =(df_dummies_Stop_Seq.drop(columns=['date','train_id','to','from','from_id','Data_Pattern','to_id','scheduled_time','actual_time','status','type','Month','Centrality','Closseness','cluster_Hierarch', 'cluster_kmeans','cluster_DBscan', 'Clustering', 'Degree', 'Latitude','Longitude','Date','line','line_encoded','delay_minutes_rounded','actual_time_hours']))

df_dummies_Stop_Seq_columns_list= list(df_dummies_Stop_Seq.drop(columns=['delay_minutes']).columns)


formula_dummies_modelo_Stop_Seq = ' + '.join(df_dummies_Stop_Seq_columns_list)
formula_dummies_modelo_Stop_Seq = "delay_minutes ~ " + formula_dummies_modelo_Stop_Seq
print("Fórmula utilizada: ",formula_dummies_modelo_Stop_Seq)


modelo_Linear_Stop_Seq= sm.OLS.from_formula(formula_dummies_modelo_Stop_Seq, df_dummies_Stop_Seq).fit()


# Parâmetros do 'modelo_corrupcao_dummies'
print(modelo_Linear_Stop_Seq.summary(alpha=0.05))


r_squared_modelo_Linear_Stop_Seq = modelo_Linear_Stop_Seq.rsquared

#Teste F -> # Análise de variância para sabe se existe modelo ( P_value <0.05 a 95% de confiança )

F_modelo_Linear_Stop_Seq = modelo_Linear_Stop_Seq.fvalue

#anova_lm(modelo_Linear_Line).F

# Definição de p-value associado ao F_calculado: 
    
from scipy.stats import f 

pvalue_modelo_Linear_Stop_Seq = 1 - f.cdf(F_modelo_Linear_Stop_Seq,modelo_Linear_Stop_Seq.df_model,modelo_Linear_Stop_Seq.df_resid)

print(pvalue_modelo_Linear_Stop_Seq)
    
## Podemos ver que o p-value é bem pequeno, então é possível dizer que existe modelo usando essas variáveis, porém o r-squared é muito baixo, indicando que essas variáveis não explicam o suficiente do modelo.

# Podemos ver que a significancia de pelo menos um dos parâmetros é diferente de 0, e de fato podemos ver que varios deles possuem pvalue > 0.05 e são estatísticamente significantes:
    
path_img = r"C:\Users\eosjo\OneDrive\Área de Trabalho\Filesystem\MBA data science\ProjetoFinalTCC\Relatorios\Imagens"
os.chdir(path_img)
img = Image.open("pvalue-Stop_Seq.png")
img.show()    

# Teste da estatística T -> #Para análise de relevância de variáveis indivídualmente 

# Teste da estatística T -> #Para análise de relevância de variáveis indivídualmente 

T_modelo_Linear_Stop_Seq = modelo_Linear_Stop_Seq.tvalues

p_value_indiv__modelo_Linear_Stop_Seq = modelo_Linear_Stop_Seq.pvalues


#--------------------------------------------------------------------------------------------------------------
# Teste de Shapiro-Francia: interpretação
teste_sf = shapiro_francia( modelo_Linear_Stop_Seq.resid) #criação do objeto 'teste_sf'
teste_sf = teste_sf.items() #retorna o grupo de pares de valores-chave no dicionário
method, statistics_W, statistics_z, p = teste_sf #definição dos elementos da lista (tupla)
print('Statistics W=%.5f, p-value=%.6f' % (statistics_W[1], p[1]))
alpha = 0.05 #nível de significância
if p[1] > alpha:
	print('Não se rejeita H0 - Distribuição aderente à normalidade')
else:
	print('Rejeita-se H0 - Distribuição não aderente à normalidade')

#--------------------------------------------------------------------------------------------------------------


Cluster_k_means_Statistics = df_Yearly.groupby('cluster_kmeans')['delay_minutes'].describe()
# -- Dumyzação da variável "Cluster_k_means" ---- #
df_dummies_Cluster_k_means = pd.get_dummies(df_Yearly, columns=['cluster_kmeans'],
                                      dtype=int,
                                      drop_first=True)

df_dummies_Cluster_k_means  =(df_dummies_Cluster_k_means.drop(columns=['date','train_id','to','from','from_id','Data_Pattern','to_id','scheduled_time','actual_time','status','type','Month','Centrality','Closseness','cluster_Hierarch', 'stop_sequence','cluster_DBscan', 'Clustering', 'Degree', 'Latitude','Longitude','Date','line','line_encoded','delay_minutes_rounded','actual_time_hours']))

df_dummies_Cluster_k_means_columns_list= list(df_dummies_Cluster_k_means.drop(columns=['delay_minutes']).columns)


formula_dummies_modelo_Cluster_k_means = ' + '.join(df_dummies_Cluster_k_means_columns_list)
formula_dummies_modelo_Cluster_k_means = "delay_minutes ~ " + formula_dummies_modelo_Cluster_k_means
print("Fórmula utilizada: ",formula_dummies_modelo_Cluster_k_means)


modelo_Linear_Cluster_k_means= sm.OLS.from_formula(formula_dummies_modelo_Cluster_k_means, df_dummies_Cluster_k_means).fit()


# Parâmetros do 'modelo_corrupcao_dummies'
print(modelo_Linear_Cluster_k_means.summary(alpha=0.05))


r_squared_modelo_Linear_Cluster_k_means = modelo_Linear_Cluster_k_means.rsquared

#Teste F -> # Análise de variância para sabe se existe modelo ( P_value <0.05 a 95% de confiança )

F_modelo_Linear_Cluster_k_means = modelo_Linear_Cluster_k_means.fvalue

#anova_lm(modelo_Linear_Line).F

# Definição de p-value associado ao F_calculado: 
    
from scipy.stats import f 

pvalue_modelo_Linear_Cluster_k_means = 1 - f.cdf(F_modelo_Linear_Cluster_k_means,modelo_Linear_Cluster_k_means.df_model,modelo_Linear_Cluster_k_means.df_resid)

print(pvalue_modelo_Linear_Cluster_k_means)
    
## Podemos ver que o p-value é bem pequeno, então é possível dizer que existe modelo usando essas variáveis, porém o r-squared é muito baixo, indicando que essas variáveis não explicam o suficiente do modelo.

# Podemos ver que a significancia de pelo menos um dos parâmetros é diferente de 0, e de fato podemos ver que varios deles possuem pvalue > 0.05 e são estatísticamente significantes:
    
path_img = r"C:\Users\eosjo\OneDrive\Área de Trabalho\Filesystem\MBA data science\ProjetoFinalTCC\Relatorios\Imagens"
os.chdir(path_img)
img = Image.open("pvalue-Cluster_k_means.png")
img.show()    

# Teste da estatística T -> #Para análise de relevância de variáveis indivídualmente 

# Teste da estatística T -> #Para análise de relevância de variáveis indivídualmente 

T_modelo_Linear_Cluster_k_means = modelo_Linear_Cluster_k_means.tvalues

p_value_indiv__modelo_Linear_Cluster_k_means = modelo_Linear_Cluster_k_means.pvalues


Cluster_DBscan_Statistics = df_Yearly.groupby('cluster_DBscan')['delay_minutes'].describe()
# -- Dumyzação da variável "Data Cluster_DBscan" ---- #
df_dummies_Cluster_DBscan = pd.get_dummies(df_Yearly, columns=['cluster_DBscan'],
                                      dtype=int,
                                      drop_first=True)

df_dummies_Cluster_DBscan  =(df_dummies_Cluster_DBscan.drop(columns=['date','train_id','to','from','from_id','Data_Pattern','to_id','scheduled_time','actual_time','status','type','Month','Centrality','Closseness','cluster_Hierarch', 'cluster_kmeans','stop_sequence', 'Clustering', 'Degree', 'Latitude','Longitude','Date','line','line_encoded','delay_minutes_rounded','actual_time_hours']))

df_dummies_Cluster_DBscan_columns_list= list(df_dummies_Cluster_DBscan.drop(columns=['delay_minutes']).columns)


formula_dummies_modelo_Cluster_DBscan = ' + '.join(df_dummies_Cluster_DBscan_columns_list)
formula_dummies_modelo_Cluster_DBscan = "delay_minutes ~ " + formula_dummies_modelo_Cluster_DBscan
print("Fórmula utilizada: ",formula_dummies_modelo_Cluster_DBscan)


modelo_Linear_Cluster_DBscan= sm.OLS.from_formula(formula_dummies_modelo_Cluster_DBscan, df_dummies_Cluster_DBscan).fit()


# Parâmetros do 'modelo_corrupcao_dummies'
print(modelo_Linear_Cluster_DBscan.summary(alpha=0.05))


r_squared_modelo_Linear_Cluster_DBscan = modelo_Linear_Cluster_DBscan.rsquared

#Teste F -> # Análise de variância para sabe se existe modelo ( P_value <0.05 a 95% de confiança )

F_modelo_Linear_Cluster_DBscan = modelo_Linear_Cluster_DBscan.fvalue

#anova_lm(modelo_Linear_Line).F

# Definição de p-value associado ao F_calculado: 
    
from scipy.stats import f 

pvalue_modelo_Linear_Cluster_DBscan = 1 - f.cdf(F_modelo_Linear_Cluster_DBscan,modelo_Linear_Cluster_DBscan.df_model,modelo_Linear_Cluster_DBscan.df_resid)

print(pvalue_modelo_Linear_Cluster_DBscan)
    
## Podemos ver que o p-value é bem pequeno, então é possível dizer que existe modelo usando essas variáveis, porém o r-squared é muito baixo, indicando que essas variáveis não explicam o suficiente do modelo.

# Podemos ver que a significancia de pelo menos um dos parâmetros é diferente de 0, e de fato podemos ver que varios deles possuem pvalue > 0.05 e são estatísticamente significantes:
    
path_img = r"C:\Users\eosjo\OneDrive\Área de Trabalho\Filesystem\MBA data science\ProjetoFinalTCC\Relatorios\Imagens"
os.chdir(path_img)
img = Image.open("pvalue-Cluster_DBscan.png")
img.show()    

# Teste da estatística T -> #Para análise de relevância de variáveis indivídualmente 

# Teste da estatística T -> #Para análise de relevância de variáveis indivídualmente 

T_modelo_Linear_Cluster_DBscan = modelo_Linear_Cluster_DBscan.tvalues

p_value_indiv__modelo_Linear_Cluster_DBscan = modelo_Linear_Cluster_DBscan.pvalues




#--------------------------------------------------------------------------------------------------------------
# Teste de Shapiro-Francia: interpretação
teste_sf = shapiro_francia( modelo_Linear_Cluster_DBscan.resid) #criação do objeto 'teste_sf'
teste_sf = teste_sf.items() #retorna o grupo de pares de valores-chave no dicionário
method, statistics_W, statistics_z, p = teste_sf #definição dos elementos da lista (tupla)
print('Statistics W=%.5f, p-value=%.6f' % (statistics_W[1], p[1]))
alpha = 0.05 #nível de significância
if p[1] > alpha:
	print('Não se rejeita H0 - Distribuição aderente à normalidade')
else:
	print('Rejeita-se H0 - Distribuição não aderente à normalidade')

#--------------------------------------------------------------------------------------------------------------






# -- Uso das variáveis indicadoras de redes  ---- #


df_Network_parameters = df_Yearly

df_Network_parameters  =(df_Network_parameters.drop(columns=['date','train_id','stop_sequence','from','from_id','Data_Pattern','to_id','scheduled_time','actual_time','status','type','Month','cluster_Hierarch', 'cluster_kmeans','cluster_DBscan', 'to', 'Latitude','Longitude','Date','line','line_encoded','delay_minutes_rounded','actual_time_hours']))

df_Network_parameters_columns_list= list(df_Network_parameters.drop(columns=['delay_minutes']).columns)


formula_modelo_Network_parameters = ' + '.join(df_Network_parameters_columns_list)
formula_modelo_Network_parameters = "delay_minutes ~ " + formula_modelo_Network_parameters
print("Fórmula utilizada: ",formula_modelo_Network_parameters)

modelo_Linear_Network_parameters= sm.OLS.from_formula(formula_modelo_Network_parameters, df_Network_parameters).fit()

# Parâmetros do 'modelo_corrupcao_dummies'
print(modelo_Linear_Network_parameters.summary(alpha=0.05))


r_squared_modelo_Linear_Network_parameters = modelo_Linear_Network_parameters.rsquared

#Teste F -> # Análise de variância para sabe se existe modelo ( P_value <0.05 a 95% de confiança )

F_modelo_Linear_Network_parameters = modelo_Linear_Network_parameters.fvalue

#anova_lm(modelo_Linear_Line).F

# Definição de p-value associado ao F_calculado: 
    
from scipy.stats import f 

pvalue_modelo_Linear_Network_parameters = 1 - f.cdf(F_modelo_Linear_Network_parameters,modelo_Linear_Network_parameters.df_model,modelo_Linear_Network_parameters.df_resid)

print(pvalue_modelo_Linear_Network_parameters)
    
## Podemos ver que o p-value é bem pequeno, então é possível dizer que existe modelo usando essas variáveis, porém o r-squared é muito baixo, indicando que essas variáveis não explicam o suficiente do modelo.

# Podemos ver que a significancia de pelo menos um dos parâmetros é diferente de 0, e de fato podemos ver que varios deles possuem pvalue > 0.05 e são estatísticamente significantes:
    
path_img = r"C:\Users\eosjo\OneDrive\Área de Trabalho\Filesystem\MBA data science\ProjetoFinalTCC\Relatorios\Imagens"
os.chdir(path_img)
img = Image.open("pvalue-Network_parameters.png")
img.show()    

# Teste da estatística T -> #Para análise de relevância de variáveis indivídualmente 

# Teste da estatística T -> #Para análise de relevância de variáveis indivídualmente 

T_modelo_Linear_Network_parameters = modelo_Linear_Network_parameters.tvalues

p_value_indiv__modelo_Linear_Network_parameters = modelo_Linear_Network_parameters.pvalues


#--------------------------------------------------------------------------------------------------------------
# Teste de Shapiro-Francia: interpretação
teste_sf = shapiro_francia( modelo_Linear_Network_parameters.resid) #criação do objeto 'teste_sf'
teste_sf = teste_sf.items() #retorna o grupo de pares de valores-chave no dicionário
method, statistics_W, statistics_z, p = teste_sf #definição dos elementos da lista (tupla)
print('Statistics W=%.5f, p-value=%.6f' % (statistics_W[1], p[1]))
alpha = 0.05 #nível de significância
if p[1] > alpha:
	print('Não se rejeita H0 - Distribuição aderente à normalidade')
else:
	print('Rejeita-se H0 - Distribuição não aderente à normalidade')

#--------------------------------------------------------------------------------------------------------------



#---------Análise conjunta de todas as variáveis para regressão linear ----------------------------------#


formula_dummies_modelo_all_variables =[]
formula_dummies_modelo_all_variables = np.concatenate((formula_dummies_modelo_all_variables,df_dummies_Cluster_DBscan_columns_list),axis=0)
formula_dummies_modelo_all_variables = np.concatenate((formula_dummies_modelo_all_variables,df_dummies_Cluster_k_means_columns_list),axis=0)
formula_dummies_modelo_all_variables = np.concatenate((formula_dummies_modelo_all_variables,df_dummies_Line_columns_list),axis=0)
formula_dummies_modelo_all_variables = np.concatenate((formula_dummies_modelo_all_variables,df_dummies_Month_columns_list),axis=0)
formula_dummies_modelo_all_variables = np.concatenate((formula_dummies_modelo_all_variables,df_dummies_Pattern_columns_list),axis=0)
formula_dummies_modelo_all_variables = np.concatenate((formula_dummies_modelo_all_variables,df_dummies_Station_columns_list),axis=0)
formula_dummies_modelo_all_variables = np.concatenate((formula_dummies_modelo_all_variables,df_dummies_Stop_Seq_columns_list),axis=0)
formula_dummies_modelo_all_variables = np.concatenate((formula_dummies_modelo_all_variables,df_Network_parameters_columns_list),axis=0)

formula_dummies_modelo_all_variables = ' + '.join(formula_dummies_modelo_all_variables)
formula_dummies_modelo_all_variables = "delay_minutes ~ " + formula_dummies_modelo_all_variables
print("Fórmula utilizada: ",formula_dummies_modelo_all_variables)

df_all_variables = df_Yearly
df_all_variables = pd.get_dummies(df_all_variables, columns=['line'],
                                      dtype=int,
                                      drop_first=True)
df_all_variables = pd.get_dummies(df_all_variables, columns=['Month'],
                                      dtype=int,
                                      drop_first=True)
df_all_variables = pd.get_dummies(df_all_variables, columns=['Data_Pattern'],
                                      dtype=int,
                                      drop_first=True)
df_all_variables = pd.get_dummies(df_all_variables, columns=['to'],
                                     dtype=int,
                                      drop_first=True)
df_all_variables = pd.get_dummies(df_all_variables, columns=['stop_sequence'],
                                      dtype=int,
                                      drop_first=True)
df_all_variables = pd.get_dummies(df_all_variables, columns=['cluster_kmeans'],
                                      dtype=int,
                                      drop_first=True)
df_all_variables = pd.get_dummies(df_all_variables, columns=['cluster_DBscan'],
                                      dtype=int,
                                      drop_first=True)


modelo_Linear_all_variables= sm.OLS.from_formula(formula_dummies_modelo_all_variables, df_all_variables).fit()


# Parâmetros do 'modelo_corrupcao_dummies'
print(modelo_Linear_all_variables.summary(alpha=0.05))


r_squared_modelo_all_variables = modelo_Linear_all_variables.rsquared

#Teste F -> # Análise de variância para sabe se existe modelo ( P_value <0.05 a 95% de confiança )

F_modelo_Linear_all_variables = modelo_Linear_all_variables.fvalue

#anova_lm(modelo_Linear_Line).F

# Definição de p-value associado ao F_calculado: 
    
from scipy.stats import f 

pvalue_modelo_Linear_all_variables = 1 - f.cdf(F_modelo_Linear_all_variables,modelo_Linear_all_variables.df_model,modelo_Linear_all_variables.df_resid)

print(pvalue_modelo_Linear_all_variables)


modelo_Linear_all_variables = stepwise(modelo_Linear_all_variables, pvalue_limit=0.05)




#-------------------------Teste de aderência a normalidade Shapiro - francia -------------------------------------------------------------#


# Teste de Shapiro-Francia: interpretação
teste_sf = shapiro_francia(modelo_Linear_all_variables.resid) #criação do objeto 'teste_sf'
teste_sf = teste_sf.items() #retorna o grupo de pares de valores-chave no dicionário
method, statistics_W, statistics_z, p = teste_sf #definição dos elementos da lista (tupla)
print('Statistics W=%.5f, p-value=%.6f' % (statistics_W[1], p[1]))
alpha = 0.05 #nível de significância
if p[1] > alpha:
	print('Não se rejeita H0 - Distribuição aderente à normalidade')
else:
	print('Rejeita-se H0 - Distribuição não aderente à normalidade')



#------------------------------------Delete all variables to clear RAM memory ----------------------------------#

# Define the list of variable names that you want to keep
keep_vars = ['formula_dummies_modelo_all_variables', 'df_all_variables']

# Get a list of all variable names in the globals dictionary
all_vars = list(globals().keys())

# Filter the variables that are not in the keep_vars list
vars_to_delete = [var for var in all_vars if var not in keep_vars and not var.startswith('__') and not callable(globals()[var])]

# Delete the filtered variables
for var in vars_to_delete:
    del globals()[var]

# Print to check the remaining variables
print(globals())


#-----------------------------------------------------------------------------------------------------------#


# ------------------------ Modelo BOX-COX Não linear -------------------------------------------------------------------#

#será adotada uma estatégia de adição de um valor muito pequeno ao Y para a retirada de valores nulos 0, para transformar valores em estritamente positivos

df_Yearly_provisory = df_Yearly
df_Yearly_provisory['delay_minutes'] = np.where(df_Yearly_provisory['delay_minutes'] == 0, df_Yearly_provisory['delay_minutes'] + 0.00001, df_Yearly_provisory['delay_minutes'])


yast, lmbda = boxcox(df_Yearly_provisory['delay_minutes'])
df_Yearly_provisory['delay_minutes_box_cox'] = yast


#---------Análise conjunta de todas as variáveis para regressão box-cox ----------------------------------#


formula_dummies_modelo_box_cox =[]
formula_dummies_modelo_box_cox = np.concatenate((formula_dummies_modelo_box_cox,df_dummies_Cluster_DBscan_columns_list),axis=0)
formula_dummies_modelo_box_cox = np.concatenate((formula_dummies_modelo_box_cox,df_dummies_Cluster_k_means_columns_list),axis=0)
formula_dummies_modelo_box_cox = np.concatenate((formula_dummies_modelo_box_cox,df_dummies_Line_columns_list),axis=0)
formula_dummies_modelo_box_cox = np.concatenate((formula_dummies_modelo_box_cox,df_dummies_Month_columns_list),axis=0)
formula_dummies_modelo_box_cox = np.concatenate((formula_dummies_modelo_box_cox,df_dummies_Pattern_columns_list),axis=0)
formula_dummies_modelo_box_cox = np.concatenate((formula_dummies_modelo_box_cox,df_dummies_Station_columns_list),axis=0)
formula_dummies_modelo_box_cox = np.concatenate((formula_dummies_modelo_box_cox,df_dummies_Stop_Seq_columns_list),axis=0)
formula_dummies_modelo_box_cox = np.concatenate((formula_dummies_modelo_box_cox,df_Network_parameters_columns_list),axis=0)

formula_dummies_modelo_box_cox = ' + '.join(formula_dummies_modelo_box_cox)
formula_dummies_modelo_box_cox = "delay_minutes_box_cox ~ " + formula_dummies_modelo_box_cox
print("Fórmula utilizada: ",formula_dummies_modelo_box_cox)

df_all_variables = df_Yearly_provisory
df_all_variables = pd.get_dummies(df_all_variables, columns=['line'],
                                      dtype=int,
                                      drop_first=True)
df_all_variables = pd.get_dummies(df_all_variables, columns=['Month'],
                                      dtype=int,
                                      drop_first=True)
df_all_variables = pd.get_dummies(df_all_variables, columns=['Data_Pattern'],
                                      dtype=int,
                                      drop_first=True)
df_all_variables = pd.get_dummies(df_all_variables, columns=['to'],
                                     dtype=int,
                                      drop_first=True)
df_all_variables = pd.get_dummies(df_all_variables, columns=['stop_sequence'],
                                      dtype=int,
                                      drop_first=True)
df_all_variables = pd.get_dummies(df_all_variables, columns=['cluster_kmeans'],
                                      dtype=int,
                                      drop_first=True)
df_all_variables = pd.get_dummies(df_all_variables, columns=['cluster_DBscan'],
                                      dtype=int,
                                      drop_first=True)


modelo_box_cox_all_variables= sm.OLS.from_formula(formula_dummies_modelo_box_cox, df_all_variables).fit()


#modelo_box_cox_all_variables = stepwise(modelo_box_cox_all_variables, pvalue_limit=0.05)


# Parâmetros do 'modelo_corrupcao_dummies'
print(modelo_box_cox_all_variables.summary(alpha=0.05))


# Teste de Shapiro-Francia: interpretação
teste_sf = shapiro_francia(modelo_box_cox_all_variables.resid) #criação do objeto 'teste_sf'
teste_sf = teste_sf.items() #retorna o grupo de pares de valores-chave no dicionário
method, statistics_W, statistics_z, p = teste_sf #definição dos elementos da lista (tupla)
print('Statistics W=%.5f, p-value=%.6f' % (statistics_W[1], p[1]))
alpha = 0.05 #nível de significância
if p[1] > alpha:
	print('Não se rejeita H0 - Distribuição aderente à normalidade')
else:
	print('Rejeita-se H0 - Distribuição não aderente à normalidade')


r_squared_modelo_box_cox_all_variables = modelo_box_cox_all_variables.rsquared

#Teste F -> # Análise de variância para sabe se existe modelo ( P_value <0.05 a 95% de confiança )

F_modelo_box_cox_all_variables = modelo_box_cox_all_variables.fvalue

#anova_lm(modelo_Linear_Line).F

# Definição de p-value associado ao F_calculado: 
    
from scipy.stats import f 

pvalue_modelo_box_cox_all_variables = 1 - f.cdf(F_modelo_box_cox_all_variables,modelo_box_cox_all_variables.df_model,modelo_box_cox_all_variables.df_resid)

print(pvalue_modelo_box_cox_all_variables)



# In[4.12]: Histograma dos resíduos do modelo_box-cox (Para verificação de aderência a normalidade)

plt.figure(figsize=(15,10))
hist2 = sns.histplot(data=modelo_box_cox_all_variables.resid, kde=True, bins=25,
                     color='darkviolet', alpha=0.4, edgecolor='snow',
                     line_kws={'linewidth': 3})
hist2.get_lines()[0].set_color('indigo')
plt.xlabel('Resíduos', fontsize=20)
plt.ylabel('Frequência', fontsize=20)
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.show()


#------------------------------------Delete all variables to clear RAM memory ----------------------------------#

# Define the list of variable names that you want to keep
keep_vars = ['formula_dummies_modelo_box_cox', 'df_all_variables']

# Get a list of all variable names in the globals dictionary
all_vars = list(globals().keys())

# Filter the variables that are not in the keep_vars list
vars_to_delete = [var for var in all_vars if var not in keep_vars and not var.startswith('__') and not callable(globals()[var])]

# Delete the filtered variables
for var in vars_to_delete:
    del globals()[var]

# Print to check the remaining variables
print(globals())


#-----------------------------------------------------------------------------------------------------------#



#cutoff_definition_of_event_values = np.arange(0.5, 5.0, 0.5)  # Gera valores de 1 até 5 inclusive, incrementando de 0.2
cutoff_definition_of_event_values = [1]
lista_sensitividade = []
lista_especificidade = []
lista_acuracia = []
lista_cuttof_def_event =[]


for cutoff_definition_of_event in cutoff_definition_of_event_values:
    df_all_variables_Logistico = df_Yearly
    Cut_off_atraso = cutoff_definition_of_event
    df_all_variables_Logistico ['delay_minutes_Event'] = np.where(df_all_variables_Logistico ['delay_minutes'] >= Cut_off_atraso , 1,0)

    
    #---------Análise conjunta de todas as variáveis para  ----------------------------------#

    formula_dummies_modelo_Logistico =[]
    #formula_dummies_modelo_Logistico = np.concatenate((formula_dummies_modelo_Logistico,df_dummies_Cluster_DBscan_columns_list),axis=0)
    formula_dummies_modelo_Logistico = np.concatenate((formula_dummies_modelo_Logistico,df_dummies_Cluster_k_means_columns_list),axis=0)
    formula_dummies_modelo_Logistico = np.concatenate((formula_dummies_modelo_Logistico,df_dummies_Line_columns_list),axis=0)
    formula_dummies_modelo_Logistico = np.concatenate((formula_dummies_modelo_Logistico,df_dummies_Month_columns_list),axis=0)
    formula_dummies_modelo_Logistico = np.concatenate((formula_dummies_modelo_Logistico,df_dummies_Pattern_columns_list),axis=0)
    formula_dummies_modelo_Logistico = np.concatenate((formula_dummies_modelo_Logistico,df_dummies_Station_columns_list),axis=0)
    formula_dummies_modelo_Logistico = np.concatenate((formula_dummies_modelo_Logistico,df_dummies_Stop_Seq_columns_list),axis=0)
    formula_dummies_modelo_Logistico = np.concatenate((formula_dummies_modelo_Logistico,df_Network_parameters_columns_list),axis=0)

    formula_dummies_modelo_Logistico = ' + '.join(formula_dummies_modelo_Logistico)
    formula_dummies_modelo_Logistico = "delay_minutes_Event ~ " + formula_dummies_modelo_Logistico
    print("Fórmula utilizada: ",formula_dummies_modelo_Logistico)

    df_all_variables_Logistico = df_Yearly
    df_all_variables_Logistico = pd.get_dummies(df_all_variables_Logistico, columns=['line'],
                                      dtype=int,
                                      drop_first=True)
    df_all_variables_Logistico = pd.get_dummies(df_all_variables_Logistico, columns=['Month'],
                                        dtype=int,
                                      drop_first=True)
    df_all_variables_Logistico = pd.get_dummies(df_all_variables_Logistico, columns=['Data_Pattern'],
                                      dtype=int,
                                      drop_first=True)
    df_all_variables_Logistico = pd.get_dummies(df_all_variables_Logistico, columns=['to'],
                                     dtype=int,
                                         drop_first=True)
    df_all_variables_Logistico = pd.get_dummies(df_all_variables_Logistico, columns=['stop_sequence'],
                                      dtype=int,
                                      drop_first=True)
    df_all_variables_Logistico = pd.get_dummies(df_all_variables_Logistico, columns=['cluster_kmeans'],
                                      dtype=int,
                                      drop_first=True)
    df_all_variables_Logistico = pd.get_dummies(df_all_variables_Logistico, columns=['cluster_DBscan'],
                                      dtype=int,
                                     drop_first=True)


# Tentativa de estimação de um modelo Logístico binário usando "Atraso" como evento, e "Não atraso" como Não evento
# Uso de um corte de 1 minuto para identificar um atraso 
# Estimação de um modelo logístico binário pela função 'smf.glm'
#('statsmodels.formula.api')

    modelo_Logistico_all_variables = smf.glm(formula=formula_dummies_modelo_Logistico, data=df_all_variables_Logistico,
                         family=sm.families.Binomial()).fit()
    

#correlation_matrix = df_dummies_Month.drop(columns=['delay_minutes']).corr()
#print("Correlation Matrix:\n", correlation_matrix)



#modelo_Logistico_all_variables = sm.Logit.from_formula(formula_dummies_modelo_Logistico,
#                                         df_all_variables_Logistico).fit()
#

    #modelo_Logistico_all_variables = stepwise(modelo_Logistico_all_variables, pvalue_limit=0.05)


    # Parâmetros do 'modelo_atrasos'
    modelo_Logistico_all_variables.summary()
    
    


# -----Calculo do Log-Likelihood dividido pelo número de observações ---------------#
    # Obter a log-verossimilhança
    log_likelihood = modelo_Logistico_all_variables.llf

    # Obter o número de observações
    num_observations = modelo_Logistico_all_variables.nobs

    # Calcular a razão log-verossimilhança / número de observações
    loglike_per_observation = log_likelihood / num_observations


    # Calcular o AIC para comparação de loglike entre modelos diferentes, com a mesma quantidade de observações. (Quanto menor, melhor o modelo na comparação)
    aic = modelo_Logistico_all_variables.aic

    print("Log-Verossimilhança por Observação:", loglike_per_observation)
    print("Akaike Information Criterion (AIC):", aic)
    



    # Adicionando os valores previstos de probabilidade na base de dados
    df_all_variables_Logistico['predict'] = modelo_Logistico_all_variables.predict()
    df_all_variables_Logistico['Logit'] = modelo_Logistico_all_variables.predict(linear=True)



    # Matriz de confusão para cutoff = cuttof
    parametros = matriz_confusao(observado=df_all_variables_Logistico['delay_minutes_Event'],
               predicts=df_all_variables_Logistico['predict'], 
                cutoff=0.5)
    
    
    
    lista_cuttof_def_event.append(cutoff_definition_of_event)
    lista_sensitividade.append(parametros['Sensitividade'].iloc[0])
    lista_especificidade.append(parametros['Especificidade'].iloc[0])
    lista_acuracia.append(parametros['Acurácia'].iloc[0]) 
 
    dados_plotagem = espec_sens(observado = df_all_variables_Logistico['delay_minutes_Event'],
                            predicts = df_all_variables_Logistico['predict'])
    dados_plotagem

    string  = "cutoff_definition_of_event = " + str(cutoff_definition_of_event)
#Plotagem de um gráfico que mostra a variação da especificidade e da sensitividade em função do cutoff

    plt.figure(figsize=(15,10))
    with plt.style.context('seaborn-v0_8-whitegrid'):
        plt.plot(dados_plotagem.cutoffs,dados_plotagem.sensitividade, marker='o',
                 color='indigo', markersize=8)
        plt.plot(dados_plotagem.cutoffs,dados_plotagem.especificidade, marker='o',
                 color='limegreen', markersize=8)
        plt.xlabel('Cuttoff', fontsize=20)
        plt.ylabel(string, fontsize=20)
        plt.xticks(np.arange(0, 1.1, 0.2), fontsize=14)
        plt.yticks(np.arange(0, 1.1, 0.2), fontsize=14)
        plt.legend(['Sensitividade', 'Especificidade'], fontsize=20)
        plt.show()


    # Construção da curva ROC
    from sklearn.metrics import roc_curve, auc

    # Função 'roc_curve' do pacote 'metrics' do sklearn

    fpr, tpr, thresholds =roc_curve(df_all_variables_Logistico['delay_minutes_Event'], df_all_variables_Logistico['predict'])
    roc_auc = auc(fpr, tpr)

    # Cálculo do coeficiente de GINI
    gini = (roc_auc - 0.5)/(0.5)

    # Plotando a curva ROC
    plt.figure(figsize=(15,10))
    plt.plot(fpr, tpr, marker='o', color='darkorchid', markersize=10, linewidth=3)
    plt.plot(fpr, fpr, color='gray', linestyle='dashed')
    plt.title('Área abaixo da curva: %g' % round(roc_auc, 4) +
              ' | Coeficiente de GINI: %g' % round(gini, 4), fontsize=22)
    plt.xlabel('1 - Especificidade', fontsize=20)
    plt.ylabel('Sensitividade', fontsize=20)
    plt.xticks(np.arange(0, 1.1, 0.2), fontsize=14)
    plt.yticks(np.arange(0, 1.1, 0.2), fontsize=14)
    plt.show()
    
    
    # Plotando Sigmoide em função do logíto

    plt.figure(figsize=(15,10))
    sns.regplot(x=df_all_variables_Logistico['Logit'], y=df_all_variables_Logistico['predict'],
                ci=None, marker='o', logistic=True,
                scatter_kws={'color':'orange', 's':250, 'alpha':0.7},
                line_kws={'color':'darkorchid', 'linewidth':7})
    plt.axhline(y = 0.5, color = 'grey', linestyle = ':')
    plt.xlabel('Logito (Z)', fontsize=20)
    plt.ylabel('Probabilidade de evento (P)', fontsize=20)
    plt.xticks(np.arange(df_all_variables_Logistico['Logit'].min() - 0.01 , df_all_variables_Logistico['Logit'].max() + 0.01),
               fontsize=14)
    plt.yticks(np.arange(0, 1.1, 0.2), fontsize=14)
    plt.show
    


       
    #Criar dataframe com os resultados nos seus respectivos cutoffs
resultado = pd.DataFrame({'cutoffs_definition_event': lista_cuttof_def_event,'sensitividade':lista_sensitividade,'especificidade':lista_especificidade, 'acuracia': lista_acuracia})



#------------------------------------Delete all variables to clear RAM memory ----------------------------------#

# Define the list of variable names that you want to keep
keep_vars = ['formula_dummies_modelo_Logistico', 'df_all_variables_Logistico',]

# Get a list of all variable names in the globals dictionary
all_vars = list(globals().keys())

# Filter the variables that are not in the keep_vars list
vars_to_delete = [var for var in all_vars if var not in keep_vars and not var.startswith('__') and not callable(globals()[var])]

# Delete the filtered variables
for var in vars_to_delete:
    del globals()[var]

# Print to check the remaining variables
print(globals())


#-----------------------------------------------------------------------------------------------------------#


# Deep Learn 















#------------Análise para um contexto baseado em linhas-----------------

# In[1.5]: plot grafico boxplot do deleay em minutos arredondado
Mean_delay_per_station = df_Yearly.groupby('line')['delay_minutes'].mean().reset_index()
Mean_delay_per_station



plt.figure(figsize=(15,10))

plt.ylim(0, 30)
sns.boxplot(data=df_Yearly, x='line_encoded', y='delay_minutes_rounded',
            linewidth=2, orient='v', palette='viridis')

plt.ylabel('delay_minutes', fontsize=20)
plt.xlabel('line $j$ (nível 2)', fontsize=20)
plt.tick_params(axis='y', labelsize=17)
plt.tick_params(axis='x', labelsize=17)
plt.show()


# In[1.1]: Kernel density estimation (KDE) - função densidade de probabilidade
#da variável dependente ('desempenho') por escola

Lines = df_Yearly['line'].unique()
colors = sns.color_palette('viridis', len(Lines))

plt.figure(figsize=(15, 10))
g = sns.pairplot(df_Yearly[['line', 'delay_minutes_rounded']], hue='line',
                 height=8,
                 aspect=1.5, palette=colors)
g._legend.remove()
g.set(xlabel=None)
g.set(ylabel=None)
g.tick_params(axis='both', which='major', labelsize=15)

# Gera a legenda com cores e rótulos das escolas
legend_elements = [plt.Line2D([0], [0], marker='o', color='w',
                              markerfacecolor=color,
                              markersize=10, label=line)
                   for line, color in zip(Lines, colors)]
plt.legend(handles=legend_elements, title='Line', fontsize=14,
           title_fontsize=18)

# Adiciona os rótulos diretamente na figura
plt.gcf().text(0.5, -0.01, 'delay_minutes_rounded', ha='center', fontsize=20)
plt.gcf().text(-0.01, 0.5, 'Frequência', va='center', rotation='vertical',
               fontsize=20)
plt.show()












# In[1.2]: Kernel density estimation (KDE) - função densidade de probabilidade
#da variável dependente ('delay_minutes_rounded'), com histograma e por linha separadamente
#(função 'GridSpec' do pacote 'matplotlib.gridspec')

Lines = df_Yearly['line'].unique()

fig = plt.figure(figsize=(15, 14))
gs = GridSpec(len(Lines) // 2 + 1, 2, figure=fig)

for i, L in enumerate(Lines):
    ax = fig.add_subplot(gs[i])

    # Subset dos dados por escola
    df_Lines = df_Yearly[df_Yearly['line'] ==  L]

    # Densidade dos dados
    densidade = gaussian_kde(df_Lines['delay_minutes_rounded'])
    x_vals = np.linspace(min(df_Lines['delay_minutes_rounded']),
                         max(df_Lines['delay_minutes_rounded']), len( df_Lines))
    y_vals = densidade(x_vals)

    # Plotagem da density area
    ax.fill_between(x_vals, y_vals,
                    color=sns.color_palette('viridis',
                                            as_cmap=True)(i/len(Lines)),
                    alpha=0.3)
    
    # Adiciona o histograma
    sns.histplot(df_Lines['delay_minutes_rounded'], ax=ax, stat="density", color="black",
                 edgecolor="black", fill=True, 
                 bins=100, alpha=0.1)
    ax.set_title(f'Lines {L}', fontsize=15)
    ax.set_ylabel('Densidade')
    ax.set_xlabel('delay_minutes_rounded')

plt.tight_layout()
plt.show()





#------------Análise para um contexto baseado em Horario de pico/ não é horario de pico----------------


# In[1.5]: plot grafico boxplot do deleay em minutos arredondado
Mean_delay_per_Pattern = df_Yearly.groupby('Data_Pattern')['delay_minutes'].mean().reset_index()
Mean_delay_per_Pattern



plt.figure(figsize=(15,10))

plt.ylim(0, 30)
sns.boxplot(data=df_Yearly, x='Data_Pattern', y='delay_minutes_rounded',
            linewidth=2, orient='v', palette='viridis')

plt.ylabel('delay_minutes', fontsize=20)
plt.xlabel('Pattern $j$ (nível 2)', fontsize=20)
plt.tick_params(axis='y', labelsize=17)
plt.tick_params(axis='x', labelsize=17)
plt.show()








# In[1.2]: Kernel density estimation (KDE) - função densidade de probabilidade
#da variável dependente ('delay_minutes_rounded'), com histograma e por linha separadamente
#(função 'GridSpec' do pacote 'matplotlib.gridspec')

Data_Pattern = df_Yearly['Data_Pattern'].unique()

fig = plt.figure(figsize=(15, 14))
gs = GridSpec(len(Data_Pattern) // 2 + 1, 2, figure=fig)

for i, D in enumerate(Data_Pattern):
    ax = fig.add_subplot(gs[i])

    # Subset dos dados por escola
    df_Data_Pattern = df_Yearly[df_Yearly['Data_Pattern'] ==  D]

    # Densidade dos dados
    densidade = gaussian_kde(df_Data_Pattern['delay_minutes_rounded'])
    x_vals = np.linspace(min(df_Data_Pattern['delay_minutes_rounded']),
                         max(df_Data_Pattern['delay_minutes_rounded']), len( df_Data_Pattern))
    y_vals = densidade(x_vals)

    # Plotagem da density area
    ax.fill_between(x_vals, y_vals,
                    color=sns.color_palette('viridis',
                                            as_cmap=True)(i/len(Data_Pattern)),
                    alpha=0.3)
    
    # Adiciona o histograma
    sns.histplot(df_Data_Pattern['delay_minutes_rounded'], ax=ax, stat="density", color="black",
                 edgecolor="black", fill=True, 
                 bins=100, alpha=0.1)
    ax.set_title(f'Dta Pattern {D}', fontsize=15)
    ax.set_ylabel('Densidade')
    ax.set_xlabel('delay_minutes_rounded')

plt.tight_layout()
plt.show()

#------------Análise para um contexto baseado em linhas-----------------

# In[1.5]: plot grafico boxplot do deleay em minutos arredondado
Mean_delay_per_month = df_Yearly.groupby('Month')['delay_minutes'].mean().reset_index()
Mean_delay_per_month



plt.figure(figsize=(15,10))

plt.ylim(0, 30)
sns.boxplot(data=df_Yearly, x='Month', y='delay_minutes_rounded',
            linewidth=2, orient='v', palette='viridis')

plt.ylabel('delay_minutes', fontsize=20)
plt.xlabel('Month $j$ (nível 2)', fontsize=20)
plt.tick_params(axis='y', labelsize=17)
plt.tick_params(axis='x', labelsize=17)
plt.show()


# In[1.1]: Kernel density estimation (KDE) - função densidade de probabilidade
#da variável dependente ('desempenho') por escola

Months = df_Yearly['Month'].unique()
colors = sns.color_palette('viridis', len(Months))

plt.figure(figsize=(15, 10))
g = sns.pairplot(df_Yearly[['Month', 'delay_minutes_rounded']], hue='Month',
                 height=8,
                 aspect=1.5, palette=colors)
g._legend.remove()
g.set(xlabel=None)
g.set(ylabel=None)
g.tick_params(axis='both', which='major', labelsize=15)

# Gera a legenda com cores e rótulos das escolas
legend_elements = [plt.Line2D([0], [0], marker='o', color='w',
                              markerfacecolor=color,
                              markersize=10, label=month)
                   for month, color in zip(Months, colors)]
plt.legend(handles=legend_elements, title='Line', fontsize=14,
           title_fontsize=18)

# Adiciona os rótulos diretamente na figura
plt.gcf().text(0.5, -0.01, 'delay_minutes_rounded', ha='center', fontsize=20)
plt.gcf().text(-0.01, 0.5, 'Frequência', va='center', rotation='vertical',
               fontsize=20)
plt.show()












# In[1.2]: Kernel density estimation (KDE) - função densidade de probabilidade
#da variável dependente ('delay_minutes_rounded'), com histograma e por linha separadamente
#(função 'GridSpec' do pacote 'matplotlib.gridspec')

Months = df_Yearly['Month'].unique()

fig = plt.figure(figsize=(15, 14))
gs = GridSpec(len(Months) // 2 + 1, 2, figure=fig)

for i, M in enumerate(Months):
    ax = fig.add_subplot(gs[i])

    # Subset dos dados por escola
    df_Months = df_Yearly[df_Yearly['Month'] ==  M]

    # Densidade dos dados
    densidade = gaussian_kde(df_Months['delay_minutes_rounded'])
    x_vals = np.linspace(min(df_Months['delay_minutes_rounded']),
                         max(df_Months['delay_minutes_rounded']), len( df_Months))
    y_vals = densidade(x_vals)

    # Plotagem da density area
    ax.fill_between(x_vals, y_vals,
                    color=sns.color_palette('viridis',
                                            as_cmap=True)(i/len(Months)),
                    alpha=0.3)
    
    # Adiciona o histograma
    sns.histplot(df_Months['delay_minutes_rounded'], ax=ax, stat="density", color="black",
                 edgecolor="black", fill=True, 
                 bins=100, alpha=0.1)
    ax.set_title(f'Months {M}', fontsize=15)
    ax.set_ylabel('Densidade')
    ax.set_xlabel('delay_minutes_rounded')

plt.tight_layout()
plt.show()









    
    # In[1.5]: Criação de um agrupamento de dados para retirar algumas estatisticas agrupadas
grouped_data = df_Yearly.astype({'stop_sequence': 'float'}).groupby(['date', 'train_id'])

# Creating some variables to be analysed

acc_delay = grouped_data['delay_minutes'].sum()
mean_delay = grouped_data['delay_minutes'].mean()
num_stations = grouped_data['stop_sequence'].agg('max')
trip_pattern = grouped_data['Data_Pattern'].agg(lambda x: pd.Series.mode(x)[0])
Line = grouped_data['line'].agg(lambda x: pd.Series.mode(x)[0])


#-------------- Modelagem multinível -----------------------------#

#--------Análise da significancia do contexto estação para a explicação dos atrasos------------#
# Estimação do modelo nulo (função 'MixedLM' do pacote 'statsmodels')

modelo_nulo_hlm2 = sm.MixedLM.from_formula(formula='delay_minutes ~ 1',
                                           groups='line',
                                           re_formula='1',
                                           data=df_Yearly).fit()
LineVar = modelo_nulo_hlm2.cov_re.iloc[0,0]
scale = modelo_nulo_hlm2.scale
# Intraclasse correlation ICC
ICC_nulo_hlm2 = LineVar / (LineVar + scale)



# In[1.14]: Análise da significância estatística dos efeitos aleatórios de
#intercepto

teste = float(modelo_nulo_hlm2.cov_re.iloc[0, 0]) /\
    float(pd.DataFrame(modelo_nulo_hlm2.summary().tables[1]).iloc[1, 1])

p_value = 2 * (1 - stats.norm.cdf(abs(teste)))

print(f"Estatística z para a Significância dos Efeitos Aleatórios: {teste:.3f}")
print(f"P-valor: {p_value:.3f}")

if p_value >= 0.05:
    print("Ausência de significância estatística dos efeitos aleatórios ao nível de confiança de 95%.")
else:
    print("Efeitos aleatórios contextuais significantes ao nível de confiança de 95%.")



modelo_nulo_hlm2.summary()


#--------Análise da significancia do horario do dia para a explicação dos atrasos------------#


#-------------- Modelagem multinível -----------------------------#

# Estimação do modelo nulo (função 'MixedLM' do pacote 'statsmodels')

modelo_nulo_hlm2 = sm.MixedLM.from_formula(formula='delay_minutes ~ 1',
                                           groups='Data_Pattern',
                                           re_formula='1',
                                           data=df_Yearly).fit()
LineVar = modelo_nulo_hlm2.cov_re.iloc[0,0]
scale = modelo_nulo_hlm2.scale
# Intraclasse correlation ICC
ICC_nulo_hlm2 = LineVar / (LineVar + scale)

# In[1.14]: Análise da significância estatística dos efeitos aleatórios de
#intercepto

teste = float(modelo_nulo_hlm2.cov_re.iloc[0, 0]) /\
    float(pd.DataFrame(modelo_nulo_hlm2.summary().tables[1]).iloc[1, 1])

p_value = 2 * (1 - stats.norm.cdf(abs(teste)))

print(f"Estatística z para a Significância dos Efeitos Aleatórios: {teste:.3f}")
print(f"P-valor: {p_value:.3f}")

if p_value >= 0.05:
    print("Ausência de significância estatística dos efeitos aleatórios ao nível de confiança de 95%.")
else:
    print("Efeitos aleatórios contextuais significantes ao nível de confiança de 95%.")

modelo_nulo_hlm2.summary()


#-------------- Modelagem multinível -----------------------------#

# Estimação do modelo nulo (função 'MixedLM' do pacote 'statsmodels')

modelo_nulo_hlm2 = sm.MixedLM.from_formula(formula='delay_minutes ~ 1',
                                           groups='stop_sequence',
                                           re_formula='1',
                                           data=df_Yearly).fit()
LineVar = modelo_nulo_hlm2.cov_re.iloc[0,0]
scale = modelo_nulo_hlm2.scale
# Intraclasse correlation ICC
ICC_nulo_hlm2 = LineVar / (LineVar + scale)
print("ICC = ") 
print(ICC_nulo_hlm2) 

# In[1.14]: Análise da significância estatística dos efeitos aleatórios de
#intercepto

teste = float(modelo_nulo_hlm2.cov_re.iloc[0, 0]) /\
    float(pd.DataFrame(modelo_nulo_hlm2.summary().tables[1]).iloc[1, 1])

p_value = 2 * (1 - stats.norm.cdf(abs(teste)))

print(f"Estatística z para a Significância dos Efeitos Aleatórios: {teste:.3f}")
print(f"P-valor: {p_value:.3f}")

if p_value >= 0.05:
    print("Ausência de significância estatística dos efeitos aleatórios ao nível de confiança de 95%.")
else:
    print("Efeitos aleatórios contextuais significantes ao nível de confiança de 95%.")

modelo_nulo_hlm2.summary()


#-------------- Modelagem multinível -----------------------------#

# Estimação do modelo nulo (função 'MixedLM' do pacote 'statsmodels')

modelo_nulo_hlm2 = sm.MixedLM.from_formula(formula='delay_minutes ~ 1',
                                           groups='to',
                                           re_formula='1',
                                           data=df_Yearly).fit()
LineVar = modelo_nulo_hlm2.cov_re.iloc[0,0]
scale = modelo_nulo_hlm2.scale
# Intraclasse correlation ICC
ICC_nulo_hlm2 = LineVar / (LineVar + scale)
print("ICC = ") 
print(ICC_nulo_hlm2) 

# In[1.14]: Análise da significância estatística dos efeitos aleatórios de
#intercepto

teste = float(modelo_nulo_hlm2.cov_re.iloc[0, 0]) /\
    float(pd.DataFrame(modelo_nulo_hlm2.summary().tables[1]).iloc[1, 1])

p_value = 2 * (1 - stats.norm.cdf(abs(teste)))

print(f"Estatística z para a Significância dos Efeitos Aleatórios: {teste:.3f}")
print(f"P-valor: {p_value:.3f}")

if p_value >= 0.05:
    print("Ausência de significância estatística dos efeitos aleatórios ao nível de confiança de 95%.")
else:
    print("Efeitos aleatórios contextuais significantes ao nível de confiança de 95%.")

modelo_nulo_hlm2.summary()

#-------------- Modelagem multinível -----------------------------#

# Estimação do modelo nulo (função 'MixedLM' do pacote 'statsmodels')

modelo_nulo_hlm2 = sm.MixedLM.from_formula(formula='delay_minutes ~ 1',
                                           groups='date',
                                           re_formula='1',
                                           data=df_Yearly).fit()
LineVar = modelo_nulo_hlm2.cov_re.iloc[0,0]
scale = modelo_nulo_hlm2.scale
# Intraclasse correlation ICC
ICC_nulo_hlm2 = LineVar / (LineVar + scale)
print("ICC = ") 
print(ICC_nulo_hlm2) 

# In[1.14]: Análise da significância estatística dos efeitos aleatórios de
#intercepto

teste = float(modelo_nulo_hlm2.cov_re.iloc[0, 0]) /\
    float(pd.DataFrame(modelo_nulo_hlm2.summary().tables[1]).iloc[1, 1])

p_value = 2 * (1 - stats.norm.cdf(abs(teste)))

print(f"Estatística z para a Significância dos Efeitos Aleatórios: {teste:.3f}")
print(f"P-valor: {p_value:.3f}")

if p_value >= 0.05:
    print("Ausência de significância estatística dos efeitos aleatórios ao nível de confiança de 95%.")
else:
    print("Efeitos aleatórios contextuais significantes ao nível de confiança de 95%.")

modelo_nulo_hlm2.summary()


# Criação de um cluster entre os dados para ver sea clusterização aumenta a variancia do grupo (Contexto não latente): 
     

#-------------- Modelagem multinível -----------------------------#
# Estimação do modelo nulo (função 'MixedLM' do pacote 'statsmodels')



df_sample = df_Yearly.sample(frac=0.05, replace=True, random_state=1)
modelo_nulo_hlm2 = sm.MixedLM.from_formula(formula='delay_minutes ~ 1',
                                           groups='Month',
                                           re_formula='1',
                                           data=df_sample).fit()


LineVar = modelo_nulo_hlm2.cov_re.iloc[0,0]
scale = modelo_nulo_hlm2.scale
# Intraclasse correlation ICC
ICC_nulo_hlm2 = LineVar / (LineVar + scale)

# In[1.14]: Análise da significância estatística dos efeitos aleatórios de
#intercepto

teste = float(modelo_nulo_hlm2.cov_re.iloc[0, 0]) /\
    float(pd.DataFrame(modelo_nulo_hlm2.summary().tables[1]).iloc[1, 1])

p_value = 2 * (1 - stats.norm.cdf(abs(teste)))

print(f"Estatística z para a Significância dos Efeitos Aleatórios: {teste:.3f}")
print(f"P-valor: {p_value:.3f}")

if p_value >= 0.05:
    print("Ausência de significância estatística dos efeitos aleatórios ao nível de confiança de 95%.")
else:
    print("Efeitos aleatórios contextuais significantes ao nível de confiança de 95%.")

modelo_nulo_hlm2.summary()












    
# dummyzação da variável Line: 
    
# In[3.7]: Outro método de estimação (sugestão de uso para muitas dummies no dataset)



# In[3.5]: Dummizando a variável 'regiao'. O código abaixo automaticamente fará:
# a) o estabelecimento de dummies que representarão cada uma das regiões do dataset;
# b) removerá a variável original a partir da qual houve a dummização;
# c) estabelecerá como categoria de referência a primeira categoria, ou seja,
#a categoria 'America_do_sul' por meio do argumento 'drop_first=True'.

df_dummies = pd.get_dummies(df_Yearly, columns=['line'],
                                      dtype=int,
                                      drop_first=True)


df_dummies.info()


# Definição da fórmula utilizada no modelo
lista_colunas = list(df_dummies.drop(columns=['date','train_id',
 'stop_sequence','from','from_id','to','to_id','scheduled_time','actual_time','delay_minutes','status','type','Data_Pattern','line_encoded','delay_minutes_rounded','actual_time_hours']).columns)

formula_dummies_modelo = ' + '.join(lista_colunas)
formula_dummies_modelo = "delay_minutes ~ " + formula_dummies_modelo
print("Fórmula utilizada: ",formula_dummies_modelo)

# Estimação
modelo_dummies = sm.OLS.from_formula(formula_dummies_modelo,
                                               df_dummies).fit()

# Parâmetros do 'modelo_corrupcao_dummies'
modelo_dummies.summary()










