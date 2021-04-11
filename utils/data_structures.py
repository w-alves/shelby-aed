import numpy as np

class MinHeap:
    def __init__(self):
        self.array = [0]
        self.current_size = 0
 
    def sift_up(self, i):
        while i // 2 > 0:
            if self.array[i][1] < self.array[i // 2][1]:
                self.array[i], self.array[i // 2] = self.array[i // 2], self.array[i]
            i = i // 2
 
    def insert(self, k):
        self.array.append(k)
        self.current_size += 1
        self.sift_up(self.current_size)

    def min_child(self, i):
        if (i * 2)+1 > self.current_size:
            return i * 2
        else:
            if self.array[i*2][1] < self.array[(i*2)+1][1]:
                return i * 2
            else:
                return (i * 2) + 1
 
    def sift_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.array[i][1] > self.array[mc][1]:
                self.array[i], self.array[mc] = self.array[mc], self.array[i]
            i = mc
 
    def delete_min(self):
        if len(self.array) == 1:
            return None
 
        root = self.array[1]
 
        self.array[1] = self.array[self.current_size]
        self.array.pop()
        self.current_size -= 1
        self.sift_down(1)
 
        return root

class Graph:
    def __init__(self, adjacency_list, n):
        self.graph =  adjacency_list
        self.vertices = n

    def minimal_path(self, start, end):
        distances = {k: np.inf for k in range(self.vertices)}
        distances[start] = 0
        previous = [-1]*self.vertices

        distance_from_source = MinHeap()
        distance_from_source.insert((start, 0))

        element = distance_from_source.delete_min()
        while element:
            node, dist = element
            if node == end:
                break
            
            if dist <= distances[node]:
                for adjnode, length_to_adjnode in self.graph[node]:
                    new_dist = dist + length_to_adjnode
                    
                    if distances[adjnode] > new_dist:
                        previous[adjnode], distances[adjnode] = node, new_dist
                        distance_from_source.insert((adjnode, new_dist))

            element = distance_from_source.delete_min()

        path_list = []
        vertex = end
        while vertex != -1:
            path_list.append(vertex)
            vertex = previous[vertex]
        path_list.reverse()
        
        path_list = list(map(str, path_list))

        return distances[end], path_list