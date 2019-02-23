import re
import csv
import pandas as pd
import os
from shutil import copyfile

# helper - sorts like a human
# def sort_human(l):
#   convert = lambda text: float(text) if text.isdigit() else text
#   alphanum = lambda key: [ convert(c) for c in re.split('([-+]?[0-9]*\.?[0-9]*)', key) ]
#   l.sort( key=alphanum )
#   return l


# # Lining Up the Files
# #ordered
# #= sort_human(os.listdir("1872"))
# print(sort_human(os.listdir('1872')))

filelist = os.listdir("1872")
os.chdir("1872")
for file in filelist:
    with open(file) as csv_file:
        ### CLEAN
        # Read in files
        csv_reader = csv.reader(csv_file, delimiter=',')
        outname = "out" + file
        csv_out = open(outname, 'w', newline='')
        csv_writer = csv.writer(csv_out, delimiter=',')
        #chars to take out
        specials = [' ', '.', ',', '$', '\'', '-', '&', '\n']

        flag = False
        blank_counter = 1
        for line in csv_reader:

            #replacGe chars in specials with blank
            for out in specials:
                line = [value.replace(out, '') for value in line]
            #replace empty cols
            # for i in range(len(line)):
            #     if flag == False and line[i] == '':
            #             line[i] = '1'
            # flag = True

            #replace empty rows
            #possible problem in stata
            # if line[0] == '':
            #     print("Found Blank Number:", blank_counter)
            #     line[0] = blank_counter
            #     blank_counter = blank_counter + 1
            if not line == None:
                csv_writer.writerow(line)
        csv_out.close()


            # #MERGE
            # df1 = pd.read_csv('csv_out.csv').T
            # #print(df1.head)
            # df2 = pd.read_csv('runner.csv')
            # #print(concat.head)
            # #df1.to_csv("panout.csv")
            # df1.append(df2)
            # print(df1.head)
            # #concat = pd.concat([df1, df2], ignore_index=True)
            # #print(concat.head)
            # df1.to_csv("runner.csv")









#df.append("csv_out3.csv")






    #pd.read_csv('csv_out.csv').T.to_csv('poutput.csv',header=False)

    #df=pd.DataFrame(list,columns=['col1','col2'])

    # res = pd.DataFrame(clean, columns=('label', '1', '2', '3', '4', '5'))
    #
    # print(res.head)
    # df = pd.DataFrame(clean[0:5]).T
    # df = pd.read_csv('csv_out.csv')
    # print(res.head)
    #df.to_csv('example.csv')
    # for row in csv_reader:
    #     #Removes chars in getout from each line
    #     for entry in row:
    #         for char in entry:
    #             getout = [' ', '.', ',', '$', '\'', '-', '&']
    #             for tag in getout:
    #                 char = char.replace(tag, '')
    #             print(entry)
    #             break





    # while line:
    #     line = line.strip()
    #     line = list(line)
    #     for x in columns:
    #         str1 = ''.join(x)
    #         getout = [' ', '.', ',', '$', '\'', '-', '&']
    #         for tag in getout:
    #             str1 = str1.replace(tag, '')
    #         #print(str1)
    #         clean.append(str1)
    #     line = fp.readline()
