import pandas as pd


print("編集対象のファイル名指定してください")
target_file = input('')

with pd.ExcelFile(target_file) as xls:
    sheets = xls.sheet_names

    print("どのシートを編集しますか？")
    print(sheets)
    sheet_num = int(input(''))

    edit_target = xls.parse(sheets[sheet_num])

    print(edit_target)