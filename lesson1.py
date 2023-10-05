import numpy as np
import pandas as pd
print("Version: " + pd.__version__)

# url = 'https://github.com/mattharrison/datasets/raw/master/data/ames-housing-dataset.zip'
url = 'data/ames-housing-dataset.zip'
df = pd.read_csv(url, engine='pyarrow', dtype_backend='pyarrow')
print("\nShape")
print(df.shape)
print("\nHead")
print(df.head())

print(df
 .select_dtypes('string')
 .memory_usage(deep=True)
 .sum()
)