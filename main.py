import pandas as pd
from pathlib import Path

def add_column(df, column_name):
    df[column_name] = None
    print("列を追加しました")
    print(df)

target_path = Path('./')
target_files = list(target_path.glob('*.xlsx'))


print("編集対象のファイル名指定してください")

for i, file in enumerate(target_files):
    print(f"{file} [{i}]")

target_file = int(input(''))


with pd.ExcelFile(target_files[target_file]) as xls:
    sheets = xls.sheet_names
    
    print("どのシートを編集しますか？")
    for sheet_num, sheet_name in enumerate(sheets):
        print(f"{sheet_name} [{sheet_num}]")

    target_sheet = int(input(''))


    edit_target = xls.parse(sheets[target_sheet])

    add_column(edit_target, "好物")

    print(edit_target)