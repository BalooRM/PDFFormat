# Use PyMuPDF to update numeric fields in PDF file
import pymupdf

jss = { 'number': 'AFNumber_Format(0, 0, 0, 0, "", true);',
        'number_ks': 'AFNumber_Keystroke(0, 0, 0, 0, "", true);',
        'currency': 'AFNumber_Format(2, 0, 0, 0, "\u0024 ", true);',
        'currency_ks': 'AFNumber_Keystroke(2, 0, 0, 0, "\u0024 ", true);',
        'percent': 'AFNumber_Format(2, 0, 0, 0, "\u0025", false);',
        'percent_ks': 'AFNumber_Keystroke(2, 0, 0, 0, "\u0025", false);',
        'xpercent': 'AFPercent_Format(2, 0);',
        'xpercent_ks': 'AFPercent_Keystroke(2, 0);'
        }

pdf = pymupdf.open("./fefillable_form.pdf")
for page in pdf:
    widgets = page.widgets()
    for widget in widgets:
        if widget.field_type_string == 'Text':
            widget.text_fontsize=12.0
            print(widget.field_name)
            if 'Number' in widget.field_name:
                widget.text_format = 1
                widget.script_stroke = jss['number_ks']
                widget.script_format = jss['number']
                dct = widget._annot
                print(widget._annot.info)
                dct.set_info(title=widget.field_name)
                #widget._annot.set_info(title=widget.field_name) #, id='fitz-W0')
                widget._annot.update()
                print(widget._annot.info)
                
            if 'Percent' in widget.field_name:
                widget.text_format = 1
                widget.script_stroke = jss['percent_ks']
                widget.script_format = jss['percent']
                print(widget._annot.info)
                widget._annot.set_info(title=widget.field_name) #, id='fitz-W0')
                print(widget._annot.info)
                
            if 'Currency' in widget.field_name:
                widget.text_format = 1
                widget.script_stroke = jss['currency_ks']
                widget.script_format = jss['currency']
                print(widget._annot.info)
                widget._annot.set_info(title=widget.field_name) #, id='fitz-W0')
                print(widget._annot.info)
                
            widget.update()
            widget._annot.update()
pdf.save("./fefillable_form2.pdf")
pdf.close()			
