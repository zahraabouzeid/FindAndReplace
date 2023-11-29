import os 
import re
import shutil
from fnmatch import fnmatch

def find_and_replace(_to_replace, _replace_with, _file_type, _directory_path, 
                    _with_regular_expressions, _search_only, _copy_files, _destination_path):
    total = 0
    for _directory_path, subdirectories, files in os.walk(_directory_path):
        for file_name in files:
            if fnmatch(file_name, _file_type):
                file_path = os.path.join(_directory_path, file_name)
                try:
                    with open(file_path, 'r', encoding="utf8") as file:
                        base = file.read()
                        occurrences = base.count(_to_replace)
                        if _with_regular_expressions:
                            occurrences = len(re.findall(_to_replace, base))
                        if occurrences == 0:
                            continue
                        print (f"Occurences in {file_name}: {occurrences}")
                        if  _copy_files:
                            shutil.copy(file_path, os.path.join(_destination_path, file_name))
                        total += 1
                    if not _search_only:
                        with open(file_path, 'w', encoding="utf8") as file:
                            if _with_regular_expressions:
                                changed = re.sub(_to_replace, _replace_with, base)
                            else:
                                changed = base.replace(_to_replace, _replace_with)
                            file.seek(0)
                            file. write (changed)
                except Exception as e:
                        print(f"Error processing {file_name}")
    print(f"\n{total} Result(s) Found")

if __name__ == "__main__":
    find_and_replace(_to_replace="",
                     _replace_with="",
                     _file_type="*.pas",
                     _directory_path="D:/DelphiXE/FW",
                     _with_regular_expressions=False,
                     _search_only=False,
					 _copy_files=True,
					 _destination_path="D:/DelphiXE")