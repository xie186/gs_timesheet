#!/usr/bin/env python
#-*-- coding: utf-8 -*-
import argparse
import gspread

gc = gspread.service_account()


#date_format = '%m/%d/%Y'
date_format = '%Y-%m-%d %H:%M:%S'

def validate(date_string):
    #date_format = '%m/%d/%Y'
    try:
        date_obj = datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False

def gspread(options):
    sh = gc.open_by_key(options.id)
    month_list = options.months.split(",")
    date_now = 0 
    for month in month_list:
        worksheet = sh.worksheet(month)
        data = worksheet.get_all_values()
        for row in data:
            #print(type(row[0]))
            if not row[0]  and row[1]  and not row[2]:
                #print(type(row[1].value))
                date_string = str(row[1])
                #print(str(row[1].value) + " " + str(validate(date_string)))
                date_string_val = date_string.split(" ")
                date_now = date_string_val[0]
                #print(date_now)
            if not row[0]  and not row[6]  and row[2]  and "Summary" not in str(row[6]):
                new_row =[date_now, row[1], row[2], row[5]];
                print("\t".join(new_row)) 
          

if __name__ == '__main__':
    ## description - Text to display before the argument help (default: none)
    parser = argparse.ArgumentParser(add_help=False)                                 
    parser.add_argument('-i', '--id', help='sheet id', required=True) 
    parser.add_argument('-m', '--months', help='months', required=True)
    parser.add_argument('-k', '--keyword', help='keyword', required=True) 
    parser.add_argument('-o', '--output', help='output file', default = "Output_file.tab") 
    options = parser.parse_args()
    gspread(options)
