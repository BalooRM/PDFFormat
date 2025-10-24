# Use PyMuPDF to create fillable PDF with 3 pages and a single element per page.
# This form contains currency, percentage, and number fields. 
import pymupdf
import sys

doc = pymupdf.open()  # Create a new PDF document
page = doc.new_page()  # Add a blank page

# Add a text field (widget)
field = pymupdf.Widget()
field.field_type = pymupdf.PDF_WIDGET_TYPE_TEXT
field.field_name = "FieldName_Currency"
field.field_value = None
field.text_fontsize = 12
field.rect = pymupdf.Rect(100, 150, 300, 180)
field.border_style = "Solid"
field.script_format = 'AFNumber_Format(2, 0, 0, 0, "\u0024 ", true);'
field.script_stroke = 'AFNumber_Keystroke(2, 0, 0, 0, "\u0024 ", true);'
field.text_format = 1
page.add_widget(field)

page = doc.new_page()  # Add a blank page
field = pymupdf.Widget()
field.field_type = pymupdf.PDF_WIDGET_TYPE_TEXT
field.field_name = "FieldName_Percent"
field.field_value = None
field.text_fontsize = 12
field.rect = pymupdf.Rect(100, 150, 300, 180)
field.border_style = "Solid"
field.script_format = 'AFNumber_Format(2, 0, 0, 0, "\u0025", false);'
field.script_stroke = 'AFNumber_Keystroke(2, 0, 0, 0, "\u0025", false);'
field.text_format = 1
page.add_widget(field)

page = doc.new_page()  # Add a blank page
field = pymupdf.Widget()
field.field_type = pymupdf.PDF_WIDGET_TYPE_TEXT
field.field_name = "FieldName_Number"
field.field_value = None
field.text_fontsize = 12
field.rect = pymupdf.Rect(100, 150, 300, 180)
field.border_style = "Solid"
field.script_format = 'AFNumber_Format(0, 0, 0, 0, "", true);'
field.script_stroke = 'AFNumber_Keystroke(0, 0, 0, 0, "", true);'
field.text_format = 1
page.add_widget(field)

# Save the document
doc.save("fillable_form2.pdf")
doc.close()
