import re 

text = input()

tx = re.findall(r"[a-z][_][a-z]", text)

print(tx)