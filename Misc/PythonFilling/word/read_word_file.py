# demo to read word doc. you need to install python-docx library using pip command
#pip install python-docx
# Reference - automate boring stuff with python programming
# tested on python IDLE

import docx

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

print(getText("C:\\Users\\xyz\\Desktop\\wordfiles\\demo.docx")) # loation of file 
