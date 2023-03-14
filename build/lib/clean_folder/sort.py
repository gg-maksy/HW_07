import sys
import re
from pathlib import Path
from .dictionary import transliterate

FORMATS = {}
folders_to_del = []


def sorter_folders(root_dir:Path):

    for item in root_dir.glob('**/*.*'):
        get_files(root_dir, item)

    folder_to_del(root_dir)

def folder_to_del(root_dir:Path):

    for item in root_dir.glob('**'):
        folders_to_del.append(item)
    
    del_empty_folders(folders_to_del)

def del_empty_folders(lst:list):

    for item in lst[::-1]:
        try:
            item.rmdir()
        except Exception as e:
            print(e)
    
    get_extention(FORMATS)

def get_extention(dct:dict):

    with open('clean_folder/format.txt', 'r') as fd:
        line = fd.readline()
        while line:

            k = re.search(r'^\w+', line)
            v = re.findall(r'\.\w+', line)
            dct.update({k.group() : v})
            line = fd.readline()

    iter_items(path)

def iter_items(root_dir:Path):
    for file in root_dir.iterdir():
        sort_files(root_dir, file)
    
    

def main():
    try:
        global path
        path = Path(sys.argv[1])
    except IndexError:
        return 'Sorry. No param.'
    
    if not path.exists():
        return 'Sorry, folder not exist'
    
    sorter_folders(path)



def get_files(path: Path, file: Path):
    file.replace(path / transliterate(file.name))
    

def get_key(dictation: dict, file_suffix) -> dict.keys:

    for key, val in FORMATS.items():
            for i in val:
                if file_suffix in i:
                    return key


def sort_files(path: Path, file_name: Path):

    key = get_key(FORMATS, file_name.suffix)
    
    if key:
        fold_i = Path(f'{path}\{key}')
        fold_i.mkdir(exist_ok=True)
        file_name.replace(fold_i / file_name.name)
    else:
        fold_n = Path(f'{path}\\another')
        fold_n.mkdir(exist_ok=True)
        file_name.replace(fold_n / file_name.name)

