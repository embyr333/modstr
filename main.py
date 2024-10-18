# Iteration8

def upper_SQL_keywords(s: str): # Note1
    if s == '':
        print("\nPlease paste the query string you want to process into the final line of code")
        return

    key_set = ('select', 'from', 'where', 'is', 'and', 'null') # TODO continue to extend as needed



    # ---Iteration8: adding...
    semicolon = False
    if s[-1] == ';':
        semicolon = True
        s = s[:-1]



    sections = s.split('\'') # odd sections will be non-quoted items; Note2
    odd_sections = [sections[i] for i in range(len(sections)) if i % 2 == 0] # index is even for odds
    even_sections = [sections[i] for i in range(len(sections)) if i % 2 != 0] # index is odd for evens

    for i in range(len(odd_sections)):
        words = odd_sections[i].split()
        for j in range(len(words)):
            if words[j] in key_set:
                words[j] = words[j].upper()
        odd_sections[i] = ' '.join(words)

    # Combine (processed) odd sections into new list with (unprocessed) evens...
    new_list = []
    for i in range(len(odd_sections)):
        new_list.append(odd_sections[i])
        if i < len(even_sections):
            new_list.append('\'' + even_sections[i] + '\'') # ...adding back quote marks*
    new_string = ' '.join(new_list)



    # ---Iteration8: replacing this...
    # If there is a semicolon at end, remove the extra space that has now been introduced (though not essential)
    # if new_string[-1] == ';' and new_string[-1] == ' ': 
    #     new_string = new_string[:-2] + new_string[-1]
    # ...and adding this...
    if semicolon == True:
        new_string = new_string.rstrip() + ';'



    print(new_string) # (*joining on quote mark here would be problematic as need extra space upstream or downstream)


print('Example1') 
upper_SQL_keywords("select first_name, last_name, gender FROM patients where gender is 'M';")
# SELECT first_name, last_name, gender FROM patients WHERE gender IS 'M';

print('\nExample2: a value in quotation marks has a word from keyword that should not be processed as a keyword') 
upper_SQL_keywords("select first_name, last_name, gender from patients where gender is 'M is gender';")
# SELECT first_name, last_name, gender FROM patients WHERE gender IS 'M is gender';
print()

print('Example3 - keyword adjacent to (terminal) semicolon') 
upper_SQL_keywords("select first_name, last_name from patients where allergies is null;")
# ---Iteration8: had discovered bug with above input - the null is not uppercased
# ...realised because it is adjacant to the semicolon
# ...might be best to just remove any (terminal) semicolon at the beginning then add back
# (then would no need the new final processing step to remove the extra space added), --> did
# TODO: Also, should consider if want to allow processing of muliple lines...

print('Example4 (no semicolon)') 
upper_SQL_keywords("select first_name, last_name from patients where allergies is null")

# Paste input between the (double) quotes here...
upper_SQL_keywords("")

# TODO: Further test cases will be tried as I use it (and of course add further items to key_set)
# TODO: Consider making a GUI

'''
Note1: Using the optional arg type specifier has the advantage of allowing
IDE to make builtin method suggestions on typing dot after string etc.

Note2: Much of the code is dealing with posibility of words from key_set used within a string in query, 
i.e. NOT as keywords, so would NOT want to mod, e.g. 2nd 'is' in the following...
select first_name, last_name, gender from patients where gender is 'M is gender';
[Iteration 4 was dead end with shelx.split() - does not preserve quotation marks]
The whole thing is now rather messy, with some (inefficient) string concatenation, 
and might be better tried with regex, but this approach is probably good enough for now.
'''

