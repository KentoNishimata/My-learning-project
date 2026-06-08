# My-learning-project-ダウンロードファイル整理アプリ
from pathlib import Path

folder = Path.home()/"Downloads"

for file in folder.iterdir():
    if file.is_file():
        print(file.name,file.suffix)
        extension = file.suffix.replace(".","")
        target_folder=folder/extension
        target_folder.mkdir(exist_ok=True)
        destination=target_folder/file.name
        file.rename(destination)
        print(f"{file.name}を移動")
