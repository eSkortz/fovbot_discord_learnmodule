#Удаление всех строк, не содержащих вертикальную черту
import re
with open('filter1.txt') as f:
    lines = f.readlines()

str = '|'
pattern = re.compile(re.escape(str))
with open('filter2.txt', 'w') as f:
    for line in lines:
        result = pattern.search(line)
        if result is None:
            continue
        else:
            f.write(line)