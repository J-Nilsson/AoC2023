import sys
import networkx as nx
import matplotlib.pyplot as plt

adj_list = dict()

for line in sys.stdin:
    line = line.strip()
    line = line.split(':')
    key = line[0]
    adj = list(line[1].split())
    adj_list[key] = adj

G = nx.Graph(adj_list)
for k, v in adj_list.items():
    G.add_node(k)
    for n in v:
        G.add_node(n)
nx.draw(G, with_labels = True)
plt.show()