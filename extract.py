import PyPDF2
path = r"c:\Users\MUBBASSIRKHAN\Desktop\iPortfolio-1.0.0\Mubbassirkhan-A-Jahagirdar-FlowCV-Resume-20260225 (3).pdf"
reader = PyPDF2.PdfReader(path)
for i, p in enumerate(reader.pages):
    print('==== page', i, '====')
    print(p.extract_text())
