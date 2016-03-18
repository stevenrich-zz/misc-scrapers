import sys
import csv

tsv_in = csv.reader(sys.stdin, dialect=csv.excel_tab)
csv_out = csv.writer(sys.stdout, dialect=csv.excel)

for row in tsv_in:
	csvout.writerow(row)