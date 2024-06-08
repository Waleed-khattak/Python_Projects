from PyPDF2 import PdfReader, PdfWriter

with open("./project2/demo.pdf", 'rb') as infile, open('./project2/updated.pdf', 'wb') as outfile:
    writer = PdfWriter()
    reader = PdfReader(infile)
    for page in range(11, 17):
        writer.add_page(reader._get_page(page))
    writer.write(outfile)

