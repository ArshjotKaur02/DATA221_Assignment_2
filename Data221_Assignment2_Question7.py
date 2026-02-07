"""
Question 7
In this question, you will work on extracting structured content from a webpage using Beautiful-Soup.
Scrape the Wikipedia page:
https://en.wikipedia.org/wiki/Data_science
Write a program using requests and BeautifulSoup that:
• Extracts and prints the page title from the <title> tag.
• Extracts the first paragraph from the main article content inside the div with id mw-content-text.
• The paragraph must contain at least 50 characters (after stripping whitespace).
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
#.find() is used to find the <title> tag
page_title = parsed_html_content.find('title').text

#Getting the article content from div with id 'mw-content-text'
main_article_content = parsed_html_content.find("div", id="mw-content-text")

#Information about .find_all() was referenced from: https://www.geeksforgeeks.org/python/find-the-text-of-the-given-tag-using-beautifulsoup/
#.find_all() is used to get all <p> tags from the main content
main_article_content_paragraph_tags = main_article_content.find_all("p")

first_paragraph_with_at_least_50_characters = ""

#For loop to find the first paragraph that contain at least 50 characters, excluding whitespaces
for current_tag in main_article_content_paragraph_tags:
    paragraph_text = current_tag.text
    #using .strip() to remove leading and trailing whitespaces
    paragraph_text_without_whitespace = paragraph_text.strip()

    #check if the length of the paragraph is at least 50, if yes break out of the loop
    if len(paragraph_text_without_whitespace) >= 50:
        first_paragraph_with_at_least_50_characters = paragraph_text_without_whitespace
        break

#print the output
print(f"The page title is: {page_title}")
print(f"First paragraph with at least 50 characters is: \n{first_paragraph_with_at_least_50_characters}")
