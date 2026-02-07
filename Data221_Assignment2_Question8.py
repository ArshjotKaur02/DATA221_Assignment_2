"""
Question 8
This task focuses on extracting structured heading information from a webpage.
Using the same Wikipedia page:
https://en.wikipedia.org/wiki/Data_science
• Extract all <h2> section headings from the main content area (div with id mw-content-text).
• Do not include headings containing the words: References, External links, See also, or Notes.
• Remove any [edit] text from headings.
• Save the headings to headings.txt, one per line, in order.
"""

import requests
from bs4 import BeautifulSoup

site_url = "https://en.wikipedia.org/wiki/Data_science"

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
#.find_all() is used to get all h2 heading from the main content
h2_heading_tags = main_article_content.find_all("h2")

#list of heading that must be excluded from the output
excluded_words = ["references", "external links", "see also", "notes"]

#initilizing a new list to store valid heading
required_headings = []

#For loop to iterate over each h2 tag in the main content
for current_tag in h2_heading_tags:
    #Using .replace() to ensure [edit] text is removed from headings
    current_heading = current_tag.text.replace("[edit]", "")
    #.strip() to remove any whitespaces
    current_heading = current_heading.strip()

    #Check if the current heading has a word in the list of excluded words, if yes skip to the next iteration
    if any((word in current_heading.lower()) for word in excluded_words):
        continue
    #else, append it to the required_headings list along with newline character
    else:
        required_headings.append(current_heading + "\n")

#variable to store the name of the output file
output_file_name = "headings.txt"

#using 'w' to write to the file
file_object = open(output_file_name, 'w')
#using .writelines() that takes in the list of strings to write it to the file
file_object.writelines(required_headings)

file_object.close() #Closing the file after use



