python test2.py Timesheet_2020.xlsx Jan,Feb,Mar,April,May,Jun |grep 'Zhang'


python extract_keyword_date.py  data/Timesheet_2019_googlesheet.xlsx Jan,Feb,Mar,April,May,Jun,Jul,Aug,Sept,Oct,Nov,Dec scRNA  > data/Timesheet_2019_scRNA.tsv 

python extract_keyword_date.py  data/Timesheet_2020_July20_2020.xlsx Jan,Feb,Mar,April,May,Jun scRNA  > data/Timesheet_2020_July20_2020_scRNA.tsv

 perl  tab2xlsx_mul.pl data/Timesheet_2019_scRNA.tsv,data/Timesheet_2020_July20_2020_scRNA.tsv 2019,2020 data/Timesheet_2019_2020_scRNA.xlsx

