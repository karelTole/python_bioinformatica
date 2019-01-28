

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter
from networkx.algorithms.community import k_clique_communities
from operator import itemgetter




#load file (DM-LC)
df = pd.read_csv('DM-LC.txt',  sep= '\s+', header = None)
#df = pd.read_table('DM-LC.txt', header= None)
df.head()

#Q1. Create network (g) with Networkx
g = nx.Graph()
for i in range(len(df)):
    node=df.loc[i,:][0] # first column as node
    next_node=df.loc[i,:][1]# first column as  node
    weight=df.loc[i,:][2] # third column as edge cost/weight
    g.add_weighted_edges_from([(node,next_node,weight)])
    #print(node,next_node,weight) 
    

#position nodes 
pos = nx.spring_layout(g)

#calculate betweeness centrality 
betCent = nx.betweenness_centrality(g, normalized=True, endpoints=True)

#node color varies with Degree
node_color = [20000.0 * g.degree(v) for v in g] 

# node size varies with betweeness centrality
node_size =  [v * 10000 for v in betCent.values()]

#create figure
plt.figure(figsize=(20,20))
nx.draw_networkx(g, pos=pos, with_labels=False, node_color=node_color, node_size=node_size)
plt.axis('off')

#another way to draw graph
G = nx.read_weighted_edgelist('DM-LC.txt')
nx.draw(G,  node_size=10)

#Q2. Compute number of nodes, number of edges and the average degree of the network
network_info = nx.info(g)
print(network_info)
#n,k = g.order(), g.size()
#av_degree = 2*float(k)/n
#print(av_degree)



#another solution
print('No. of nodes: ', nx.number_of_nodes(g))
print('No. of edeges: ', nx.number_of_edges(g))


degrees = [deg for (node, deg) in nx.degree(g)]  # The degrees of each node
avg_degree = sum(degrees) / float(len(degrees))
print('Average degree: ', avg_degree )
print("Average degree: ", 2 * nx.number_of_edges(g) / nx.number_of_nodes(g))

#Q3. Compute the density of the network
density = nx.density(g)
print("Network density:", density)

T = nx.minimum_spanning_tree(g)
print(nx.info(T))
#list(T.edges(data=False))
pos = nx.spring_layout(T)
plt.figure(figsize=(20,20))
nx.draw_networkx(T, pos=pos, with_labels=False,
                 node_color='b',
                 node_size= 30 )
plt.axis('off')

T = nx.minimum_spanning_tree(g)
print(nx.info(T))
#list(T.edges(data=False))
pos = nx.spring_layout(T)
plt.figure(figsize=(20,20))
nx.draw_networkx(T, pos=pos, with_labels=False,
                 node_color='b',
                 node_size= 30 )
plt.axis('off')

#lsit the components in network (g)
components = nx.connected_components(g)

#compare among components and find the one having maximun length(LC)
largest_component = max(components, key=len)
#largest_component

# Q1.draw LC
subgraph = g.subgraph(largest_component)
pos = nx.spring_layout(subgraph) # force nodes to separte 
betCent = nx.betweenness_centrality(subgraph, normalized=True, endpoints=True)
node_color = [20000.0 * g.degree(v) for v in subgraph]
node_size =  [v * 10000 for v in betCent.values()]
plt.figure(figsize=(20,15))
nx.draw_networkx(subgraph, pos=pos, with_labels=False,
                 node_color=node_color,
                 node_size=node_size)
plt.axis('off')

diameter = nx.diameter(subgraph)
print("Diameter of LC:", diameter)

#Q3.compute center
center = nx.center(subgraph)
print('Center of LC: ', center)

cli_num = list(k_clique_communities(subgraph,3))
print('clique communities with 3 nodes: ', len(cli_num))


#claculates eigenvector centrality in  LC
eigen_cent = nx.eigenvector_centrality(subgraph)
#sorted_eigen=sorted(eigen_cent, key=eigen_centrality.get)
sorted_eigen =sorted(eigen_cent.items(), key=itemgetter(1), reverse=True)
sorted_eigen[1][0]

degree_cent = nx.algorithms.degree_centrality(subgraph)
sorted_degree = sorted(degree_cent.items(), key=itemgetter(1), reverse=True)
sorted_degree[1][0]

