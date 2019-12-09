import numpy as np # numerical computing 
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt #visualization
import seaborn as sns #modern visualization`

sns.set_style("darkgrid")
plt.rcParams['figure.figsize'] = (14, 8)

file_path = 'C:\\Users\\shubham \\Downloads\\'
matches = pd.read_csv(file_path+'matches.csv')

matches.shape
(636, 18)