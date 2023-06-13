import pdfkit

pdf_file = open('SG - James Seekings - DevOps Engineer.pdf', 'rb')

html_file = pdfkit.from_pdf(pdf_file, 'SG - James Seekings - DevOps Engineer.html')

pdf_file.close()