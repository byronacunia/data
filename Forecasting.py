import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#Load the data into a Pandas DataFrame
Year1_df = pd.read_excel('PV_firstRealease.xlsx', sheet_name='Year 1')

#Group the Year1_df DataFrame by the 'Hour' column
groups = Year1_df.groupby(['Hour', 'Starting minute (inclussive)'])

#Iterate through the groups and print the group name and the number of unique rows in each group.
for name, group in groups:
    print(name, group.shape[0])
    #Calculate the Z-score of each data point


    # Calculate the median of the 'Generated power' column
    median = group['Generated power'].median()

    # Compute the mean and standard deviation of the data
    mean = group['Generated power'].mean()
    std = group['Generated power'].std()
    print('Median = ', median)
    print('Mean = ', mean)
    print('Std = ', std)

    # Calculate the interquartile range (IQR) of the data
    q75, q25 = np.percentile(group['Generated power'], [75, 25])
    iqr = q75 - q25
    # Set the upper and lower bounds for the outliers
    upper_bound = median + 3 * iqr
    lower_bound = median - 3 * iqr
    print('upper_bound = ', upper_bound)
    print('lower_bound = ', lower_bound)

    # Replace the outliers with the upper and lower bounds
    group['Generated power'] = group['Generated power'].clip(lower=lower_bound, upper=upper_bound)
    # Replace the remaining outliers with the median value
    group['Generated power'] = group['Generated power'].where(group['Generated power'].notna(), median)

    # Plot the 'SolarRadiationWatts_m2' column
    x = np.linspace(0, group.shape[0], group.shape[0])
    plt.scatter(x, group['Generated power'].values)
    #plt.hist(group['Generated power'].values)
    plt.xlabel('Sample')
    plt.ylabel('Generated power')
    #group['Generated power'].plot(kind='line')
    plt.title('Solar Generated power in Watts of Hour='+str(name))
    # Save the plot
    plt.savefig(str(name)+'.png',dpi=300)
    # Clear the current figure
    plt.clf()


print(Year1_df.columns[0])
print("Fin")