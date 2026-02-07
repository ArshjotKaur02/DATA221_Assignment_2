'''
Question 10
This final question asks you to design a reusable function for searching within text files.
Write a function:
Test the function using sample-file.txt with keyword lorem.
• Print how many matching lines were found.
• Print the first 3 matching lines (line number and text).
'''

#defining the function that takes in filename and keyword as input
#line 12 is from the question
def find_lines_containing(filename, keyword):
    matching_lines = [] #Initilizing the list to store the final output

    # Opening the file for reading its contents (mode = "r")
    file_object  = open(filename, "r")
    #Reading each line using .readlines() and storing it as list of string
    file_content = file_object.readlines()

    # Iterate over each line in the text file
    for current_index in range(0, len(file_content)):
        if file_content[current_index] == "\n":
            # if the current element is a newline character, skip to the next iteration
            continue

        current_line_number = current_index + 1
        current_line_text = file_content[current_index].rstrip("\n")
        # using .rstrip("\n") to remove the newline character at the end of each line

        if keyword.lower() in current_line_text.lower():
            matching_lines.append((current_line_number, current_line_text))

    file_object.close()  # Closing the file after use
    return matching_lines

#calling the function for testing using the sample-file.txt
text_file_name = "sample-file.txt"
keyword = "lorem"

function_output = find_lines_containing(text_file_name, keyword)

# print the length of matching_lines, that is the number of lines that have a match
print(f"Number matching lines are: {len(function_output)}")

# check if the length of the matching_lines list is greater than or equal to 3 i.e., there are at least 3 matches
number_of_matching_lines = 3
if len(function_output) < 3:
    number_of_matching_lines = len(function_output)

# using nested for loop to iterate over each element in the list and then accessing the line number and text
for current_list_index in range(0, number_of_matching_lines):
    current_list_element = function_output[current_list_index]
    print(f"{current_list_element[0]} -> {current_list_element[1]}")



