import pandas as pd
#Load the data into a Pandas DataFrame
Year1_df = pd.read_excel('PV_firstRealease.xlsx', sheet_name='Year 1')
#Compute the mean and standard deviation of the data
mean = Year1_df['SolarRadiationWatts_m2'].mean()
std = Year1_df['SolarRadiationWatts_m2'].std()

#Identify anomalies as values that are more than 3 standard deviation from the mean
print('Mean = ', mean)
print('Std = ', std)
#print(Year1_df.describe())
print(Year1_df.columns)
print("Fin")