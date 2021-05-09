
import pandas as pd

dataFilename = "../../data/All_three_exp_conditions_4.csv"
data = pd.read_csv(dataFilename, index_col=0)

print(data.head)
# Index    Expt_#  Cell_# Speed     ...  Region    Layer Cell_Type
# 0           1       1  -7.072485  ...     SUB      NaN      Wide
# 1           1       1 -14.089136  ...     SUB      NaN      Wide
# 2           1       1 -20.994557  ...     SUB      NaN      Wide
# 3           1       1 -27.734234  ...     SUB      NaN      Wide
# 4           1       1 -34.254958  ...     SUB      NaN      Wide
# ...       ...     ...        ...  ...     ...      ...       ...
# 71755      17      13  79.123708  ...    RSPg  Layer 6      Wide
# 71756      17      13  77.979147  ...    RSPg  Layer 6      Wide
# 71757      17      13  76.218968  ...    RSPg  Layer 6      Wide
# 71758      17      13  73.857066  ...    RSPg  Layer 6      Wide
# 71759      17      13  70.912087  ...    RSPg  Layer 6      Wide

print(data.columns.values)
# 'Expt #' 'Cell #' 'Speed' 'Spike Rate' 'Trial Condition' 'Region' 'Layer' 'Cell Type'

trialConditions = data.loc[:, "Trial Condition"].unique()
print(trialConditions)
# ['Vestibular' 'VisVes' 'Visual']

regions = data.loc[:, "Region"].unique()
print(regions)
# ['SUB' nan 'V1' 'SC' 'RSPg' 'RSPd']

