import camelot
import matplotlib
import matplotlib.pyplot as plt

tables = camelot.read_pdf('1872_recognized.pdf',pages='1-38', column_tol=2, flavor='stream', table_areas=['35,555,356,374','35,369,356,206','35,196,356,26'])
#tables = camelot.read_pdf('doc.pdf', flavor='stream')
#camelot.plot(tables[0], kind='text')
#plt.show()
tables.export('1872BB.csv', f='csv', compress=True) # json, excel, html
