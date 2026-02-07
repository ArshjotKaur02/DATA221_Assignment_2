"""
Question 2
In this question, you will analyze pairs of consecutive words (called bigrams) from a text file.
Using sample-file.txt:
• Read the file and split it into tokens (words).
• Convert all tokens to lowercase.
• Remove punctuation characters from the beginning and end of each token.
• Keep only tokens that contain at least two alphabetic characters.
• Construct bigrams (pairs of consecutive cleaned words).
• Count the frequency of each bigram.
• Print the 5 most frequent bigrams in descending order in the format: word1 word2 -> count.
"""
#code matches question 1 for line 15 to 53 and line 69 to 95

import string
#Variable to store file name
#Since file is located in the same directory, path is not used
text_file_name = "sample-file.txt"

#Opening the file for reading its contents (mode = "r")
file_object = open(text_file_name, "r")
#Reading the entire file using .read() and storing it as string
file_content = file_object.read()

#The text stored as a sting is split into individual words using the space
list_of_raw_words_from_text = file_content.split()

list_of_clean_valid_words = [] #list created to store words that meets the requirements

#Using for loop to iterate over all the extracted words from the text file
for current_word in list_of_raw_words_from_text:
    lowercase_version_of_word = current_word.lower() # .lower() to convert each word to lowercase

    #Information on .strip(string.punctuation) was referenced from: https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string
    #Using string.punctuation method to remove punctuation characters
    cleaned_version_of_word = lowercase_version_of_word.strip(string.punctuation)

    #Initialize a variable to store the length of the current word
    number_of_alphabetic_characters = 0

    #Using for loop to get the length of the word since the requirement is to only count 'alphabetic characters'
    for character_in_word in cleaned_version_of_word:

        # Check if the character is an alphabet using .isalpha()
        # Information about .isalpha() method was referenced from: https://www.geeksforgeeks.org/python/python-string-isalpha-method/
        if character_in_word.isalpha():
            # If yes, increase the count of alphabetic characters by one
            number_of_alphabetic_characters += 1

        #check if the word contains at least two alphabetic characters
    if number_of_alphabetic_characters >= 2:
        # if yes, append it to the list of valid words
        list_of_clean_valid_words.append(cleaned_version_of_word)

#Initilizing a list to store pairs of consecutive valid words
list_of_bigrams = []

#For loop iterate over each element in the list
#Using len() - 1 to stop when the last 2 words are left
#using current index and index +1 to get 2 consecutive words
for current_index in range(0, (len(list_of_clean_valid_words) - 1)):
    first_word_of_bigram = list_of_clean_valid_words[current_index]
    second_word_of_bigram = list_of_clean_valid_words[(current_index + 1)]

    #using + for string concatenation
    current_bigram = first_word_of_bigram + " " + second_word_of_bigram
    list_of_bigrams.append(current_bigram)

#Initilizing a dictionary to store word count as key-value pair
dictionary_of_bigram_frequencies = {}

# For loop to iterate over each valid word
for current_valid_word in list_of_bigrams:

    # Check if the word (key) already exists in the dictionary. If yes increase its count by 1
    if current_valid_word in dictionary_of_bigram_frequencies:

        dictionary_of_bigram_frequencies[current_valid_word] += 1
    # else, add the key to the dictionary with count equal 1
    else:
        dictionary_of_bigram_frequencies[current_valid_word] = 1

#information on using key = lambda to sort dictionary by values was referenced from: https://www.geeksforgeeks.org/python/python-sort-python-dictionaries-by-key-or-value/
#using reverse = True to arrange the dictionary in descending order
sorted_list_of_word = sorted(dictionary_of_bigram_frequencies.items(), key = lambda item:item[1], reverse = True)

#Since sorting a dictionary returns a list of tuple, using slicing to get the first 5 words (upto index 4)
top_5_most_frequent_bigram = sorted_list_of_word[0:5]

#iterating overall each bigram to print it in the "word1 word2 -> count" form in descending order
for current_word in top_5_most_frequent_bigram:
    print(f"{current_word[0]} -> {current_word[1]} ", end = "")
    #using end = "" to remove new line character

file_object.close() #closing the text file after use
