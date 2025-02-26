#1

import re

text = "String: abb , a0 , ab"

tx1 = re.findall(r"ab", text)

tx2 = re.findall(r"a0", text)

tx3 = re.findall(r"abb", text)

print(tx1)

print(tx2)

print(tx3)
