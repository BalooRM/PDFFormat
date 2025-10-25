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

# doc = fitz.open("example.pdf")
# for xref in range(1, doc.xref_length()):
# js = doc.xref_get_key(xref, "JS")
# if js and js[0] == "string":
# print(f"JavaScript Code: {js[1]}")

indir = './'

files = os.listdir(indir)
files = [a for a in files if '.pdf' in a]
print(files)
files = []
#files = ['FieldTest_acrobat.pdf']
#files += ['NumberTest.pdf', 'NumberTest_acrobat.pdf']
files += ['NumberTest_muformat2.pdf']
#files = ['FieldTest_muformat2.pdf']
#files = ['FieldTest.pdf']


for fname in files:
    pdf = pymupdf.open(indir + fname)
    print('***', fname)
    cat = pdf.pdf_catalog()
    print('dir(cat)', dir(cat))
    print('cat=', cat)
    for xref in range(1, pdf.xref_length()):
        print('xref=', str(xref))
        print(xref, pdf.xref_get_keys(xref))
        xrefobj = pdf.xref_object(xref, compressed=True)
        print('xrefobj:', xrefobj)
    for page in pdf:
        widgets = page.widgets()
        for widget in widgets:
            print(widget.field_name, widget.xref)

sys.exit()

for fname in files:
    pdf = pymupdf.open(indir + fname)
    print('***', fname)
    cat = pdf.pdf_catalog()
    print('dir(cat)', dir(cat))
    print(cat)
    for xref in range(1, pdf.xref_length()):
        js = pdf.xref_get_key(xref, "JS")
        if js and js[0] == "string":
            print('xref=', str(xref))
            print(f"JavaScript Code: {js[1]}")
            print(js)
            xrefobj = pdf.xref_object(xref, compressed=False)
            print('xrefobj:', xrefobj)
    for page in pdf:
        widgets = page.widgets()
        for widget in widgets:
            print(widget.field_name)
            print('parent:', widget.parent)
            xref = widget.xref
            print(xref)
            xrefobj = pdf.xref_object(xref, compressed=True)
            print('xrefobj:', xrefobj)
            if 'Parent' in xrefobj:
                parentxref = int(xrefobj.split('Parent ')[-1].split(' ')[0])
                print('Parent', str(parentxref))
                pxrefobj = pdf.xref_object(parentxref, compressed=True)
                print('pxrefobj:', pxrefobj)

    
            #print(dir(pdf.
    # print(dir(pdf))
    # printAttr('pdf', pdf)
    # for page in pdf:
    #     widgets = page.widgets()
    #     for widget in widgets:
    #         print('dir(widget)', dir(widget))
    #         printAttr('widget', widget)
    #         print('dir(widget._annot)', dir(widget._annot))
    #         printAttr('widget._annot.flags', widget._annot.flags)
