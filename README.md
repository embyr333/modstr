Simple Python tool to automate capitalisation of keywords and (MySQL) function names in SQL statements (for enhanced readability). No immediate plans to add other functionality, but named project 'modstr' to suggest general modification of strings. 

Function names are processed only if the calls are 'conventionally written' with no space between function name and opening parenthesis (though this could be changed; see Note5 in code comments).

Multiple statements can be input simultaneously, assuming they are separated by semicolons.

Individual statements over multiple lines can be processed, but only if there are no indentations and no traling spaces before linebreaks.

A semicolon is added to a final/only statement if absent, though this can be changed (Note7a in code).

Testing has been limited, so there may be well-formed statements that elicit incorrect output or errors.

Additions of feature addition /modification of behaviours was gradual, based on my limited needs as I wrote a few simple SQL pracise statements, so the resulting code may have areas of redundancy, inefficient approaches and sub-optimal organisation. If developing a more rigorous and/or fully-featured tool, I would want to consider more complex use cases, and probably start from scratch with a comprehensive list of requirements in mind.

The latest version can be run
(1) If you have Python installed, by downloading the source code and running “python modstr.py” in a terminal opened in the destination folder, or through an IDE
OR
(2) By downloading the modstr.exe file from Releases (then by passing any system warnings after clicking into that). This should work for Windows machines anyway; not sure about other operating systems.
