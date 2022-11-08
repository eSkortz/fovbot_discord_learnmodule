#Удаление всех строк содержащих @
import re
with open('filter2.txt') as f:
    lines = f.readlines()

str = '<'
pattern = re.compile(re.escape(str))
with open('filter3.txt', 'w') as f:
    for line in lines:
        result = pattern.search(line)
        if result is None:
            f.write(line)