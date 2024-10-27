# 1st commit (starting this repo series yet again, this time because of apparent corruption in version sequence/behaviour!)

def upper_SQL_keywords(s: str) -> str: # Note1
    mod_s = s.replace('select', 'SELECT')
    mod_s = mod_s.replace('from', 'FROM')
    mod_s = mod_s.replace('where', 'WHERE')
    mod_s = mod_s.replace('is', 'IS')
    return mod_s

# TODO: Try to deal with posibility of double-quotes being used in query etc?


print(upper_SQL_keywords("select first_name, last_name, gender from patients where gender is 'M';"))


# Note1: using the optional arg and return type specifiers has the advantage
# of allowing IDE to make builtin method suggestions on typing dot after string etc