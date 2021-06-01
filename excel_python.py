import xlrd
loc = ("C:\\Users\\Mr Madhusudhan\\OneDrive\\Desktop\\python-with-IIT\\Book1.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
print(sheet.ncols)
print(sheet.nrows)
for i in range(sheet.ncols):
    print(sheet.cell_value(0,i))
for i in range(sheet.ncols):
    print(sheet.cell_value(i,0))
