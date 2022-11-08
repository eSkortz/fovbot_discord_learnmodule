#Удаление из файла пустых строк
with open('input.txt', 'r') as inf, open('filter1.txt', 'w') as out:
    for line in inf:
        if line.strip():
            out.write(line)