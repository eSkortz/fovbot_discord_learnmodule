#Удаление всех строк содержащих #
import re
with open('filter3.txt') as f:
    lines = f.readlines()

str = '>'
str1 = 'dape'
str2 = 'DaPe'
str3 = 'am'
str4 = 'pm'
pattern = re.compile(re.escape(str))
pattern1 = re.compile(re.escape(str1))
pattern2 = re.compile(re.escape(str2))
pattern3 = re.compile(re.escape(str3))
pattern4 = re.compile(re.escape(str4))
with open('filter4.txt', 'w') as f:
    for line in lines:
        result = pattern.search(line)
        if result is None:
            f.write(line)
with open('filter4.txt', 'w') as f:
    for line in lines:
        result = pattern1.search(line)
        if result is None:
            f.write(line)
with open('filter4.txt', 'w') as f:
    for line in lines:
        result = pattern2.search(line)
        if result is None:
            f.write(line)
with open('filter4.txt', 'w') as f:
    for line in lines:
        result = pattern3.search(line)
        if result is None:
            f.write(line)
with open('filter4.txt', 'w') as f:
    for line in lines:
        result = pattern4.search(line)
        if result is None:
            f.write(line)