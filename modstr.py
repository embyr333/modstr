# 19th commit - added ability to process multiple statements 
# (as deliniated by semi-colons)

# TODO: Write a README file


def upper_SQL_keywords(s: str): # Note1
    if s == '':
        return 'Please enter the query string you want to process'

    key_set = ('add', 'all', 'alter', 'and', 'any', 'as', 'asc', 'backup', 'between', 'by', 'case', 'check', 
               'column', 'constraint', 'create', 'database', 'default', 'delete', 'desc', 'distinct', 'drop', 
               'exec', 'exists', 'foreign', 'from', 'full', 'group', 'having', 'in', 'index', 'inner', 
               'insert', 'into', 'is', 'join', 'key', 'left', 'like', 'limit', 'not', 'or', 'order', 'outer', 
               'primary', 'procedure', 'replace', 'right', 'rownum', 'select', 'set', 'table', 'top', 
               'truncate', 'union', 'unique', 'update', 'values', 'view', 'where'
               ) 
    
    fn_set = ('sum', 'avg', 'count', 'min', 'max', 'ucase', 'lcase', 'mid', 'length', 'round', 'now', 'format', 
              'curdate', 'curtime', 'sysdate', 'current_date', 'current_time', 'day', 'month', 'year', 'hour', 
              'minute', 'second', 'date_format', 'ifnull', 'isnull', 'concat', 'replace', 'substring', 'trim', 
              'ltrim', 'rtrim', 'coalesce', 'left', 'right', 'ascii', 'char_length', 'instr', 'locate', 'strpos', 
              'substring_index', 'find_in_set', 'lower', 'upper', 'abs', 'acos', 'asin', 'atan', 'ceiling', 
              'floor', 'mod', 'rand', 'sign', 'sqrt', 'pow', 'truncate', 'log', 'exp', 'pi', 'degrees', 
              'radians', 'sin', 'cos', 'tan', 'cot'
              )

    # Log input linebreaks to be restored at end of prcessing; Note6
    linebreak_indices = []
    for i in range(len(s)):
        if s[i] == '\n':
            linebreak_indices.append(i)
    # print(linebreak_indices) # temp check (I see a linebreak is indeed added at end)

    # semicolon = False
    # if s[-1] == ';':
    #     semicolon = True
    #     s = s[:-1]
    # ---now processing semicolons in process_statements() instead, and provsionally 
    # adding unconditionally if absent (see Note7)
    
    sections = s.split('\'') # odd sections will be non-quoted items; Note2
    odd_sections = [sections[i] for i in range(len(sections)) if i % 2 == 0] # index is even for odds
    even_sections = [sections[i] for i in range(len(sections)) if i % 2 != 0] # index is odd for evens

    for i in range(len(odd_sections)):
        words = odd_sections[i].split()
        for j in range(len(words)):
            word = words[j] 
            if word in key_set:
                word = word.upper()
            elif word.__contains__('('):  
                p_index = word.index('(')
                if word[:p_index] in fn_set: # Note5
                    word = word[:p_index].upper() + word[p_index:]
            words[j] = word

        odd_sections[i] = ' '.join(words)

    # Combine (processed) odd sections into new list with (unprocessed) evens...
    new_list = []
    for i in range(len(odd_sections)):
        new_list.append(odd_sections[i])
        if i < len(even_sections):
            new_list.append('\'' + even_sections[i] + '\'') # ...adding back quote marks*
    new_string = ' '.join(new_list)

    # Restore any linebreaks
    if linebreak_indices != []:
        lines = []
        prev_index = -1
        for i in linebreak_indices:
            lines.append(new_string[prev_index + 1 : i])
            prev_index = i
        lines.append(new_string[i+1:])
        # print('lines are', lines) # temp check
        new_string = '\n'.join(lines)
    
    # return new_string.rstrip() + ';' if semicolon else new_string
    # ---now restoring semicolons in process_statements() instead, 
    # (and decided to add it to only/last statement even if not present in input)
    return new_string.rstrip()


# GUI...

from tkinter import *
root_widget = Tk()
root_widget.title('modstr modifies strings - so far just has a function to capitalise SQL keywords in non-quoted substrings')

root_widget.geometry("1000x500") # provisional width, height GUI

Label(root_widget, text = 'Enter (SQL) text)').grid(row=0, column=0) # (1st row of grid, so row index is 0)

input_field = Text(root_widget, width = 120, fg = 'blue', font=("Courier", 10),
                   height=10) # input textbox (on 2nd row)

input_field.grid(row=1, column=0, padx=15) # ---added padding to move Text box(es) out from left side of windw

output = StringVar()


# ---adding to process each statement, as defined by semicolons, separately
def process_statements(s: str): # Note7
    statements = s.split(';') # If final statement has the semicolon, empty string is added, so...
    statements = statements[:-1] if statements[-1] == '' else statements # ...do this
    for statement in statements:
        # print(upper_SQL_keywords(statement.strip())) # temp
        output_field.insert("end", upper_SQL_keywords((statement.strip())) + ';\n')


def submit_click(): # actions for Submit button bekow
    output_field.delete('1.0', END) # clear any existing output
    # output_field.insert("1.0", upper_SQL_keywords(input_field.get("1.0",'end').rstrip()))
    process_statements(input_field.get("1.0",'end').rstrip()) # ---now pass through new fn 1st


# 'Submit' button on 3rd row grid sets output text in 4th row; Note4
Button(root_widget, text = 'Submit', 
       command = submit_click, 
       bg='#C8C8C8').grid(row=2, column=0)

output_field = Text(root_widget, width = 120, fg = 'blue', 
                     font=("Courier", 10), height=10) # output textbox 

output_field.grid(row=3, column=0) # (located on 4th row)

root_widget.mainloop()


'''
Note1: Using the optional arg type specifier has the advantage of allowing
IDE to make builtin method suggestions on typing dot after string etc.

Note2: Much of the code is dealing with possibility of words from key_set used within a string in query, 
i.e. NOT as keywords, so would NOT want to mod, e.g. 2nd 'is' in the following...
select first_name, last_name, gender from patients where gender is 'M is gender';
[Iteration 4 was dead end with shelx.split() - does not preserve quotation marks]
The whole thing is now rather messy, with some (inefficient) string concatenation, 
and might be better tried with regex, but this approach is probably good enough for now.

Note3: List from as per https://www.w3schools.com/sql/sql_ref_keywords.asp 
but including each word of any multi-word phrases as separate entries, not including 'null'.
I think this will still be suitable, but if not will have to change from
odd_sections[i].split()  to a more complex search and replace strategy.

Note4: Provisionally replaced command value of submit_click with a lambda in 15th Commit, 
as the submit_click() function (see below) was used only here, and had only 1 expression. 
def submit_click():
    output.set(upper_SQL_keywords(input_field.get())) 
    # input_field.delete(0, END) # (optional, to remove entered text after output appears)
    # (or could add a 'Clear' button and associated function)
...of course may revert if do add extra expressions such as the delete call

Note5: Decided (provisionally) to uppercase (MySQL) function names also. My current approach
assumes (and only works for) 'conventionally written' calls with no space between function name
and opening parenthesis. It means that the check against fn_set (and the presence of the set at all)
is not actually needed, though I have included it to exclude mis-processing of any column names
that might happen to have an opening parentnesis within them (unlikely, admittedly). Processing of
function calls with a space could be included by changing   
if word in key_set: 
to
if word in key_set or if word in fn_set:
but that would open the possibility of mis-processing any column names that happened to be the 
same as function names...something that might also happen for keywords, though probaby less likely?

Note6: Can process a statement written over multiple lines as long as there  
are no indentation sand no traling spaces before linebreaks.

Note7: Multiple statements. as deliniated by semicolons, can be processed. 
If the final  (or only) statement does not have a semicolon, one is added,
though this could be changed if needed.


Example1
select first_name, last_name, gender from patients where gender is 'M';
-->
SELECT first_name, last_name, gender FROM patients WHERE gender IS 'M';

Example2 - a value in quotation marks has a word from keyword that should not be processed as a keyword
select first_name, last_name, gender from patients where gender is 'M is gender';
-->
SELECT first_name, last_name, gender FROM patients WHERE gender IS 'M is gender';

Example3 - keyword adjacent to (terminal) semicolon
select first_name, last_name from patients where allergies is null;
-->
SELECT first_name, last_name FROM patients WHERE allergies IS NULL;

Example4 - no semicolon
select first_name, last_name from patients where allergies is null
-->
SELECT first_name, last_name FROM patients WHERE allergies IS NULL;

Example5 - all 4 above input together
select first_name, last_name, gender from patients where gender is 'M';
select first_name, last_name, gender from patients where gender is 'M is gender';
select first_name, last_name from patients where allergies is null;
select first_name, last_name from patients where allergies is null
-->
SELECT first_name, last_name, gender FROM patients WHERE gender IS 'M';
SELECT first_name, last_name, gender FROM patients WHERE gender IS 'M is gender';
SELECT first_name, last_name FROM patients WHERE allergies IS null;
SELECT first_name, last_name FROM patients WHERE allergies IS null;

Example6 - 2 statements on 1 input line
select * from patients; select first_name where last_name = 'John;
-->
SELECT * FROM patients;
SELECT first_name WHERE last_name = 'John';

'''