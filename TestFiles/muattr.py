# use PyMuPDF (fitz) to evaluate format of PDFs
import pymupdf 
import os, sys

def iscallable(obj, attr):
    try:
        retval = callable(getattr(obj, attr))
    except:
        # default to true to avoid call
        return True
    return retval

def printAttr(prefix, obj):
    #attributes = [attr for attr in dir(obj) if not attr.startswith('__') and not iscallable(obj, attr)]
    attributes = [attr for attr in dir(obj) if not iscallable(obj, attr)]
    #attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    for attr in attributes:
        print(prefix, f"{attr}: {getattr(obj, attr)}")


indir = './'

files = os.listdir(indir)
files = [a for a in files if '.pdf' in a]
files = ['NumberTest_muformat2.pdf']
print(files)

for fname in files:
    pdf = pymupdf.open(indir + fname)
    print('***', fname)
    print(dir(pdf))
    printAttr('pdf', pdf)
    for page in pdf:
        widgets = page.widgets()
        for widget in widgets:
            print('dir(widget)', dir(widget))
            printAttr('widget', widget)
            print('dir(widget._annot)', dir(widget._annot))
            printAttr('widget._annot.flags', widget._annot.flags)
