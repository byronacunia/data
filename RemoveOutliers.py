import pandas as pd
import numpy as np
def RemoveOutliersbyCol(data, col):
    # Group the Year1_df DataFrame by the 'Hour' column
    groups = data.groupby(['Hour', 'Starting minute (inclussive)'])
    # Iterate through the groups and print the group name and the number of unique rows in each group.
    df_modified = list()
    for name, group in groups:
        # Compute the median value of each column
        median = group.median()
        # Replace all zeros in the selected columns with the corresponding median value
        group = group.replace(0, median)
        # Calculate the median of the 'Generated power' column
        median = group[col].median()
        # Calculate the interquartile range (IQR) of the data
        q75, q25 = np.percentile(group[col], [75, 25])
        iqr = q75 - q25
        # Set the upper and lower bounds for the outliers
        upper_bound = median + 3 * iqr
        lower_bound = median - 3 * iqr

        # Replace the outliers with the upper and lower bounds
        group[col] = group[col].clip(lower=lower_bound, upper=upper_bound)
        # Replace the remaining outliers with the median value
        group[col] = group[col].where(group[col].notna(), median)
        data.update(group)
    return data
def RemoveOutliers(data, columns):
    for col in columns:
        modified_data = RemoveOutliersbyCol(data, col)
    return modified_data
