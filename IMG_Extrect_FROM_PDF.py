import fitz
import sys
from fitz.utils import getColor
#pdf file should be in same direction with this script
doc = fitz.open(input("please enter the file name \n "))

for i in range(len(doc)):
	for img in doc.getPageImageList(i):
		xref = img[0]
		pix = fitz.Pixmap(doc, xref)
		if pix.n<5:
			pix.writePNG("p%s-%s.png" % (i, xref))
		else:
			pix1 = fitz.Pixmap(fitz.csRGB, pix)
			pix1.writePNG("p%s-%s.png" % (i, xref))
			pix1 = None