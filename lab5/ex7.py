import re

text = input()

def s_to_c(txt):

    tx = re.findall("[a-z]+",text)

    help = ""

    for i in tx:

        help+=i[0].upper()+i[1:len(i)]

    return help

print(s_to_c(text))