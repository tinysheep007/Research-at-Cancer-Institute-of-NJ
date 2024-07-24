import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# File paths
input_file = './EE87915.frag.tsv.bed'
output_file = './10000sample5fromEE87915.tsv'

# Read the file
data_subset = pd.read_csv(input_file, sep='\t', header=None, nrows=10000)

# Write the first 10,000 rows to a new .tsv file
data_subset.to_csv(output_file, sep='\t', header=None, index=False)

output_file