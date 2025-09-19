
import pyodbc
import pandas as pd
import os
import networkx as nx
import haversine as hs
from haversine import Unit
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.cluster.hierarchy as sch
import scipy.stats as stats
from scipy.stats import zscore
from scipy.spatial.distance import pdist
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import KMeans
import pingouin as pg
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
from ipyleaflet import Map, Marker
from sklearn.cluster import DBSCAN
from sklearn.neighbors import NearestNeighbors
import numpy as np
from sklearn.metrics.pairwise import haversine_distances


new_dir = r"C:\Users\eosjo"
os.chdir(new_dir)


SERVER_NAME = 'ZEC'
DATABASE_NAME = 'NJTransit'
USERNAME = 'sa'
PASSWORD = ''
connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER_NAME};DATABASE={DATABASE_NAME};UID={USERNAME};PWD={PASSWORD}'

connection = pyodbc.connect(connectionString)

# Import into databases all Lines Table info

# 1 - Atl_City_Line_info

sql_query_Atl_City_Line_info = """
      SELECT 
    	[stop_sequence]
          ,[to]
          ,[to_id]
          ,[line]
          ,[type]
    	  ,[NJTransit].[dbo].[Lat_long].[Latitude]
    	  ,[NJTransit].[dbo].[Lat_long].[Longitude]
      FROM [NJTransit].[dbo].[Atl_City_Line_info]
       left Join [NJTransit].[dbo].[Lat_long] 
      ON [NJTransit].[dbo].[Atl_City_Line_info].[to]=[NJTransit].[dbo].[Lat_long].StationName;
    """

df_Atl_City_Line_info = pd.read_sql(
    sql_query_Atl_City_Line_info, connection)

#df_Atl_City_Line_info = df_Atl_City_Line_info.drop_duplicates()

# 2 - Bergen_Co_Line_info

sql_query_Bergen_Co_Line_info = """
      SELECT 
    	[stop_sequence]
          ,[to]
          ,[to_id]
          ,[line]
          ,[type]
    	  ,[NJTransit].[dbo].[Lat_long].[Latitude]
    	  ,[NJTransit].[dbo].[Lat_long].[Longitude]
      FROM [NJTransit].[dbo].[Bergen_Co_Line_info]
       left Join [NJTransit].[dbo].[Lat_long] 
      ON [NJTransit].[dbo].[Bergen_Co_Line_info].[to]=[NJTransit].[dbo].[Lat_long].StationName;
    """

df_Bergen_Co_Line_info = pd.read_sql(
    sql_query_Bergen_Co_Line_info, connection)

#df_Bergen_Co_Line_info = df_Bergen_Co_Line_info.drop_duplicates()

# 3 - Gladstone_Branch_info

sql_query_Gladstone_Branch_info = """
      SELECT 
    	[stop_sequence]
          ,[to]
          ,[to_id]
          ,[line]
          ,[type]
    	  ,[NJTransit].[dbo].[Lat_long].[Latitude]
    	  ,[NJTransit].[dbo].[Lat_long].[Longitude]
      FROM [NJTransit].[dbo].[Gladstone_Branch_info]
       left Join [NJTransit].[dbo].[Lat_long] 
      ON [NJTransit].[dbo].[Gladstone_Branch_info].[to]=[NJTransit].[dbo].[Lat_long].StationName;
    """

df_Gladstone_Branch_info = pd.read_sql(
    sql_query_Gladstone_Branch_info, connection)

#df_Gladstone_Branch_info = df_Gladstone_Branch_info.drop_duplicates()
# 4 - Main_Line_info

sql_query_Main_Line_info = """
      SELECT 
    	[stop_sequence]
          ,[to]
          ,[to_id]
          ,[line]
          ,[type]
    	  ,[NJTransit].[dbo].[Lat_long].[Latitude]
    	  ,[NJTransit].[dbo].[Lat_long].[Longitude]
      FROM [NJTransit].[dbo].[Main_Line_info]
       left Join [NJTransit].[dbo].[Lat_long] 
      ON [NJTransit].[dbo].[Main_Line_info].[to]=[NJTransit].[dbo].[Lat_long].StationName;
    """

df_Main_Line_info = pd.read_sql(sql_query_Main_Line_info, connection)

#df_Main_Line_info = df_Main_Line_info.drop_duplicates()
# 5 - Montclair_Boonton_info

sql_query_Montclair_Boonton_info = """
      SELECT 
    	[stop_sequence]
          ,[to]
          ,[to_id]
          ,[line]
          ,[type]
    	  ,[NJTransit].[dbo].[Lat_long].[Latitude]
    	  ,[NJTransit].[dbo].[Lat_long].[Longitude]
      FROM [NJTransit].[dbo].[Montclair_Boonton_info]
       left Join [NJTransit].[dbo].[Lat_long] 
      ON [NJTransit].[dbo].[Montclair_Boonton_info].[to]=[NJTransit].[dbo].[Lat_long].StationName;
    """

df_Montclair_Boonton_info = pd.read_sql(
    sql_query_Montclair_Boonton_info, connection)

#df_Montclair_Boonton_info = df_Montclair_Boonton_info.drop_duplicates()

# 6 - Morristown_Line_info

sql_query_Morristown_Line_info = """
      SELECT 
    	[stop_sequence]
          ,[to]
          ,[to_id]
          ,[line]
          ,[type]
    	  ,[NJTransit].[dbo].[Lat_long].[Latitude]
    	  ,[NJTransit].[dbo].[Lat_long].[Longitude]
      FROM [NJTransit].[dbo].[Morristown_Line_info]
       left Join [NJTransit].[dbo].[Lat_long] 
      ON [NJTransit].[dbo].[Morristown_Line_info].[to]=[NJTransit].[dbo].[Lat_long].StationName;
    """

df_Morristown_Line_info = pd.read_sql(
    sql_query_Morristown_Line_info, connection)

#df_Morristown_Line_info = df_Morristown_Line_info.drop_duplicates()

# 7 - No_Jersey_Coast_info
sql_query_No_Jersey_Coast_info = """
      SELECT 
    	[stop_sequence]
          ,[to]
          ,[to_id]
          ,[line]
          ,[type]
    	  ,[NJTransit].[dbo].[Lat_long].[Latitude]
    	  ,[NJTransit].[dbo].[Lat_long].[Longitude]
      FROM [NJTransit].[dbo].[No_Jersey_Coast_info]
       left Join [NJTransit].[dbo].[Lat_long] 
      ON [NJTransit].[dbo].[No_Jersey_Coast_info].[to]=[NJTransit].[dbo].[Lat_long].StationName;
    """

df_No_Jersey_Coast_info = pd.read_sql(
    sql_query_No_Jersey_Coast_info, connection)

#df_No_Jersey_Coast_info = df_No_Jersey_Coast_info.drop_duplicates()

# 8 - Northeast_Corrd_info

sql_query_Northeast_Corrd_info = """
      SELECT 
    	[stop_sequence]
          ,[to]
          ,[to_id]
          ,[line]
          ,[type]
    	  ,[NJTransit].[dbo].[Lat_long].[Latitude]
    	  ,[NJTransit].[dbo].[Lat_long].[Longitude]
      FROM [NJTransit].[dbo].[Northeast_Corrd_info]
       left Join [NJTransit].[dbo].[Lat_long] 
      ON [NJTransit].[dbo].[Northeast_Corrd_info].[to]=[NJTransit].[dbo].[Lat_long].StationName;
    """

df_Northeast_Corrd_info = pd.read_sql(
    sql_query_Northeast_Corrd_info, connection)

#df_Northeast_Corrd_info = df_Northeast_Corrd_info.drop_duplicates()

# 9 - Pascack_Valley_info

sql_query_Pascack_Valley_info = """
      SELECT 
    	[stop_sequence]
          ,[to]
          ,[to_id]
          ,[line]
          ,[type]
    	  ,[NJTransit].[dbo].[Lat_long].[Latitude]
    	  ,[NJTransit].[dbo].[Lat_long].[Longitude]
      FROM [NJTransit].[dbo].[Pascack_Valley_info]
       left Join [NJTransit].[dbo].[Lat_long] 
      ON [NJTransit].[dbo].[Pascack_Valley_info].[to]=[NJTransit].[dbo].[Lat_long].StationName;
    """

df_Pascack_Valley_info = pd.read_sql(
    sql_query_Pascack_Valley_info, connection)

#df_Pascack_Valley_info = df_Pascack_Valley_info.drop_duplicates()

# 10 - Princeton_Shuttle_info
sql_query_Princeton_Shuttle_info = """
      SELECT 
    	[stop_sequence]
          ,[to]
          ,[to_id]
          ,[line]
          ,[type]
    	  ,[NJTransit].[dbo].[Lat_long].[Latitude]
    	  ,[NJTransit].[dbo].[Lat_long].[Longitude]
      FROM [NJTransit].[dbo].[Princeton_Shuttle_info]
       left Join [NJTransit].[dbo].[Lat_long] 
      ON [NJTransit].[dbo].[Princeton_Shuttle_info].[to]=[NJTransit].[dbo].[Lat_long].StationName;
    """
df_Princeton_Shuttle_info = pd.read_sql(
    sql_query_Princeton_Shuttle_info, connection)

#df_Princeton_Shuttle_info = df_Princeton_Shuttle_info.drop_duplicates()

# 11 - Raritan_Valley_info
sql_query_Raritan_Valley_info = """
      SELECT 
    	[stop_sequence]
          ,[to]
          ,[to_id]
          ,[line]
          ,[type]
    	  ,[NJTransit].[dbo].[Lat_long].[Latitude]
    	  ,[NJTransit].[dbo].[Lat_long].[Longitude]
      FROM [NJTransit].[dbo].[Raritan_Valley_info]
       left Join [NJTransit].[dbo].[Lat_long] 
      ON [NJTransit].[dbo].[Raritan_Valley_info].[to]=[NJTransit].[dbo].[Lat_long].StationName;
    """

df_Raritan_Valley_info = pd.read_sql(
    sql_query_Raritan_Valley_info, connection)

#df_Raritan_Valley_info = df_Raritan_Valley_info.drop_duplicates()


# 12 - Link between Habok and Penstation

sql_query_Link_info = """
      SELECT 
    	[stop_sequence]
          ,[to]
          ,[to_id]
          ,[line]
          ,[type]
    	  ,[NJTransit].[dbo].[Lat_long].[Latitude]
    	  ,[NJTransit].[dbo].[Lat_long].[Longitude]
      FROM [NJTransit].[dbo].[Link_penst_habok]
       left Join [NJTransit].[dbo].[Lat_long] 
      ON [NJTransit].[dbo].[Link_penst_habok].[to]=[NJTransit].[dbo].[Lat_long].StationName;
    """

df_Link_info = pd.read_sql(
    sql_query_Link_info, connection)


All_dataset_list = [df_Atl_City_Line_info, df_Bergen_Co_Line_info, df_Gladstone_Branch_info, df_Main_Line_info, df_Montclair_Boonton_info, df_Morristown_Line_info,
                    df_No_Jersey_Coast_info, df_Northeast_Corrd_info, df_Pascack_Valley_info, df_Princeton_Shuttle_info, df_Raritan_Valley_info, df_Link_info]
All_dataset = df_Atl_City_Line_info
for dataset in range(2, len(All_dataset_list) + 1):
    All_dataset = pd.concat(
        [All_dataset, All_dataset_list[dataset - 1]], axis=0)

All_dataset = All_dataset.drop_duplicates()
All_dataset = All_dataset.reset_index()

# END of data import


def write_gephi_file(list_graphs):
    i = 0
    for graph in list_graphs:
        i = i + 1
        string = str(i) + ".gexf"
        nx.write_gexf(graph, string + ".gexf")


def density(n_nodes, n_edges):
    return (2*n_edges)/(n_nodes*(n_nodes - 1))


def fill_network(df, lineLabel):

    Graph = nx.Graph()
    maxValue = df['stop_sequence'].max()
    labels = []

    for count in range(1, (int(maxValue) + 1)):
        row_number = df.index.get_loc(
            df[df['stop_sequence'] == count].index[0])
        Node_to_add = df.at[row_number, 'to']
        Graph.add_node(Node_to_add)

        Lat = df.at[row_number, 'Latitude']
        Long = df.at[row_number, 'Longitude']
        key = df.at[row_number, 'to']

      
        nx.set_node_attributes(Graph, {key: Lat}, "Lat")
        nx.set_node_attributes(Graph, {key: Long}, "Long")

    for count in range(2, (int(maxValue) + 1)):
        row_number_first = df.index.get_loc(
            df[df['stop_sequence'] == (count - 1)].index[0])
        first_node = df.at[row_number_first, 'to']
        first_cord = (df.at[row_number_first, 'Latitude'],
                      df.at[row_number_first, 'Longitude'])

        row_number_second = df.index.get_loc(
            df[df['stop_sequence'] == (count)].index[0])
        second_node = df.at[row_number_second, 'to']
        second_cord = (df.at[row_number_second, 'Latitude'],
                       df.at[row_number_second, 'Longitude'])

        distance_km = hs.haversine(
            first_cord, second_cord, unit=Unit.KILOMETERS)
        Graph.add_edge(first_node, second_node, weight=round(distance_km, 1))

    labels.append(lineLabel)
    nx.set_node_attributes(Graph, labels, "line")

    return Graph


# create empty graphs
Graph_Atl_City_Line = fill_network(df_Atl_City_Line_info, 'Atl_City_Line')
Graph_Bergen_Co_Line = fill_network(df_Bergen_Co_Line_info, 'Bergen_Co_Line')
Graph_Gladstone_Branch = fill_network(
    df_Gladstone_Branch_info, 'Gladstone_Branch')
Graph_Main_Line = fill_network(df_Main_Line_info, 'Main_Line')
Graph_Montclair_Boonton = fill_network(
    df_Montclair_Boonton_info, 'Montclair_Boonton')
Graph_Morristown_Line = fill_network(
    df_Morristown_Line_info, 'Morristown_Line')
Graph_No_Jersey_Coast = fill_network(
    df_No_Jersey_Coast_info, 'No_Jersey_Coast')
Graph_Northeast_Corrd = fill_network(
    df_Northeast_Corrd_info, 'Northeast_Corrd')
Graph_Pascack_Valley = fill_network(df_Pascack_Valley_info, 'Pascack_Valley')
Graph_Princeton_Shuttle = fill_network(
    df_Princeton_Shuttle_info, 'Princeton_Shuttle')
Graph_Raritan_Valley = fill_network(df_Raritan_Valley_info, 'Raritan_Valley')
Graph_Link = fill_network(df_Link_info, 'Link')

# nodes

list_of_Graphs = [Graph_Atl_City_Line, Graph_Bergen_Co_Line, Graph_Gladstone_Branch, Graph_Main_Line, Graph_Montclair_Boonton, Graph_Morristown_Line,
                  Graph_No_Jersey_Coast, Graph_Northeast_Corrd, Graph_Pascack_Valley, Graph_Princeton_Shuttle, Graph_Raritan_Valley, Graph_Link]

list_of_Graphs_2 = [Graph_Bergen_Co_Line, Graph_Gladstone_Branch, Graph_Main_Line, Graph_Montclair_Boonton, Graph_Morristown_Line,
                    Graph_No_Jersey_Coast, Graph_Northeast_Corrd, Graph_Pascack_Valley, Graph_Princeton_Shuttle, Graph_Raritan_Valley, Graph_Link]


full_network = Graph_Atl_City_Line
for graph in range(2, len(list_of_Graphs) + 1):
    full_network = nx.compose(full_network, list_of_Graphs[graph - 1])

strongly_connected_network = Graph_Bergen_Co_Line
for graph in range(2, len(list_of_Graphs_2) + 1):
    strongly_connected_network = nx.compose(
        strongly_connected_network, list_of_Graphs_2[graph - 1])


#list_of_Graphs_strongly_connected = []
#Strongly_connected_Network = Graph_Bergen_Co_Line
# for graph in range(2,len(list_of_Graphs) + 1 ):
 #   Strongly_connected_Network = nx.compose(Strongly_connected_Network, list_of_Graphs_strongly_connected[graph - 1])


# edges = [(u, v) for (u, v, d) in full_network.edges(data=True) if d["weight"] > 0]

# pos = nx.spring_layout( full_network, k=0.35, iterations=10)  # positions for all nodes - seed for reproducibility

# # nodes


# nx.draw_networkx_nodes( full_network, pos, node_size=100)

# # edges

# nx.draw_networkx_edges(full_network, pos, edgelist=edges, width=1, alpha=0.5, edge_color="b", style="dashed")

# # node labels
# nx.draw_networkx_labels(full_network, pos, font_size=8, font_family="sans-serif")
# # edge weight labels
# edge_labels = nx.get_edge_attributes(full_network, "weight",)
# nx.draw_networkx_edge_labels(full_network, pos, edge_labels,font_size= 8)

# ax = plt.gca()
# ax.margins(0.08)
# plt.axis("off")
# plt.tight_layout()
# plt.show()


list_of_nodes = list(full_network.nodes)
degrees_list_node = [(node) for (node, val) in full_network.degree()]
degrees_list = [(val) for (node, val) in full_network.degree()]
closeness = nx.closeness_centrality(full_network)
clustering = nx.clustering(full_network)
centrality = nx.betweenness_centrality(full_network, k=10, endpoints=True)


# Elements statics in a full network

df_degree = pd.DataFrame(
    {
        'Station': [node for (node, val) in full_network.degree()],
        'Degree': [val for (node, val) in full_network.degree()],
    })

df_closseness = pd.DataFrame.from_dict(
    closeness, orient='index', columns=['Closseness'])
df_closseness.index.names = ['Station']

df_clustering = pd.DataFrame.from_dict(
    clustering, orient='index', columns=['Clustering'])
df_clustering.index.names = ['Station']

df_centrality = pd.DataFrame.from_dict(
    centrality, orient='index', columns=['Centrality'])
df_centrality.index.names = ['Station']

density_full_network = density(
    full_network.number_of_nodes(), full_network.number_of_edges())

# Not strongly connected graph makes imposible to take those parameters
Average_shortest_path_lenght = nx.average_shortest_path_length(
    strongly_connected_network)
eccentricity = nx.eccentricity(strongly_connected_network)


# Comunity_partition = nx.community.edge_betweenness_partition(G, 2)
# Comunity_partition = nx.community.louvain_communities(full_network, seed=123)

df_Network_info = pd.DataFrame(columns=['Info','Value'])

new_row = pd.DataFrame({'Info':'density', 'Value':density_full_network}, index=[0])
df_Network_info = pd.concat([new_row,df_Network_info.loc[:]]).reset_index(drop=True)

new_row = pd.DataFrame({'Info':'Average shortest path lenght', 'Value':Average_shortest_path_lenght}, index=[0])
df_Network_info = pd.concat([new_row,df_Network_info.loc[:]]).reset_index(drop=True)


new_dir_Gephi = r"C:\Users\eosjo\OneDrive\Área de Trabalho\Filesystem\MBA data science\ProjetoFinalTCC\Gephi"
os.chdir(new_dir_Gephi)

# write into gefx file:
#nx.write_gexf(full_network, "full_network.gexf")
#nx.write_gexf(strongly_connected_network, "strongly_connected_network.gexf")


#exporting all Network analysis dataframes created to CSV files, that are going to be loaded on SQL to better visualization 
new_dir_customDB_results = r"C:\Users\eosjo\OneDrive\Área de Trabalho\Filesystem\MBA data science\ProjetoFinalTCC\Python_Generated_DB"
os.chdir(new_dir_customDB_results)


df_degree.to_csv('degree.csv', index=False)
df_closseness.to_csv('closseness.csv', index=True)
df_clustering.to_csv('clustering_coef.csv', index=True)
df_centrality.to_csv('centrality.csv', index=True)
df_Network_info.to_csv('Network_info.csv', index=True)



####### Clustering at station level using hierarchy aglomerativy method###################
new_dir_Images_clustering = r"C:\Users\eosjo\OneDrive\Área de Trabalho\Filesystem\MBA data science\ProjetoFinalTCC\Cluster"
os.chdir(new_dir_Images_clustering)


# Dendrograma
# Distância euclidiana e método de encadeamento single linkage
# Não existe um critério objetico que nos permita decidir a distância euclidiana entre os clusters
clustering_df = All_dataset[["Latitude", "Longitude"]]



plt.figure(figsize=(40,40))
dend_sing = sch.linkage(clustering_df, method = 'average')
dendrogram_s = sch.dendrogram(dend_sing, color_threshold = 4.5, labels = list(All_dataset.to))
plt.title('Dendrograma', fontsize=16)
plt.xlabel('Estações', fontsize=16)
plt.ylabel('euclidean distance', fontsize=16)
plt.axhline(y = 4.5, color = 'red', linestyle = '--')
plt.show()



# A medida de distância e o método de encadeamento são mantidos
Linkage = 'complete'
for n in range(1, 12):
    cluster_Hier = AgglomerativeClustering(n_clusters = n, linkage = Linkage)
    indica_cluster_Hier = cluster_Hier.fit_predict(clustering_df)
    All_dataset['cluster_Hierarch'] = indica_cluster_Hier
    All_dataset['cluster_Hierarch'] = All_dataset['cluster_Hierarch'].astype('category')



    # Create scatter map clustering Kmeans
    fig = px.scatter_geo(All_dataset, lat='Latitude', lon='Longitude', color='cluster_Hierarch',
                    hover_name='to', title='Map')


    fig.update_layout(
        autosize=True,
        height=600,
        geo=dict(
            center=dict(
                lat=40.730610,
                lon=-73.935242
                ),
            scope='usa',
            projection_scale=8
            )
        )
    fig.show()
    Name = "Newyork_Hierarch_" + Linkage + str(n) + ".png"
    fig.write_image(Name)

# Kmeans clusterization: 
    

elbow = []
K = range(1,15) # ponto de parada pode ser parametrizado manualmente
for k in K:
    kmeanElbow = KMeans(n_clusters=k, init='random', random_state=100).fit(clustering_df)
    elbow.append(kmeanElbow.inertia_)
    
plt.figure(figsize=(16,8))
plt.plot(K, elbow, marker='o')
plt.xlabel('Nº Clusters', fontsize=16)
plt.xticks(range(1,15))
plt.ylabel('WCSS', fontsize=16)
plt.title('Método de Elbow', fontsize=16)
plt.show()


# Considerando o resultado do grafico do método de elbow, podemos usar um valor razoável de 8 clusteres nessa divisãp

kmeans = KMeans(n_clusters=8, init='random', random_state=100).fit(clustering_df)

# Gerando a variável para identificarmos os clusters gerados

kmeans_clusters = kmeans.labels_
All_dataset['cluster_kmeans'] = kmeans_clusters
All_dataset['cluster_kmeans'] = All_dataset['cluster_kmeans'].astype('category')
    

# Create scatter map clustering Kmeans
fig = px.scatter_geo(All_dataset, lat='Latitude', lon='Longitude', color='cluster_kmeans',
                    hover_name='to', title='Map')


fig.update_layout(
    autosize=True,
    height=600,
    geo=dict(
        center=dict(
            lat=40.730610,
            lon=-73.935242
        ),
        scope='usa',
        projection_scale=8
    )
)
fig.show()
fig.write_image("Newyork_Kmeans.png")






# Plot to decide the nearest neybor kneeusing n = 3
nn = NearestNeighbors(n_neighbors=3)
nn.fit(clustering_df)

distances, indices = nn.kneighbors()
sorted_distances = np.sort(distances, axis=0)

fig = plt.figure(figsize=(16,9))
fig.suptitle(" Nearest Neighbour Distance")
ax = fig.add_subplot()
ax.set_xlabel("Observation")
ax.set_ylabel("Distance nearest neighbor")
ax.plot(sorted_distances[:,2])
ax.axhline(y=0.18, linestyle='dashed')
plt.show()



# Create scatter map clustering Dbscan
DBSCAN_clusters = DBSCAN(eps=0.18, min_samples=4,metric='haversine').fit_predict(clustering_df)
All_dataset['cluster_DBscan'] = DBSCAN_clusters
All_dataset['cluster_DBscan'] = All_dataset['cluster_DBscan'].astype('category')


# Create scatter map clustering Kmeans
fig = px.scatter_geo(All_dataset, lat='Latitude', lon='Longitude', color='cluster_DBscan',
                    hover_name='to', title='Map')


fig.update_layout(
    autosize=True,
    height=600,
    geo=dict(
        center=dict(
            lat=40.730610,
            lon=-73.935242
        ),
        scope='usa',
        projection_scale=8
    )
)
fig.show()
fig.write_image("Newyork_DBscan.png")



#exporting all Network analysis dataframes created to CSV files, that are going to be loaded on SQL to better visualization 
new_dir_customDB_results = r"C:\Users\eosjo\OneDrive\Área de Trabalho\Filesystem\MBA data science\ProjetoFinalTCC\Python_Generated_DB"
os.chdir(new_dir_customDB_results)

# all dataset remove duplicates: 
All_dataset = All_dataset.drop_duplicates(subset=['to'])
All_dataset.drop(columns=['index', 'stop_sequence','to_id','line','type','Latitude','Longitude']).to_csv('clustering.csv', index=False)




