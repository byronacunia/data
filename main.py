import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from RemoveOutliers import RemoveOutliers
#Load the data into a Pandas DataFrame
Year1_df = pd.read_excel('PV_firstRealease.xlsx', sheet_name='Year 1')
Year2_df = pd.read_excel('PV_firstRealease.xlsx', sheet_name='Year 2')
Year3_df = pd.read_excel('PV_firstRealease.xlsx', sheet_name='Year 3')
data_df = pd.concat([Year1_df, Year2_df, Year3_df], ignore_index=True)

columns = ['Generated power', 'TemperatureC', 'DewpointC', 'PressurehPa', 'WindDirectionDegrees', 'WindSpeedKMH', 'WindSpeedGustKMH', 'Humidity', 'HourlyPrecipMM', 'dailyrainMM', 'SolarRadiationWatts_m2']

modified_data_df = RemoveOutliers(data_df, columns)
n_rows = 288
df_chunks = np.array_split(modified_data_df, len(modified_data_df) // n_rows + (len(modified_data_df) % n_rows != 0))
# Iterate over the groups and plot the data
i=0
for group in df_chunks:
    # Plot the 'SolarRadiationWatts_m2' column
    x = np.linspace(0, group.shape[0], group.shape[0])
    plt.scatter(x, group['Generated power'].values)
    plt.scatter(x, group['SolarRadiationWatts_m2'].values)
    plt.scatter(x, group['TemperatureC'].values)
    # plt.hist(group['Generated power'].values)
    plt.xlabel('Sample')
    plt.ylabel('Generated power')
    # group['Generated power'].plot(kind='line')
    plt.title('Solar Generated power in Watts of Hour=' + str(group['Hour'].values[0]))
    # Save the plot
    plt.savefig(str(i) + '.png', dpi=300)
    # Clear the current figure
    plt.clf()
    i+=1