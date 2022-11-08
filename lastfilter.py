#Удаление всех повторяющихся строк
uniqlines = set(open('filter4.txt','r', encoding='utf-8').readlines())
gotovo = open('last.txt','w', encoding='utf-8').writelines(set(uniqlines))