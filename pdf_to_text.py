import PyPDF2

def pdf_to_text_main(filename):
    # creating a pdf file object
    pdfFileObj = open(filename, 'rb')
    
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    
    # This will store the number of pages of the pdf file
    x = len(pdfReader.pages)
    text = ""

    for i in range(1,x):
        pageObj = pdfReader.pages[i]
        text += pageObj.extract_text() + " "    

    return text