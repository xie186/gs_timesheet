import gspread

gc = gspread.service_account()

sh = gc.open("Timesheet_2020")

print(sh.sheet1.get('Jan'))
