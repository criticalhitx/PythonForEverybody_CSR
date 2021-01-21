#Hitung jumlah angka2 yang muncul

import re
result = list()
hd = open('text.txt')
for line in hd:
    line = line.rstrip()
    numbers = re.findall('[0-9]+',line)
    for number in numbers:
        result.append(number)
total = 0
for i in result:
    total=total+int(i)
print(total)