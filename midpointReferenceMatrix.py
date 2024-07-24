import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import NMF

# Loading the data from the TSV file
# data_1 = pd.read_csv("./first_10000_rows.tsv", sep="\t")

# data_1.columns = ["Chromosome", "Start_Position", "End_Position", "Count_or_Label"]
# Displaying the first few rows of the dataset
# print(data_1.head())

# Loading the GenpromTxA data from the TSV file
genpromTxA_data = pd.read_csv("./GenpromTxA.tsv", sep="\t")

# # Displaying the first few rows of the dataset
# # print(genpromTxA_data.head())

# # Create a list to hold the counts for each TSS interval
# counts = []

# # Iterate over each TSS interval and count how many intervals from data_1 fall within it
# for _, row in genpromTxA_data.iterrows():
#     start, end = row['start'], row['end']
#     count = len(data_1[(data_1['Start_Position'] >= start) & (data_1['End_Position'] <= end)])
#     counts.append(count)

# # Convert the counts list to a DataFrame (matrix) format
# matrix = pd.DataFrame([counts], columns=["TSS" + str(i+1) for i in range(len(counts))])

# print(matrix)

sample_files = ['./10000sample1fromEE87919.tsv',
                './10000sample2fromEE87918.tsv',
                './10000sample3fromEE87917.tsv', 
                './10000sample4fromEE87916.tsv',
                './10000sample5fromEE87915.tsv']

# sample_files = ['./EE87917.frag.tsv.bed',
#                 './EE87918.frag.tsv.bed',
#                 './EE87919.frag.tsv.bed']

def create_overlap_matrix(sample_files, tss_data):
    """
    Create a matrix of overlaps between blood sample intervals and TSS intervals.

    Parameters:
    - sample_files (list): A list of filenames for the blood sample data.
    - tss_data (DataFrame): The DataFrame containing the TSS intervals.

    Returns:
    - DataFrame: A matrix where each row represents a blood sample and each column corresponds to a TSS interval.
    """
    all_counts = []

    for sample_file in sample_files:
        # Load the blood sample data
        blood_sample = pd.read_csv(sample_file, sep="\t")
        blood_sample.columns = ["Chromosome", "Start_Position", "End_Position", "Count_or_Label"]

        # Calculate the mean position of each interval in the blood sample
        blood_sample['Mean_Position'] = (blood_sample['Start_Position'] + blood_sample['End_Position']) / 2

        counts = []
        for _, row in tss_data.iterrows():
            tss_start, tss_end = row['start'], row['end']
            # Count how many means fall within the current TSS interval
            count = ((blood_sample['Mean_Position'] >= tss_start) & (blood_sample['Mean_Position'] <= tss_end)).sum()
            counts.append(count)
        
        all_counts.append(counts)

    # Convert the counts to a DataFrame format
    matrix = pd.DataFrame(all_counts, index=sample_files, columns=["TSS" + str(i+1) for i in range(len(counts))])
    return matrix

# make our matrix
m = create_overlap_matrix(sample_files, genpromTxA_data)


sns.heatmap(m)
plt.show()

# print out matrix
# print(m)

# # Initialize NMF with n_components
# nmf = NMF(n_components=5, init='random', random_state=42)

# # Apply NMF
# W = nmf.fit_transform(m)
# H = nmf.components_

# print("M: ", W)

# print("  "," ")

# print("H: ", H)
