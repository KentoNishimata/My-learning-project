from pathlib import Path

folder = Path.home()/"Downloads"
def should_skip(file):
    if file.name.startswith("."):
        return True

    extension = file.suffix.replace(".", "")

    if extension == "":
        return True

    return False
def move_file(file, folder):
    extension = file.suffix.replace(".", "")

    target_folder = folder / extension
    target_folder.mkdir(exist_ok=True)

    destination = target_folder / file.name
    file.rename(destination)

    print(f"{file.name}を移動")

for file in folder.iterdir():
    
    if should_skip(file):
        continue
    
    if file.is_file():
         move_file(file, folder)