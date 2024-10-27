# 10th commit - removed the console-print statements & added a few more keywords

def upper_SQL_keywords(s: str): # Note1
    if s == '':
        no_input_message = 'Please enter the query string you want to process'
        return no_input_message

    key_set = ('select', 'from', 'where', 'is', 'and', 'null', 'like', 'in', 'between', 'and') 
    # ... TODO continue to extend as needed

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

    if semicolon == True:
        new_string = new_string.rstrip() + ';'

    return new_string 


# GUI...

from tkinter import *
root_widget = Tk()
root_widget.title('modstr modifies strings - so far just has a function to capitalise SQL keywords in non-quoted substrings')
root_widget.geometry("800x100") # provisional width, height GUI

Label(root_widget, text = 'Enter (SQL) text)').grid(row=0, column=0) # (1st row of grid, so row index is 0)

input_field = Entry(root_widget, width = 100, fg = 'blue', font=("Courier", 10)) # input textbox (on 2nd row)
input_field.grid(row=1, column=0) 

output = StringVar()

# Button-click function sets output text in 4th row of grid (have to put this before button)
def submit_click():
    output.set(upper_SQL_keywords(input_field.get())) 
    # input_field.delete(0, END) # (optional, to remove entered text after output appears)
    # (or could add a 'Clear' button and associated function)

# Button on 3rd row grid
submit_button = Button(root_widget, text = 'Submit', 
                       command = submit_click, bg='#C8C8C8').grid(row=2, column=0, padx=5)

output_field = Entry(root_widget, width = 100, fg = 'blue', textvariable=output, 
                     state='readonly', font=("Courier", 10)) # output textbox 
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


Example1
select first_name, last_name, gender FROM patients where gender is 'M';
SELECT first_name, last_name, gender FROM patients WHERE gender IS 'M';

Example2 - a value in quotation marks has a word from keyword that should not be processed as a keyword
select first_name, last_name, gender from patients where gender is 'M is gender';
SELECT first_name, last_name, gender FROM patients WHERE gender IS 'M is gender';

Example3 - keyword adjacent to (terminal) semicolon
select first_name, last_name from patients where allergies is null;
SELECT first_name, last_name FROM patients WHERE allergies IS NULL;

Example4 - no semicolon
select first_name, last_name from patients where allergies is null
SELECT first_name, last_name FROM patients WHERE allergies IS NULL
'''