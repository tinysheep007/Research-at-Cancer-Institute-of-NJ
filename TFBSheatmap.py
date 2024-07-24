import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Reading the newly created CSV file
df_tfbs = pd.read_csv("TFBS.csv")

# # Heatmap for unnormalized data 
# # Generating a heatmap
# plt.figure(figsize=(12, 9))
# sns.heatmap(df_tfbs, cmap='viridis')
# plt.title('Heatmap of Selected Columns')
# plt.show()



# Normalizing the dataset by columns
scaler_column = MinMaxScaler()
df_normalized_columns = pd.DataFrame(scaler_column.fit_transform(df_tfbs), columns=df_tfbs.columns)

# Generating a heatmap for the column-normalized data
plt.figure(figsize=(12, 9))
sns.heatmap(df_normalized_columns, cmap='viridis')
plt.title('Heatmap of Column Normalized Data')
plt.show()