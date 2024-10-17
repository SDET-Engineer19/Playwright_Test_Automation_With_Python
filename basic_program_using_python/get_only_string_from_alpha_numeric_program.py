val = "kabira1234"
print(val.replace("\\^[0-9]", ""))

import re

pattern = r'[0-9]'
val2 = re.sub(pattern, '', val)

print(val2)

val = ''.join((x for x in val if not x.isdigit()))
print(val)
