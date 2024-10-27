# 3rd commit

def upper_SQL_keywords(s: str): # Note1
    key_set = ('select', 'from', 'where', 'is') # TODO extend as needed
    word_list = s.split()
    for i in range(len(word_list)):
        if word_list[i] in key_set:
            word_list[i] = word_list[i].upper()
    print(' '.join(word_list))

# TODO: Try to deal with posibility of words from key_set used within a string in query, 
# i.e. NOT as keywords, so would NOT want to mod, e.g. 2nd 'is' in the following
# select first_name, last_name, gender from patients where gender is 'M is gender';


# Example
upper_SQL_keywords("select first_name, last_name, gender FROM patients where gender is 'M';")
print()
# SELECT first_name, last_name, gender FROM patients WHERE gender IS 'M';

# If query uses single (or no) quotes internally, paste between the single quotes here...
upper_SQL_keywords("")
# Otherwise can use...
upper_SQL_keywords('')
# TODO: Consider whether there a better way to deal with this (without making a GUI - may do later)

# Note1: using the optional arg type specifier has the advantage of allowing
# IDE to make builtin method suggestions on typing dot after string etc.