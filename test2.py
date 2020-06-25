import sys
from openpyxl import load_workbook

xlsx = sys.argv[1]
month = sys.argv[2]
month_list = month.split(",")

wb = load_workbook(filename = xlsx)
dict_val = {}
for mon in month_list:
    ws = wb[mon]
    for row in ws.rows:
        #print(type(row))
        if row[0].value is not None and row[6].value is not None and "Summary" not in str(row[6].value):
            if row[0].value in dict_val:
                dict_val[row[0].value] += row[6].value
            else:
                dict_val[row[0].value] = row[6].value

for ele in dict_val:
    print(ele + "\t"  + str(dict_val[ele]))
