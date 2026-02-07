"""
Question 6
In this question, you will create a simple category based on crime levels and compare unemployment rates between the groups.
Using crime.csv:
• Load the dataset into a pandas DataFrame.
• Create a new column called risk based on ViolentCrimesPerPop:
– If ViolentCrimesPerPop is greater than or equal to 0.50, set risk = "High-Crime".
– Otherwise, set risk = "LowCrime".
• Group the data by the risk column.
• For each group, calculate the average value of PctUnemployed.
• Print the average unemployment rate for both HighCrime and LowCrime groups in a clear format.
"""

import pandas

#student.csv is located in the same directory
#loading the data into data fram using pandas package
crime_data_dataframe = pandas.read_csv("crime.csv")

#Information on creating conditional column was referenced from: https://stackoverflow.com/questions/21702342/creating-a-new-column-based-on-if-elif-else-condition
#If the data in the ViolentCrimesPerPop is >= 0.50, then create a column risk equal to "HighCrime". Else, risk equal "LowCrime"
crime_data_dataframe.loc[crime_data_dataframe["ViolentCrimesPerPop"] >= 0.50, "risk"] = "HighCrime"
crime_data_dataframe.loc[crime_data_dataframe["ViolentCrimesPerPop"] < 0.50, "risk"] = "LowCrime"

#Information on grouping dataframe by column .groupby() method was referenced from: https://stackoverflow.com/questions/46464718/summarize-dataframe-by-grouping-on-a-column-with-pandas
#.groupby() creates a groups based on risk column
#.agg() computes summary calculations
# average_unemployment_rate computes the 'mean' of data in PctUnemployed column per group
summary_by_risk_dataframe = crime_data_dataframe.groupby("risk").agg(
    average_unemployment_rate =("PctUnemployed", "mean"))

#Print the average by group rounded to 5 decimel places
print(f"Average Unemployment Rate for High Crime Group is: {summary_by_risk_dataframe.loc['HighCrime', 'average_unemployment_rate']:.5f}")
print(f"Average Unemployment Rate for Low Crime Group is: {summary_by_risk_dataframe.loc['LowCrime', 'average_unemployment_rate']:.5f}")

