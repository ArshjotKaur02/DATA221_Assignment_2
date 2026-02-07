"""
Question 9
In this question, you will extract tabular data from a webpage and store it in a structured format.
Scrape the Wikipedia page:
https://en.wikipedia.org/wiki/Machine_learning
• Locate the first table inside the main content area (div with id mw-content-text) that
contains at least 3 data rows.
• Extract the table header from <th> tags if present; otherwise create headers named col1, col2, col3, etc.
• Some rows may have fewer columns than others; pad missing values with empty strings.
• Save the extracted table to wiki_table.csv.
"""

import requests
from bs4 import BeautifulSoup
import csv

site_url = "https://en.wikipedia.org/wiki/Machine_learning"

#Line 20 to 23 is from CPSC 217 course content
#Wikipedia did not allow accessing the website directly without the browser information

headers = {"User-Agent":
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
               "AppleWebKit/537.36 (KHTML, like Gecko) "
               "Chrome/124.0.0.0 Safari/537.36"}

#store the full html content from the website in site_content variable using .get()
# .text saves the html as string
site_content_html = requests.get(site_url, headers=headers).text

#Using BeautifulSoup() to parse the html
parsed_html_content = BeautifulSoup(site_content_html, "html.parser")

#Information about .find() was referenced from: https://www.geeksforgeeks.org/python/find-the-text-of-the-given-tag-using-beautifulsoup/
#Getting the article content from div with id 'mw-content-text'
main_article_content = parsed_html_content.find("div", id="mw-content-text")

#Information about .find_all() was referenced from: https://www.geeksforgeeks.org/python/find-the-text-of-the-given-tag-using-beautifulsoup/
#.find_all() is used to get all tables from the main content
table_content = main_article_content.find_all("table")

first_table_with_at_least_three_rows = ""
#for loop to iterate over each table in the main content
for current_table in table_content:
    count_of_data_rows = 0 #variable to store the number of data cells in the table
    for row in current_table.find_all("tr"):
        #iterate over each row in the table to check how many rows have a data cell. if yes, increase the count by 1
        if row.find("td"):
            count_of_data_rows += 1

    #check the count of table row (<tr>) that have data cell(s) (<td>) to ensure that the extracted table contains at least 3 data rows
    if count_of_data_rows >= 3:
        #if the condition is met, break out of the loop as soon as the first valid table is found
        first_table_with_at_least_three_rows = current_table
        break
#using .findall() to get table row data
targeted_table_rows = first_table_with_at_least_three_rows.find_all("tr")

# Initializing the list to store table headers
table_headers = []
#using for loop to find the first row that contains <th> tag to get the headers
for current_row in targeted_table_rows:
    header_cell_content = current_row.find_all("th")

    #using conditionals to check if the table has any <th> tags. If yes, use it as headers
    if len(header_cell_content) > 0:
        for header in header_cell_content:
            #information on .get_text(strip=True) was reference from: http://stackoverflow.com/questions/13637911/elegant-way-to-safely-text-strip-in-beautifulsoup
            #.get_text() is used to just extract the text inside the tags
            # strip = True removes any whitespace from the test
            table_headers.append(header.get_text(strip=True))
        break #break out of the loop once the headers are found

# Initializing the list to store data rows
table_data_rows = []

#Using for loop to iterate through each row in the table and extract the data (<td> tags)
for current_row in targeted_table_rows:
    data_cell_content = current_row.find_all("td")
    # If the current row does not have and td tags continue to the next iteration
    if not data_cell_content:
        continue

    current_row_content = []
    for content in data_cell_content:
        # using .get_text() to just extract the text inside the tags
        # using strip = True to remove extra whitespaces and " " to concatenates the text from separate tags by adding space in between
        # Example: Paradigms Supervised learning vs. ParadigmsSupervised learning

        # Information on separator (" ") was referenced from: https://www.educative.io/answers/how-to-use-gettext-in-beautiful-soup
        current_row_content.append(content.get_text(" ", strip = True))
    table_data_rows.append(current_row_content)

# Initializing the variable to store the maximum number of columns in the table
maximum_number_of_columns = 0

# Using for loop to check the maximum number of columns required
#This is to pad missing values with empty strings for rows that have fewer columns
for current_row in table_data_rows:
    if len(current_row) > maximum_number_of_columns:
        maximum_number_of_columns = len(current_row)

#if the table does not have any headers, col1, col2, col3... is used as headers
if len(table_headers) == 0:
    for i in range(maximum_number_of_columns): #Create the headers that matches the maximum number of columns
        table_headers.append(f"col{i+1}")

#Using for loop to iterate over all data rows in the table
for current_row in table_data_rows:
    #check is the length of the current row is less than the maximum number of columns
    #If no, append empty strings to the list of row data until the length matches (padding missing values)
    while len(current_row) < maximum_number_of_columns:
        current_row.append("")

with open("wiki_table.csv", "w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerow(table_headers)
    writer.writerows(table_data_rows)



