# 4th commit - Dead end (see end Note1)!

import shlex # Note1

def upper_SQL_keywords(s: str): # Note2
    key_set = ('select', 'from', 'where', 'is') # TODO extend as needed
    word_list = shlex.split(s)
    # print(word_list) # temp check
    for i in range(len(word_list)):
        if word_list[i] in key_set:
            word_list[i] = word_list[i].upper()
    print(' '.join(word_list))


# Example
upper_SQL_keywords("select first_name, last_name, gender FROM patients where gender is 'M';")
print()
# SELECT first_name, last_name, gender FROM patients WHERE gender IS 'M';

# If query uses single (or no) quotes internally, paste between the single quotes here...
upper_SQL_keywords("select first_name, last_name, gender from patients where gender is 'M is gender';")
# Otherwise can use...
upper_SQL_keywords('')
# TODO: Consider whether there a better way to deal with this (without making a GUI - may do later)

'''
Note1: To deal with posibility of words from key_set used within a string in query, 
i.e. NOT as keywords, so would NOT want to mod, e.g. 2nd 'is' in the following...
select first_name, last_name, gender from patients where gender is 'M is gender';
...using shlex.split() instead of string's split() to preserve quoted substrings. Thanks to folks at 
https://stackoverflow.com/questions/79968/split-a-string-by-spaces-preserving-quoted-substrings-in-python
Update: bah, just realised that the quote characters themselves are lost!

Note2: Using the optional arg type specifier has the advantage of allowing
IDE to make builtin method suggestions on typing dot after string etc.
'''

