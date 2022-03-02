# https://stackoverflow.com/questions/22776388/pypdf2-compression

# import PyPDF2
# path = open('path/to/hello.pdf', 'rb')
# path2 = open('path/to/another.pdf', 'rb')
# merger = PyPDF2.PdfFileMerger()
# merger.append(fileobj=path2)
# merger.append(fileobj=path)
# pdf.filters.compress(merger)
# merger.write(open("test_out2.pdf", 'wb'))

# import PyPDF2

# path = 'path/to/hello.pdf'
# path2 = 'path/to/another.pdf'
# pdfs = [path, path2]

# writer = PyPDF2.PdfFileWriter()

# for pdf in pdfs:
#     reader = PyPDF2.PdfFileReader(pdf)
#     for i in xrange(reader.numPages):
#         page = reader.getPage(i)
#         page.compressContentStreams()
#         writer.addPage(page)

# with open('test_out2.pdf', 'wb') as f:
#     writer.write(f)