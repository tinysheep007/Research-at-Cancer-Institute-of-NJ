from scipy.stats import zscore
import pandas as pd

# Load your data (assuming it's in an Excel file)
data_xlsx = pd.read_excel('resultFromSample123.xlsx')

# Applying Z-score normalization (excluding the first identifier column)
normalized_data = data_xlsx.iloc[:, 1:].apply(zscore)

# Saving the normalized data to a new Excel file
normalized_data.to_excel('normalized123.xlsx', index=False)
