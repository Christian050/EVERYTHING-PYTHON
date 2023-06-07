from Packages.XlsxSheetAutomation import *


# Code should look like this


# Code('weather.xlsx', 'Sheet2').ProcessWorkbook((5, 6), 6).DrawChart(5, 6)

# OR

# data = Code('weather.xlsx', 'Sheet2').ProcessWorkbook((5, 6), 6)
# chart = data.DrawChart(5, 6)

Code('Spreadsheets/transactions.xlsx', 'Sheet1').ProcessWorkbook(3)