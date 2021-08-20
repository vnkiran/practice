import pdfx

pdf = pdfx.PDFx("bs.pdf")
metadata = pdf.get_metadata()
reference_list = pdf.get_references()
reference_dict = pdf.get_references_as_dict()
pdf.download_pdfs("target-directory")