import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

fnamet1 = './test1.frag.tsv.bed'
fname = './first_10000_rows.tsv'
# Load the data
data = pd.read_csv(fname, sep='\t', header=None)
data.columns = ['Chromosome', 'Start', 'End', 'NumFragments']

# Determine the range for our x-axis intervals
min_val = data['Start'].min() // 100 * 100  # floor to nearest hundred
max_val = data['End'].max() // 100 * 100 + 100  # ceil to nearest hundred

# Generate the x-axis intervals
intervals = list(range(min_val, max_val, 100))

# Initialize an array to store the density values for each interval
densities = np.zeros(len(intervals) - 1)

# Calculate the density for each interval
for i in range(len(intervals) - 1):
    start_interval = intervals[i]
    end_interval = intervals[i+1]
    
    # Filter data rows that intersect with the current interval
    intersecting_rows = data[(data['Start'] < end_interval) & (data['End'] > start_interval)]
    
    for _, row in intersecting_rows.iterrows():
        start_data_interval = max(row['Start'], start_interval)
        end_data_interval = min(row['End'], end_interval)
        
        spanned_intervals = np.ceil((end_data_interval - start_data_interval) / 100.0)
        increment = 1.0 / spanned_intervals
        
        densities[i] += increment

highestDen = np.max(densities)
# print(densities)
# print(highestDen)

# # Plotting
# plt.figure(figsize=(10, 6))
# plt.bar(intervals[:-1], densities, width=100, align='edge')
# plt.xlabel('Intervals')
# plt.ylabel('Density')
# plt.ylim(0, 35 )
# plt.title('Interval Density Graph')
# # newIntervals = list(range(min_val, max_val, 5000))
# plt.xticks(intervals, rotation=45)
# plt.tight_layout()
# plt.show() 

column_names = [f'{i}-{i+100}' for i in range(min_val, max_val - 100, 100)]
df = pd.DataFrame([densities], columns=column_names)

# sns.heatmap(df)
# plt.show() 
