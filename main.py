import pandas as pd


def add_column(df, column_name):
    df[column_name] = None
    print("列を追加しました")
    print(df)


print("編集対象のファイル名指定してください")
target_file = input('')

with pd.ExcelFile(target_file) as xls:
    sheets = xls.sheet_names

    print("どのシートを編集しますか？")
    print(sheets)
    sheet_num = int(input(''))

    

    edit_target = xls.parse(sheets[sheet_num])

    add_column(edit_target, "好物")

    print(edit_target)