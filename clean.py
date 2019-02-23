import re
import csv
import pandas as pd
import os
from shutil import copyfile

#generate file list
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

            #replace chars in specials with blank
            for out in specials:
                line = [value.replace(out, '') for value in line]
            #write line if not blank
            if not line == None:
                csv_writer.writerow(line)
        csv_out.close()
