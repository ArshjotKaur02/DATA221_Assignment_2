"""
Question 3
In this task, you will identify lines that are nearly identical after basic normalization.
Two lines are considered near-duplicates if they become identical after converting to lower-case and removing all whitespace and punctuation characters.
Using sample-file.txt:
• Identify sets of near-duplicate lines.
• Print the number of such sets.
• Print the first two sets you find, including line numbers and original lines.
"""

#Variable to store file name
#Since file is located in the same directory, path is not used
text_file_name = "sample-file.txt"

#Opening the file for reading its contents (mode = "r")
file_object = open(text_file_name, "r")
#Reading the entire file line by line using .readlines() and storing it as list of strings
file_content = file_object.readlines()

#Dictionary to store normalized line as key and values are the list of tuples containing number and line text
dictionary_of_normalized_lines = {}

#Iterate over each line in the text file
for current_index in range(0, len(file_content)):
    if file_content[current_index] == "\n":
        #if the current element is a newline character, skip to the next iteration
        continue

    current_line_number = current_index + 1
    current_original_line = file_content[current_index].rstrip("\n") #using .rstrip("\n") to remove the newline character at the end of each line
    current_line_text = current_original_line.lower() #.lower() to convert the line text to lowercase

    normalized_line_text = ""
    #iterate over each character in the line and check if its alphabet using .isalpha()
    #Information about .isalnum() method was referenced from: https://www.geeksforgeeks.org/python/python-string-isalnum-method/
    #If the character is an alphabet/number, add it to the normalized_line_text string
    for current_character_index in range(0, len(current_line_text)):
        if current_line_text[current_character_index].isalnum():
            normalized_line_text += current_line_text[current_character_index]

    #store the line number and text in the dictionary. The lines are grouped based on normalized_line_text
    #if the current normalized text already exist as a key, append the tuple of line number and text
    if normalized_line_text in dictionary_of_normalized_lines:
        dictionary_of_normalized_lines[normalized_line_text].append((current_line_number, current_original_line))
    else: #else, add a new key with normalized text as key and a list of tuple containing line number and text as value
        dictionary_of_normalized_lines[normalized_line_text] = [(current_line_number, current_original_line)]


#initilizing the new list to store the list of tuples that have at least one match
list_of_duplicate_lines = []

#iterate over all the keys in the dictionary
for key in dictionary_of_normalized_lines:
    if len(dictionary_of_normalized_lines[key]) >= 2:
        # if the length of the current key's value is 2, that is the current line text have at least one match, append it to the list
        list_of_duplicate_lines.append(dictionary_of_normalized_lines[key])


#print the length of list_of_duplicate_lines, that is the number of lines that have at least one match
print(f"Number of near duplicate set of lines are: {len(list_of_duplicate_lines)}")

#check if the length of the list_of_duplicate_lines is greater than or equal to 2 i.e., there are at least 2 matches
number_of_sets_being_printed = 2
if len(list_of_duplicate_lines) < 2:
    number_of_sets_being_printed = len(list_of_duplicate_lines)

#using nested for loop to iterate over each element in the list and then accessing the line number and text using double index [r][c]
for current_list_index in range(0, number_of_sets_being_printed):
    current_list_element = list_of_duplicate_lines[current_list_index]
    for current_tuple_index in range(0, len(current_list_element)):
        #Printing only the first two sets
        print(f"{current_list_element[current_tuple_index][0]} -> {current_list_element[current_tuple_index][1]}")

file_object.close() #closing the text file after use



