import math
import numpy as np
import statistics
import pandas as pd

values = [1,4,4,3,2,7,2]

print("Average\t", statistics.average(values))
print("MD\t", statistics.meanDeviation(values))
print("Count 7\t", statistics.count(values, 7))
print("Length\t", statistics.length(values))
print("Max\t", statistics.max(values))
print("Min\t", statistics.min(values))
print("Range\t", statistics.range(values))
print("Sum\t", statistics.sum(values))
print("Sort\t", statistics.sort(values))
print("Variance", statistics.variance(values))
print("SD\t", statistics.standardDeviation(values))
print("Median\t", statistics.median(values))
