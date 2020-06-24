# bankdata
### The Problems of Historical Data Extraction
Many libraries have begun to upload scans of their archives, and many scans contain historical data that is not available anywhere else. These scans are of varying quality and extracting the data can be very time consuming. Here are my attempts to extract data from the several thousand pages of pdf's like the one below.

### First Attempts
I wrote these scripts to try and extract the table data found in the Comptroller of the Currency reports for US Banks in the 1800s.
I was working with a subset of state summary files. The full set of files is available [here](https://fraser.stlouisfed.org/title/56).
### OCR
OCR is now a solved problem. I tried every solution I could find in the spring of 2019, and [Google’s Cloud Vision API](https://cloud.google.com/vision/docs/drag-and-drop) was the best. AWS Textract and Azure’s OCR were fine, but they were not sufficiently better than the free options to justify the hassle of setting them up and in almost every case I tested Google performed better.

##### OCR Ranking
All of the OCR tools made mistakes. If I had to rank the quality of the text recognition services for my use case it would be as follows.
1. [**Google Cloud Vision**](https://cloud.google.com/vision/docs) - This service performed well on text that was tilted, obscured by ink specs, and on characters ambiguous even to humans. All new data extraction projects should start here.
1. [**Tesseract 4**](https://tesseract-ocr.github.io/) - Easy to use and gave the most accurate output. I did not retrain the model.
2. [**ABBYY FineReader**](https://www.abbyy.com/en-us/finereader/) - very well designed application but did not handle obscured text well which is common in historical documents.
3. [**OCR provided by the FED's digitization team**](https://fraser.stlouisfed.org/title/56) - The FED's OCR had lots of errors on pages with non-perfect scans.
4. **Free online OCR sites** - These were very bad in general. I think most of these sites are running Tesseract under the hood and 
5. **Adobe Acrobat** - I was surprised how poorly Acrobat performed when re-OCRing these pages. It did not produce a single usable page. Adobe's lack of innovation here is disappointing. 

### Table Extraction
I found three tools that were designed for this task. So far, none of them have been much help.
 - [Camelot](https://github.com/socialcopsdev/camelot)
 - [Tabula](https://tabula.technology/)
 - [pdftotable](https://github.com/tfmorris/pdf2table)

The best I have been able to do so far, which is still not very good and requires alot of hand correction, is to use Camelot and hard code the table areas. Unfortunately, the programs still messes up the columns. This code is in redeem.py. 
