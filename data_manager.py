import numpy as np
import zarr


class DataManager:
    def __init__(self):
        self.__data = None

    def load_data(self, path):
        self.__data = np.array(zarr.open(path, mode='r')["C"])

    def interval_split_data(self, interval_length):
        num_neurons = self.__data.shape[0]
        length_time_series = self.__data.shape[1]
        return np.resize(self.__data, (length_time_series // interval_length, num_neurons, interval_length))

    @property
    def data(self):
        return self.__data
