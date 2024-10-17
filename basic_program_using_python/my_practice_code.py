def verify_char_is_present_not(std_name, char_name):
    for char in std_name:
        if char not in char_name:
            print("Not Present")
        else:
            print("Present")


verify_char_is_present_not("Ramesh", 'p')
print("###############")
verify_char_is_present_not("Ramesh", 'a')

