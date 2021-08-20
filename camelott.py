'''import camelot

# PDF file to extract tables from (from command-line)
file = "foo.pdf"

# extract all the tables in the PDF file
tables = camelot.read_pdf(file)

# number of tables extracted
print("Total tables extracted:", tables.n)

# print the first table as Pandas DataFrame
print(tables[0].df)

# export individually as CSV
tables[0].to_csv("foo.csv")
# export individually as Excel (.xlsx extension)
tables[0].to_excel("foo.xlsx")

# or export all in a zip
tables.export("foo.csv", f="csv", compress=True)

# export to HTML
tables.export("foo.html", f="html")'''
#!pip install tabula-py
import tabula
#read all table data
df = tabula.read_pdf("bs.pdf",pages="all")
print(df)

df1 = tabula.convert_into("bs.pdf", "sample.csv",pages="all", output_format="csv")
print(df1)
df2 = tabula.convert_into("bs.pdf", "sample.json",pages="all", output_format="json")
print(df2)

# Python program to convert text
# file to JSON


