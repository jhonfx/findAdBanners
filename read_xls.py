import xlrd
import json

book = xlrd.open_workbook("wm_super_madres.xlsx")
print "The number of worksheets is", book.nsheets
print "Worksheet name(s):", book.sheet_names()
sh = book.sheet_by_index(0)
print sh.name, sh.nrows, sh.ncols
print "Cell (2,0) is: ", sh.cell_value(rowx=2, colx=0)
# print sh.cell_value(rowx=2)
response = []
response.append({'impresiones': sh.cell_value(rowx=2, colx=0), 'clicks': sh.cell_value(rowx=2, colx=1)})

for rx in range(sh.nrows):
  # response.append({'impresiones': sh.cell_value(rowx=2, colx=0), 'clicks': sh.cell_value(rowx=2, colx=1)})
  print sh.row(rx)



print json.dumps(response)

# data = {}
# data['asdasdsad', 'qweqwewqe', 'xczxczxc'] = 'value', 'asdasd', '12312'
# json_data = json.dumps(data)

# print json_data