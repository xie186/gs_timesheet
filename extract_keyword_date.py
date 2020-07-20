import sys
from datetime import datetime
from openpyxl import load_workbook

xlsx = sys.argv[1]
month = sys.argv[2]
key_word = sys.argv[3]

month_list = month.split(",")

wb = load_workbook(filename = xlsx)
#date_format = '%m/%d/%Y'
date_format = '%Y-%m-%d %H:%M:%S'

def validate(date_string):
    #date_format = '%m/%d/%Y'
    try:
        date_obj = datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False 

dict_val = {}
date_now = 0
for mon in month_list:
    ws = wb[mon]
    #print(mon)
    for row in ws.rows:
        #print(type(row))
        #print(row)
        values = []
        for row_val in row:
            values.append(row_val.value)
        #print("\t".join(str(item) for item in values))
        ### DAte 
        if row[0].value is None and row[1].value is not None and row[2].value is None:
            #print(type(row[1].value))
            date_string = str(row[1].value)
            #print(str(row[1].value) + " " + str(validate(date_string)))
            date_string_val = date_string.split(" ")
            date_now = date_string_val[0]
        if row[0].value is None and row[6].value is None and row[2].value is not None and "Summary" not in str(row[6].value):
            if key_word in row[2].value:
                print("{date_now}\t{time}\t{task}\t{content}\t{hour}".format(date_now=date_now, time= row[1].value, task = row[2].value, content = row[3].value, hour = row[5].value))
#for ele in dict_val:
#    print(ele + "\t"  + str(dict_val[ele]))
