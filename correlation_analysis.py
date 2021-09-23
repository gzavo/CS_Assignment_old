#%%
import numpy as np
import pandas as pd

data = pd.read_csv("./istherecorrelation.csv", sep=";")
data.set_index("Year", drop=True)
# %%
data.head()
#%%
data.describe()

# %%
