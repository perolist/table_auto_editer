import openpyxl
# import pandas as pd

df = openpyxl.load_workbook('sample.xlsx')

ws = df["sheet1"]

ws2 = df.worksheets[0]

print(ws)