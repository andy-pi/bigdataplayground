import PyPDF2
pdf1File = open('originalfile.pdf', 'rb')
pdfWriter = PyPDF2.PdfFileWriter()
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)

pageObj = pdf1Reader.getPage(0)
pdfWriter.addPage(pageObj)
pdfOutputFile = open('newfile.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()