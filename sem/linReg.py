import pandas as pd
from sklearn.linear_model import LinearRegression

# Path to your CSV file
file_path = './GC05cr_h16_tfbs.csv'

# Load the CSV file
df = pd.read_csv(file_path)

varX_df = pd.read_csv('.//varX.csv')


individual_results_varX = {}

# Iterate through each column from 'EE87893ln1' to 'EE87919ln1' in the original dataset
for col in df.loc[:, 'EE87893ln1':'EE87919ln1']:
    # Set the current column as the dependent variable
    y_individual_varX = df[col].values.reshape(-1, 1)

    # Fit the model
    model_individual_varX = LinearRegression()
    model_individual_varX.fit(varX_df, y_individual_varX)

    # Store the coefficients for the current column
    individual_results_varX[col] = model_individual_varX.coef_

# individual_results_varX now contains the coefficients for each regression

print(list(individual_results_varX.keys()))

# print(list(individual_results_varX.values())[0])

# Accessing the coefficients for 'EE87899ln1' from the results
coefficients_ee87899ln1 = individual_results_varX['EE87899ln1']
print(coefficients_ee87899ln1[0])
print(len(coefficients_ee87899ln1[0]))
