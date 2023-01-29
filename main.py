import numpy as np

list = np.random.rand(10)
print(f'Random numbers: {list}')

mean = np.mean(list)
median = np.median(list)
standard_deviation = np.std(list)

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Standard Deviation: {standard_deviation}")