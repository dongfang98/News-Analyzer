from PyPDF2 import PdfFileReader

def convert_from_PDF(title):
    pdf = open(title, 'rb')
    pdfReader = PdfFileReader(pdf)
    body = ''
    for i in range(pdfReader.numPages):
        page = pdfReader.getPage(i)
        body += page.extractText()
    return body
