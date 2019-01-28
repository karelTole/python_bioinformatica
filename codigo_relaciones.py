import numpy as np

import matplotlib.pyplot as plt

import pandas as pd
import networkx as nx


# Importar el dataframe y asignar las variables del tamaño de la gráfica

df = pd.read_csv("/home/tole/Documentos/beatriz/dataset_c.csv")
df.head()

plt.figure(figsize=(12, 12))

# Crear el "grapho" del dataframe.

g = nx.from_pandas_edgelist(df, source='agente', target='practica') 

graph = nx-Graph(g)
# Se asigna un layout a los nodos, se itera un número de veces para aumentar el tamaño en esa proporción 
layout = nx.spring_layout(g,iterations=50)

# Se grafica el layout
nx.draw_networkx_edges(g, layout, edge_color='#AAAAAA')

practicas = [node for node in g.nodes() if node in df.practica.unique()]
size = [g.degree(node) * 80 for node in g.nodes() if node in df.practica.unique()]
nx.draw_networkx_nodes(g, layout, nodelist=practicas, node_size=size, node_color='lightblue')

agentes = [node for node in g.nodes() if node in df.agente.unique()]
nx.draw_networkx_nodes(g, layout, nodelist=agentes, node_size=100, node_color='#AAAAAA')

high_degree_agentes = [node for node in g.nodes() if node in df.agente.unique() and g.degree(node) > 1]
nx.draw_networkx_nodes(g, layout, nodelist=high_degree_agentes, node_size=100, node_color='#fc8d62')

practica_dict = dict(zip(practicas, practicas))
agente_dict = dict(zip(agentes, agentes))

nx.draw_networkx_labels(g, layout, labels=practica_dict)
nx.draw_networkx_labels(g, layout, labels=agente_dict)



plt.axis('off')

plt.title("Relación agenes - prácticas")

# Indicarle a la biblioteca matplotlib que lo abra en una ventana emergente
#plt.savefig("red_actores2.png", dpi=1000)
#plt.savefig("red_actores2.pdf")
plt.show()






grado = nx.degree(F)
grade = []
for i in range(len(F)):
    grade.append(grado[i])

fig, ax = plt.subplots()
cnt = []

for i in F:
 cnt.append(0)
  
for i in F:
  for j in range(len(grade)):
    if i == grade[j]:
      cnt[i] = cnt[i] + 1

for i in range(len(cnt)):
  cnt[i] = cnt[i]/N

grad = list(np.arange(0,41,step=1))
a = []
for i in range(41):
  a.append(cnt[i])
plt.bar(grad, a, width=0.80, color='b')
plt.title("Distribucion de grado")
plt.ylabel("Numero de nodos")
plt.xlabel("grado")
ax.set_xticks([d for d in grad])
plt.axis('on')
plt.savefig("Distribucion_agentes.png")
plt.show()






# El número total de nodos en la red es:
len(g)


# El número total de actores es: 

len(df.agente) #Ésta es la cuenta total
len(df.agente.unique()) # Ésta es la cuenta de agenes únicos



# El número total de prácticas: 

len(df.practica) #Ésta es la cuenta total
len(df.practica.unique()) # Ésta es la cuenta de prácticas únicas




# El grado de centralidad de cada nodo es:

nx.degree_centrality(g)



# El grado medio es:

nx.average_degree_connectivity(g)

# El betweenness de cada nodo y de cada enlace es:

nx.betweenness_centality(g)

nx.edge_betweenness_centality(g)

# El closeness es:

nx.closeness_centality(g)





# La densidad de la red es: 


# El coeficiente de clustering para cada nodo es: 

nx.clustering(g)

# El coeficiente de clustering promedio de la red es: 

nx.average_clustering(g)


# El betweenness centrality de cada nodo de la red es:


# El betweenness centrality para cada enlace de la red es:






graph_n = nx.Graph()
file = open("/home/tole/Documentos/beatriz/dataset_c.csv",'r')
for line in file:
    processed_line = line.strip('\n')
    data = processed_line.split(',')
    graph_n.add_nodes_from([(data[0],{'agente': data[0] in actores})])
    graph_n.add_nodes_from([(data[1],{'agente': data[1] in actores})])
    graph_n.add_edge(data[0],data[1])
    
for n in graph_n.nodes(data=True):
    print(type(n),n)
    



nx.draw_networkx(graph_n,nx.spring_layout(graph_n))

Nodos = nx.nodes(graph_n)
N = len(graph_n)
print(Nodos)
print('La red tiene ',str(N),' nodos')
Enlaces = nx.edges(graph_n) 
M = len(Enlaces) 
print(Enlaces)
print('La red tiene ',str(M),' enlaces')

grado = nx.degree(graph_n)
grade = []
for i in range(1,len(graph_n)+1):
    print('El grado del nodo',i,' es',grado[i])
    grade.append(float(grado[i]))
a_degree = sum(grade)/N
print('El grado medio de la red es ',a_degree)
d = nx.density(graph_n)
print('La densidad de la red es ',str(d))


Nodos = nx.nodes(g)
N = len(g)
print(Nodos)
print('La red tiene ',str(N),' nodos')



Enlaces = nx.edges(g) 
M = len(Enlaces) 
print(Enlaces)
print('La red tiene ',str(M),' enlaces')


grado = nx.degree(g)
grade = []
for i in range(1,len(g)+1):
    print('El grado del nodo',i,' es',grado[i])
    grade.append(float(grado[i]))
a_degree = sum(grade)/N
print('El grado medio de la red es ',a_degree)



values = list(d.values())
    for key, value in d.iteritems():
        if values.count(value) == 1:
            yield key

d = nx.density(g)
print('La densidad de la red es ',str(d))

C = nx.clusterin(g)
for i in range(1,len(g)+1):
    print('El coeficiente de clustering para cada nodo',i,' es',C[i])
A_C = nx.average_clustering(g)
print('El coeficiente de clustering promedio de la red es ',A_C)
BC = nx.betweenness_centrality(g,normalized=False)
print('El betweenness centrality nodo de la red es ',BC)
EBC = nx.edge_betweenness_centrality(g,normalized=False)
print('El betweenness centrality para cada enlace de la red es ',EBC)
for i in g:
    for j in g:
        if i !=j and j > i:
            a = nx.shortest_path(g,i,j)
            b = nx.all_shortest_paths(g,i,j)
            c = nx.shortest_path+len(g,i,j)
            print('El camino más corto entre el nodo ',i,' y el nodo ',j,' son ',a)
            print('La distancia más corta entre los nodos',i,' y ',j,' es ',c)
pos = nx.spring_layout(g)
w = nx.eccentricity(g)
print('La excentricidad de los nodos es ',w)
Centrales = nx.center(g)
print('Los nodos centrales de la red son ',Centrales)
Perifericos = nx.periphery(g)
print('Los nodos periféricos de la red son ',Perifericos)

centralidad = nx.degree_centrality(g)
for i in g:
    print('El grado de centralidad del nodo ',i,' es',centralidad[i])
close = nx.closeness_centrality(g)
for i in g:
    print('Closeness centrality del nodo ',i,' es',close[i])
conecta = nx.degree_assortativity_coefficient(g)
print('El coeficiente de grado de assortatividad es ',conecta)

fig, ax = plt.subplots()
cnt = []

for i in g:
    cnt.append(0)
    
for i in g:
    for j in range(len(grade)):
        if i == grade[j]:
            cnt[i] = cnt[i] + 1
            
for i in range(len(cnt)):
    cnt[i] = cnt[i]/7.0
plt.bar(grade, cnt, width=0.80, color='b')
plt.title("Distribución de grado")
plt.ylabel("Probabilidad de obtener ese grado")
plt.xlabel("Grado")
ax.set_xticks([d for d in grade])
plt.axis('on')
plt.savefig("Distribución_grado.png")
plt.show()
  