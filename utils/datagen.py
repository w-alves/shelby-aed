from collections import defaultdict
import numpy as np

class DataGenerator():
    def __init__(self, path):
        self.data_path = path

    def get_data(self):
        """
        Run the pipeline to read/process the data and return adjacency list.
        """
        data = self._get_input()
        adjacency_list = self._to_adjacency_list(data)
        num_vertex = self._get_uniques(data)

        return adjacency_list, num_vertex

    def _get_input(self):
        """
        Read the input data and return a dataframe with the data.
        """
        with open(self.data_path, 'r') as f:
            data = f.read()
            
        return data

    def _to_adjacency_list(self, data):
        """
        Process the data and return a adjacency list.
        """
        adjacency_list = defaultdict(list)

        for line in data.split('\n'):
            id_from, id_to, weight = list(map(int, line.split()))
            adjacency_list[id_from].append((id_to, weight))
        
        return adjacency_list

    def _get_uniques(self, data):
        """
        Return the number of unique vertices on the graph.
        """
        unique_values = set()
        for line in data.split('\n'):
            id_from, id_to, weight = list(map(int, line.split()))
            unique_values.add(id_from)
            unique_values.add(id_to)

        return len(unique_values)