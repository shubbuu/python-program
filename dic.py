import PyPDF2,re,pprint
file = open('vocabulary.pdf', 'rb')
pdfreader = PyPDF2.PdfFileReader(file)
page = pdfreader.getPage(0)
xyz = page.extractText()
list = xyz.split('\n')
del list[:3]

voc = {}
for i in list:
    print(i)
    regex = re.compile(r'\w+')
    mo = regex.findall(i)
    # print(mo)
    voc.setdefault(mo[0],' '.join(mo[1:]))
    print(voc)
    break

print("enter a word to be searched")    
xyz=input()
if xyz in voc:
    print("meaning of word is"+voc[xyz])
else:
    print("word doesnt exist")

    
    
    
    
    
