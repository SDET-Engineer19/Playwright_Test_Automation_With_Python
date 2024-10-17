def count_each_char_occurrence(val):
    freq = {}
    for key in set(val):
        freq[key] = val.count(key)
    return freq


new_set_val = count_each_char_occurrence("Kabira")
print(new_set_val)



