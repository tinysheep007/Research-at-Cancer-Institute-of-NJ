import numpy as np
import pandas as pd
# from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from scipy import stats

# content = []
# with open("test1.frag.tsv.bed")as f:
#     for line in f:
#         content.append(line.strip().split())
# content  = np.asarray(content)
# print(content)


# Read TSV file into DataFrame
cols = ["chr1","var1", "var2","var3"]
df = pd.read_table('test1.frag.tsv.bed', names=cols)
# print(df)

# lin regression
x = df["var1"]
y = df["var2"]
    
slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show() 

# multiple regression
# mymodel = np.poly1d(np.polyfit(x, y, 3))
# myline = np.linspace(1, 22, 100)
# plt.scatter(x, y)
# plt.plot(myline, mymodel(myline))
# plt.show() 