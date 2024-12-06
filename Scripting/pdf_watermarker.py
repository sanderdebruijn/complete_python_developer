import PyPDF2
from pathlib import Path


template = PyPDF2.PdfReader(open("./Scripting/pdf_files/twopage.pdf", "rb"))
watermark = PyPDF2.PdfReader(open(Path("./Scripting/pdf_files/wtr.pdf"), "rb"))
output = PyPDF2.PdfWriter()

for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermark.pages[0])
    output.add_page(page)

with open('./Scripting/pdf_files/watermaked_output.pdf', 'wb') as outputFile:
    output.write(outputFile)
