# 2nd commit

def upper_SQL_keywords(s: str) -> str: # Note1
    key_set = ('select', 'from', 'where', 'is')
    word_list = s.split()
    for i in range(len(word_list)):
        if word_list[i] in key_set:
            word_list[i] = word_list[i].upper()
    mod_query = ' '.join(word_list)
    return mod_query

# TODO: Try to deal with posibility of double-quotes being used in query etc?
# (would have to change 
# ...and also that keywords might be used within a suted string in query, where DON'T want to mod


print(upper_SQL_keywords("select first_name, last_name, gender from patients where gender is M';"))


# Note1: using the optional arg and return type specifiers has the advantage
# of allowing IDE to make builtin method suggestions on typing dot after string etc