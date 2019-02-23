# manually count the number of spaces for each column
# read each into dataframe line by line
# remove spaces and commas from dataframe
# export to csv

import re
import csv
clean = []
with open("bigboy.txt") as fp:
   line = fp.readline()
   cnt = 1
   while line:
       line = line.strip()
       line = list(line)
       c1 = line[0:22]
       c2 = line[23:40]
       c3 = line[41:72]
       c4 = line[73:93]
       c5 = line[93:111]
       c6 = line[112:130]
       columns = [c1, c2, c3, c4, c5, c6]
       for x in columns:
           str1 = ''.join(x)
           getout = [' ', '.', ',', '$', '\'', '-', '&']
           for tag in getout:
               str1 = str1.replace(tag, '')
           #print(str1)
           clean.append(str1)
       line = fp.readline()
       cnt += 1

writer = csv.writer(open("bigout.cvs",'wb'))
a = 0
b = 6
for c in clean:
    c.replace(",","")
for x in range(3200):
    short = clean[a:b]
    writer.writerow(short)
    a = a+6
    b = b+6




#for word in short:
    #writer.writerow([word])

#for i in range(5):
    #df.loc[i] = [np.random.randint(-1,1) for n in range(3)]for i in range(5):

#df.to_excel('foo.xlsx', sheet_name='Sheet1')
