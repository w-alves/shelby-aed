import time
import random
import numpy as np
import networkx as nx
from utils.data_structures import Graph, MinHeap
from utils.datagen import DataGenerator

test_cases = [(random.randint(1, 2538), random.randint(1, 2538)) for _ in range(1000)]

start = time.time()

data = open("src/data.tsv", 'r')
g = nx.DiGraph()
graph = nx.read_weighted_edgelist(data, nodetype=int, create_using=g)
data.close()

distances_networkx = []
paths_networkx = []
for _from, _to in test_cases:
    previous, dist = nx.dijkstra_predecessor_and_distance(graph, _from)
    if _to in dist:
        dist = dist[_to]
        distances_networkx.append(dist)
        path, vertex = [],  [_to]
        while len(vertex) > 0:
            path.append(vertex[0])
            vertex = previous[vertex[0]]
        path.reverse()
        paths_networkx.append(list(map(str, path)))
    else:
        dist = np.inf
        distances_networkx.append(dist)
        paths_networkx.append([str(_to)])

end = time.time()

print('WALLTIME NETWORKX:', end - start)


start = time.time()
datagen = DataGenerator('src/data.tsv')
adjacency_list, n = datagen.get_data()
network = Graph(adjacency_list, n)

distances_shelby = []
paths_shelby = []
for _from, _to in test_cases:
    dist, path = network.minimal_path(_from, _to)
    distances_shelby.append(dist)
    paths_shelby.append(path)
end = time.time()

print('WALLTIME SHELBY:', end - start)

all_samples = len(distances_networkx)
print('\nVALIDATING MINIMAL DISTANCES |', end=' ')
correct_dist = sum(np.array(distances_networkx) == np.array(distances_shelby))
print(f'TEST PASSEDS: {correct_dist}/{all_samples}')

print('VALIDATING MINIMAL PATHS |', end= ' ')
correct_path = sum(np.array(paths_networkx, dtype=object) == np.array(paths_shelby, dtype=object))
print(f'TEST PASSEDS: {correct_path}/{all_samples}')

if correct_dist == all_samples and correct_path != all_samples:
    print("\nWARNING: THE 'INCORRECT' MINIMAL PATHS ARE BECAUSE THERE IS NOT ONLY A SINGLE WHOSE DISTANCE IS THE SHORTEST BETWEEN TWO PEOPLE.")
    