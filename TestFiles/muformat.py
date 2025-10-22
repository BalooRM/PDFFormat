# use PyMuPDF (fitz) to format PDFs
# set textarea font to 12 pt instead of autosize
# Use PyMuPDF (fitz)
# add javascript xrefs https://github.com/pymupdf/PyMuPDF/discussions/2157
#
import pymupdf
import sys

indir = './'
outdir = './'
fname = 'NumberTest.pdf'

pdf = pymupdf.open(indir + fname)
print(fname)
xrefs = {}
jss = { 'number': 'AFNumber_Format(0, 0, 0, 0, "", true);',
        'number_ks': 'AFNumber_Keystroke(0, 0, 0, 0, "", true);',
        'percent': 'AFPercent_Format(2, 0);',
        'percent_ks': 'AFPercent_Keystroke(2, 0);',
        'currency': 'AFNumber_Format(2, 0, 0, 0, "\u0024 ", true);',
        'currency_ks': 'AFNumber_Keystroke(2, 0, 0, 0, "\u0024 ", true);',
        'validate': 'AFRange_Validate(true, 0, true, 1);'
}

for key in jss:
    xref = pdf.get_new_xref()
    js = jss[key]
    objsource = f"<</Type/Action/S/JavaScript/JS({js})>>"
    print(objsource)
    objsource = f"<</JS({js})/S/JavaScript>>"
    print(objsource)
    pdf.update_object(xref, objsource)
    cat = pdf.pdf_catalog()
    #pdf.xref_set_key(cat, "OpenAction", f"{xref} 0 R")
    xrefobj = pdf.xref_object(xref, compressed=False)
    # print('key:', str(xref))
    # print('xrefobj:', xrefobj)
    xrefs[key] = xref
    
print(xrefs)
for xref in range(1, pdf.xref_length()):
    js = pdf.xref_get_key(xref, "JS")
    if js and js[0] == "string":
        print('xref=', str(xref))
        print(f"JavaScript Code: {js[1]}")
        print(js)
        xrefobj = pdf.xref_object(xref, compressed=True)
        print('xrefobj:', xrefobj)

for page in pdf:
    widgets = page.widgets()
    for widget in widgets:
        print(widget.field_name)
        if widget.field_type_string == 'Text':
            widget.text_fontsize=12.0
            xref = widget.xref
            print('widget xref:', xref)
            xrefobj = pdf.xref_object(widget.xref, compressed=True)
            print(xrefobj)

            if 'Currency' in widget.field_name:
                #aa_dct = "<</F " + str(xrefs['currency']) + " 0 R/K " + str(xrefs['currency_ks']) + " 0 R/V " + str(xrefs['validate']) + " 0 R>>"
                aa_dct = "<</F " + str(xrefs['currency']) + " 0 R/K " + str(xrefs['currency_ks']) + " 0 R>>"
                print(aa_dct)
                if 'Parent' in xrefobj:
                    parentxref = int(xrefobj.split('Parent ')[-1].split(' ')[0])
                    print('Parent', str(parentxref))
                    pxrefobj = pdf.xref_object(parentxref, compressed=True)
                    print('pxrefobj:', pxrefobj)
                    pdf.xref_set_key(parentxref, "/AA", aa_dct)
                    print(pdf.xref_object(parentxref, compressed=True))
                
            if 'Numeric' in widget.field_name:
                #aa_dct = "<</F " + str(xrefs['number']) + " 0 R/K " + str(xrefs['number_ks']) + " 0 R/V " + str(xrefs['validate']) + " 0 R>>"
                aa_dct = "<</F " + str(xrefs['number']) + " 0 R/K " + str(xrefs['number_ks']) + " 0 R>>"
                print(aa_dct)
                if 'Parent' in xrefobj:
                    parentxref = int(xrefobj.split('Parent ')[-1].split(' ')[0])
                    print('Parent', str(parentxref))
                    pxrefobj = pdf.xref_object(parentxref, compressed=True)
                    print('pxrefobj:', pxrefobj)
                    pdf.xref_set_key(parentxref, "/AA", aa_dct)
                    print(pdf.xref_object(parentxref, compressed=True))

            if 'Percentage' in widget.field_name:
                #aa_dct = "<</F " + str(xrefs['percent']) + " 0 R/K " + str(xrefs['percent_ks']) + " 0 R/V " + str(xrefs['validate']) + " 0 R>>"
                aa_dct = "<</F " + str(xrefs['percent']) + " 0 R/K " + str(xrefs['percent_ks']) + " 0 R>>"
                print(aa_dct)
                if 'Parent' in xrefobj:
                    parentxref = int(xrefobj.split('Parent ')[-1].split(' ')[0])
                    print('Parent', str(parentxref))
                    pxrefobj = pdf.xref_object(parentxref, compressed=True)
                    print('pxrefobj:', pxrefobj)
                    pdf.xref_set_key(parentxref, "/AA", aa_dct)
                    print(pdf.xref_object(parentxref, compressed=True))

            widget.update()
            
pdf.save(outdir + fname.split('.')[0] + '_muformat2.pdf')
pdf.close()


                    
sys.exit()

for page in pdf:
    widgets = page.widgets()
    for widget in widgets:
        print(widget.field_name)
        if widget.field_type_string == 'Text':
            widget.text_fontsize=12.0
            if 'Currency' in widget.field_name:
#                widget.text_format = pymupdf.PDF_WIDGET_TX_FORMAT_NUMBER
                print(dir(widget))
                print(dir(widget.__class__))
                print(dir(widget.__format__))
                print(dir(widget._validate))
                print(dir(widget.script_format))
 #               widget.set_action("Validate", js_action)
            widget.update()
            widget._annot.set_flags(4)
            widget._annot.update()
            
        
pdf.save(outdir + fname.split('.')[0] + '_muformat2.pdf')
pdf.close()
