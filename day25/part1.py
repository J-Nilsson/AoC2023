import sys
import networkx as nx
import matplotlib.pyplot as plt

adj_list = dict()

edges_remove = {
    ('fpg', 'ldl'),
    ('dfk', 'nxk'),
    ('lhn', 'hcf')
}

for line in sys.stdin:
    line = line.strip()
    line = line.split(':')
    key = line[0]
    adj = set(line[1].split())
    if key not in adj_list.keys():
        adj_list[key] = set()
    adj_list[key].update(adj)
    for n in adj:
        if n not in adj_list.keys():
            adj_list[n] = set()
        adj_list[n].update({key})

for e in edges_remove:
    adj_list[e[0]].discard(e[1])
    adj_list[e[1]].discard(e[0])

for k in adj_list.keys():
    node = k
    break

visited = set()
q = [node]
while q:
    cur_node = q.pop(0)
    for n in adj_list[cur_node]:
        if n in visited:
            continue
        visited.add(n)
        q.append(n)
s1 = len(visited)

for k in adj_list.keys():
    if k not in visited:
        node = k
        break

visited = set()
q = [node]
while q:
    cur_node = q.pop(0)
    for n in adj_list[cur_node]:
        if n in visited:
            continue
        visited.add(n)
        q.append(n)
s2 = len(visited)

print(s1 * s2)