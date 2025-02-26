import re

text = input()

tx = re.findall(r"a.+b$", text)

print(tx)