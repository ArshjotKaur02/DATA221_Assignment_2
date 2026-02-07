"""
Question 5
Here you will create a new categorical variable and generate a grouped summary table.
Using student.csv:
• Create a new column grade_band:
    – Low: grade ≤ 9
    – Medium: grade 10–14
    – High: grade ≥ 15
• Create a grouped summary table showing for each band:
    – number of students
    – average absences
    – percentage of students with internet access
• Save the table as student_bands.csv.
"""

import pandas

#student.csv is located in the same directory
#loading the data into data fram using pandas package
student_data_dataframe = pandas.read_csv("student.csv")

#Information on creating conditional column was referenced from: https://stackoverflow.com/questions/21702342/creating-a-new-column-based-on-if-elif-else-condition

#If the data in the grade column of student_data_dataframe is <= 9, then create a column grade_band equal to "low"
student_data_dataframe.loc[student_data_dataframe["grade"] <= 9, "grade_band"] = "Low"

#If the data in the grade column of student_data_dataframe is between 10 and 14, then create a column grade_band equal to "medium"
student_data_dataframe.loc[(student_data_dataframe["grade"] >= 10) & (student_data_dataframe["grade"] <= 14), "grade_band"] = "Medium"

#If the data in the grade column of student_data_dataframe is >= 15, then create a column grade_band equal to "high"
student_data_dataframe.loc[student_data_dataframe["grade"] >= 15, "grade_band"] = "High"

#Information on grouping dataframe by column .groupby() method was referenced from: https://stackoverflow.com/questions/46464718/summarize-dataframe-by-grouping-on-a-column-with-pandas
#.groupby() creates a groups based on grade_band column
#.agg() computes summary calculations
# number_of_students column counts the number of students in each group
# average_absences computes the 'mean' of absences per group
# percentage_of_students_with_internet_access computes the 'mean' since the values are either i or 0, then multiplied by 100
summary_by_grade_band_dataframe = student_data_dataframe.groupby("grade_band").agg(
    number_of_students = ("grade", "count"),
    average_absences =("absences", "mean"),
    percentage_of_students_with_internet_access = ("internet", "mean"))

#Multipling the percentage column with 100 to convert the values into percentages(0.4444 -> 44.44)
summary_by_grade_band_dataframe["percentage_of_students_with_internet_access"] *= 100

# Converting the data frame to a csv file
# Information on .to_csv() was referenced from: https://stackoverflow.com/questions/16923281/writing-a-pandas-dataframe-to-csv-file
summary_by_grade_band_dataframe.to_csv("student_bands.csv")



