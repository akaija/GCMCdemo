# standard library imports
from math import ceil

# related third party imports
import matplotlib.pyplot as plt
import numpy as np

def draw_lattice_configuration(coordinates, length):
    '''This function draws a two-dimensional lattice configuration, given the coordinates for each
    particle and the size of the lattice.
    '''
    fig = plt.figure()
    ax = plt.subplot(111)

    plt.xlim(0, length)
    plt.ylim(0, length)

    ax.grid(True)

    ax.set_xticks(range(length), minor=False)
    ax.get_xaxis().set_ticklabels([])

    ax.set_yticks(range(length), minor=False)
    ax.get_yaxis().set_ticklabels([])

    ax.plot(coordinates[0] + 0.5, coordinates[1] + 0.5, 'bo', markersize=5, markeredgecolor='none',
        alpha=0.5)

    plt.show()

class Histogram:
    '''Histogram class for tracking particle concentrations in MC simulations.'''
    count = 0
    
    def __init__(self, value_range, increment, output_frequency):
        self.value_range = value_range
        self.increment = increment
        self.output_frequency = output_frequency
        self.count += 1
        
        number_of_bins = ceil((value_range[1] - value_range[0]) / increment)  # determine number of bins
        self.histogram = np.zeros(number_of_bins)                             # set all bins to zero
        self.value_range[1] = value_range[0] + number_of_bins * increment     # adjust range (if needed)
        self.values = range(number_of_bins)                                   # centre the vector-values
        self.values = [value_range[0] + increment * (i - 0.5) for i in self.values]
        
    def add_data(self, data):
        '''Add new data (concentration [frac.]) to histogram.'''
        if data > self.value_range[0] and data <= self.value_range[1]:
            bin_index = ceil((data - self.value_range[0]) / self.increment)
            self.histogram[bin_index] += 1
            self.count += 1
