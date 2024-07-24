import pandas as pd

# Path to your CSV file
file_path = './GC05cr_h16_tfbs.csv'

# Load the CSV file
df = pd.read_csv(file_path)

# Extracting the columns from 'blood_vessel_h16' to 'urinary_bladder_h16'
extracted_columns = df.loc[:, 'blood_vessel_h16':'urinary_bladder_h16']

# Display the first few rows of the extracted columns
print(extracted_columns.head())

# Path for the new CSV file
output_file_path = './varX.csv'

# Save the extracted columns to the new CSV file
extracted_columns.to_csv(output_file_path, index=False)

print(f"File saved as {output_file_path}")