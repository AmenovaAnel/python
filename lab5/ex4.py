import re

text = input()

tx = re.findall(r"[A-Z][a-z]+", text)

print(tx)