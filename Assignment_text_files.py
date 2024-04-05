# Ask the user to enter the name of a text file to analyze.
def user_input():
    userInput = input('Enter name of the file: ')
    return userInput

user_input()

#Open the file and read its contents.
def open_read_file():
    with open('text_filezz.txt', 'r') as rf:
        rf_contents = rf.read()
        return rf_contents
    
open_read_file()
 

#Count the number of lines in the file and print it.
def line_number():
    with open('text_filezz.txt', 'r') as rf:
        list = []
        for words in rf:
            words.split()
            list.append(words)
            print(list)
            print(len(list))
    
'''
#Count the number of words in the file and print it.
with open('text_filezz.txt', 'r') as rf:
   content = rf.read()
   words = content.split()
   print(len(words))

#Count the number of characters (including whitespace) in the file and print it.
with open('text_filezz.txt', 'r') as rf:
   content = rf.read()
   print(len(content))

#Determine the average word length in the file and print it.
with open('text_filezz.txt', 'r') as rf:
   content = rf.read()
   total_content = len(content)
   print(total_content)

   words = content.split()
   total_words = len(words)
   print(total_words)
   
   print(total_content/total_words)

#Determine the most common word in the file and print it.

from collections import Counter

def most_common_word(filename):
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()
        word_counts = Counter(words)
        most_common = word_counts.most_common(1)
        if most_common:
            return most_common[0][0]
        else:
            return None

filename =  
most_common = most_common_word(filename)
if most_common:
    print(f"The most common word in '{filename}' is: {most_common}")
else:
    print("The file is empty.")


with open('analysis.txt', 'w') as wf:
    wf.write(f'Number of lines : {list}')
    wf.write('Number of words : [193]')
    wf.write('Number of characters : [1125]')
    wf.write('Most common word : []')
    '''