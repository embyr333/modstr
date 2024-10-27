# 5th commit - Another dead end - more than one thing wrong here!

def upper_SQL_keywords(s: str): # Note1
    key_set = ('select', 'from', 'where', 'is') # TODO extend as needed

    # word_list = s.split()
    word_list = s.split('\'')

    print(word_list) # temp check

    # for i in range(0, len(word_list), 2): # only process odd items for uppercase
    # ...on 2nd thoughts if do parity checking in loop instead, can do both uppercasing
    # of odd items and quote-reinstatement for even items in same loop...
    for i in range(0, len(word_list), 2): # only proxcess odd items
        if i % 2 != 0 and word_list[i] in key_set: # only do this for odd items
            word_list[i] = word_list[i].upper()
        else: # for the even items do...
            word_list[i] = '\'' + word_list[i] + '\''
    print(word_list) # temp check

    print(' '.join(word_list))

# Example
upper_SQL_keywords("select first_name, last_name, gender FROM patients where gender is 'M';")
print()
# SELECT first_name, last_name, gender FROM patients WHERE gender IS 'M';

# If query uses single (or no) quotes internally, paste between the single quotes here...
upper_SQL_keywords("select first_name, last_name, gender from patients where gender is 'M is gender';")
# Otherwise can use...
# upper_SQL_keywords('')
# TODO: Consider whether there a better way to deal with this (without making a GUI - may do later)

'''
TODO: Deal with posibility of words from key_set used within a string in query, 
i.e. NOT as keywords, so would NOT want to mod, e.g. 2nd 'is' in the following...
select first_name, last_name, gender from patients where gender is 'M is gender';
[Iteration 4 was dead end with shelx.split() - does not preserve quotation marks]

Note1: Using the optional arg type specifier has the advantage of allowing
IDE to make builtin method suggestions on typing dot after string etc.
'''


