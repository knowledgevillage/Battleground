from pypdf import PdfReader

reader = PdfReader('S:\GitRepo\practice\Capstone Project\dataExtract\sample.pdf')

print(len(reader.pages))
page=reader.pages[0]
print(page.extract_text())

