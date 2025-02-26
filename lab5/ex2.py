#2

import re

text = input()

text1 = re.findall(r"ab{2,3}")

print(text1)