# bankdata
### The Problems of Historical Data Extraction
Many libraries have begun to upload scans of their archives, and many scans contain historical data that is not available anywhere else. These scans are of varying quality and extracting the data can be very time consuming. Here are my attempts to extract data from the several thousand pages of pdf's like the one below.

![alt text](https://s3.amazonaws.com/the-present-age/1872_-_0001_2_26.png "Bank data in printed form")



### First Attempts
I wrote these scrips to try and extract the table data found in the Comptroller of the Currency reports for US Banks in the 1800s.
I was working with a subset of state summery files. [Here](https://s3.amazonaws.com/the-present-age/1872.pdf) is an example.
The full set of files is available [here](https://fraser.stlouisfed.org/title/56).
### OCR
OCR is now a solved problem. I have found Tesseract 4 to the best most cases. Some of the pages of these scans are very messing and Tesseract did a better job as guess half-missing characters than the alternatives.

##### OCR Ranking
All of the OCR tools made mistakes. If I had to rank the quality of the text recognition services it would be as follows.
1. **Tesseract 4** - Easy to use and gave the most accurate output. I did not retrain the model.
2. **ABBYY FineReader** - very well designed application but did not handle obscured text well which is common in historical documents.
3. **OCR provided by the FED's digitization team** - The FED's OCR had lots of error on pages with non-perfect scans.
4. **Free online OCR sites** - These were very bad in general. They worked well on images like the one above but were junk on lower quality pages.
5. **Adobe Acrobat** - I was surprise how poorly Acrobat performed when re-OCRing these pages. It did not produce a single usable page.

### Table Extraction
I found three tools that were designed for this task. So far, none of them have been much help.
 - [Camelot](https://github.com/socialcopsdev/camelot)
 - [Tabula](https://tabula.technology/)
 - [pdftotable](https://github.com/tfmorris/pdf2table)

The best I have been able to do far, which is not very good, is to used Camelot and hard code the table areas. Unfortunately, the programs still messes up the columns. This code is in redeem.py. 
