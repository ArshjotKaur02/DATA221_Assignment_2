"""
Question 4
This question involves filtering tabular data and saving the results to a new file.
Using student.csv:
• Load the dataset into a DataFrame.
• Filter students where studytime ≥ 3, internet = 1, and absences ≤ 5.
• Save the filtered data to high_engagement.csv.
• Print the number of students saved and their average grade.
"""

import pandas

#student.csv is located in the same directory
#loading the data into data fram using pandas package
student_data_dataframe = pandas.read_csv("student.csv")

#Filter students to only include students that have studytime ≥ 3, internet = 1, and absences ≤ 5
#Using '&' operator to check conditions for all three columns
high_engagement_student_dataframe = student_data_dataframe[
    (student_data_dataframe["studytime"] >= 3) &
    (student_data_dataframe["internet"] == 1) &
    (student_data_dataframe["absences"] <= 5)]

#Converting the data frame to a csv file
# Information on .to_csv() was referenced from: https://stackoverflow.com/questions/16923281/writing-a-pandas-dataframe-to-csv-file
high_engagement_student_dataframe.to_csv("high_engagement.csv", index=False)

#using len() to get the number of high engagement students
number_of_students_saved = len(high_engagement_student_dataframe)
#using .mean() to calculate the mean of grades column
average_grade_of_students_saved = high_engagement_student_dataframe["grade"].mean()

print(f"Number of high engagement students: {number_of_students_saved}")
print(f"Average grade of high engagement students: {average_grade_of_students_saved:.02f}")





