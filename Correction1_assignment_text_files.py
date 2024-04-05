from collections import Counter

def analyze_text(filename):
    try:
        # Open the file and read its content
        with open(filename, 'r') as file:
            content = file.read()

            #Count the number of lines, words and characters
            num_lines = content.count('\n') + 1
            num_words = len(content.split())
            num_chars = len(content)

            #Calculate the average word length
            words = content.split()
            for word in words:
                total_word_length = sum(len(word))
                avg_word_length = total_word_length/num_words

            '''
            #Find the most common word
            word_counts = Counter(words)
            
            most_common_word = word_counts.most_common(1)[0][0]
           '''
            #Write analysis results to a new file
            with open('analysis.txt', 'w') as wf:
                wf.write(f'Number of lines: {num_lines}\n')
                wf.write(f'Number of words: {num_words}\n')
                wf.write(f'Number of characters: {num_chars}\n')
                wf.write(f'Average word length: {avg_word_length}\n')
               # wf.write(f'Most common word: {most_common_word}\n')

            print('Analysis complete.Results written to `analysis.txt`')


    except FileNotFoundError:
        print('Error: File not Found')

    except Exception as e:
        print(f'An error occured: {e}')

def main():
    filename = input('Enter the name of the text file to analyze: ')
    analyze_text(filename)

if __name__ =='_ _ main_ _':
    main()

main()

            
