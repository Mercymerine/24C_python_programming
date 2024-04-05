'''
import re

pattern = r"\d{3}-\d{3}-\d{4}"

text = 'I love Kenya and I love being black 123-456-7890' #+254

match = re.search(pattern, text)

print(match)

if match:
    print(f'I found the pattern: {pattern}')

else:
    print('Pattern not found.')
    '''
import re

# Write a function called extract_phone_numbers(string) that takes in a string and returns a list of all the phone numbers present in the string in the format (XXX) XXX-XXXX
def extract_phone_numbers(string):
    pattern = '\(\d{3}\) \d{3}-\d{4}'

    matches = re.findall(pattern, string)

    print (matches)

extract_phone_numbers("Please contact info@example.com for assistance. Phone: (123) 456-7890 or (111) 222-3333")

# Write a function called extract_email_addresses(string) that takes in a string and returns a list of all the email addresses present in the string.
def extract_email_addresses(string):
    pattern = '[a-zA-Z0-9]*@[a-zA-Z-0-9]*.com'

    matches = re.findall(pattern, string)

    print (matches)

extract_email_addresses('"Please contact info@example.com for assistance. Phone: (123) 456-7890 or (111) 222-3333')

#Write a function called replace_email_addresses(string, replacement) that takes in a string and a replacement string, and replaces all email addresses in the given string with the replacement string.
def replace_email_addresses(string, replacement):
    pattern = '[a-zA-Z0-9]*@[a-zA-Z-0-9]*.com'
    
    replaced_string =  re.sub(pattern, replacement, string)

    print (replaced_string)

replace_email_addresses('Please contact info@example.com for assistance.', 'REPLACEMENT')

