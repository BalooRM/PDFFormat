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

#indir = './'
indir = '../StackOverflow/'
files = os.listdir(indir)
files = [a for a in files if '.pdf' in a]
files = ['fillable_form2.pdf', 'fefillable_form2.pdf']
print(files)

for fname in files:
    pdf = pymupdf.open(indir + fname)
    print('***', fname)
    print(dir(pdf))
    printAttr('pdf', pdf)
    for page in pdf:
        widgets = page.widgets()
        for widget in widgets:
            print('widget field_name:', widget.field_name)
            #print('dir(widget)', dir(widget))
            printAttr('widget', widget)
            #print("'" + widget.field_name + "': '', ") 
            # print('widget field_type_string:', widget.field_type_string)
            # print('widget field_value:', widget. field_value)
            printAttr('widget _annot:', widget._annot)
            print(widget._annot.info)
            # print('dir(widget._annot)', dir(widget._annot))
            # printAttr('widget._annot.flags', widget._annot.flags)
    pdf.save(fname.split('.')[0] + '_updated.pdf')
    pdf.close()
                  
