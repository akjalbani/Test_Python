# PyPDF2 is the python poweful library to read and write pdf file, you have to install PyPDF2 library with pip command
# pip install PyPDF2
# pip install os
# author: AA Jalbani
# version 1.0
# Tested on Python IDLE
# ################################################################################################
import PyPDF2
import os
os.chdir('C:\\Users\\xyz\\Desktop\\mypdf') # change dir ( chdir) and provide relative path to the target folder
pdfFile = open('filename.pdf','rb') # read binary mode
reader = PyPDF2.PdfFileReader(pdfFile)
pages = reader.numPages
print("No .of pages = ", pages)
page = reader.getPage(2) # readeing page numbers 3 -> arg 0 represents the page 1, arg1 represents page 2 and so on
text= page.extractText()
print("Text from Pdf file")
print("^"*30)
print(text)
