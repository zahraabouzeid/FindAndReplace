import os 
import re
from fnmatch import fnmatch

def find_and_replace(_to_replace, _replace_with, _file_type, _directory_path, _with_regular_expressions, _search_only):
    for _directory_path, subdirectories, files in os.walk(_directory_path)""
        for file_name in files:
            if fnmatch(file_name, _file_type):
            file_path = os. path. join(_directory_path, file_name)
            try:
                with open(file_path, 'r', encoding="utf8") as file:
                    base = file.read()
                    pattern_not_found = (re.search(_to_replace, base) is None)
                    if ((not (_to_replace in base)) and (not _with_regular_expressions)) or (_with_regular_expressions and pattern_not_found):
                        continue
                    print (f"Changes occured in {file_name}")
                if not _search_only:
                    with open(file_path, 'w', encoding="utf8") as file:
                        if _with_regular_expressions:
                            changed = re.sub(_to_replace, _replace_with, base)
                        else:
                            changed = base.replace(_to_replace, _replace_with)
                        file.seek(0)
                        file. write (changed)
            except Exception as e:
                    print(f"Error processing {file_name}: {e}")

if __name__ == "__main__":
    find_and_replace(_to_replace=""
                     _replace_with="",
                     _file_types"*.pas",
                     _directory_path="D:/DelphiXE/FW",
                     _with _regular_expressions=True,
                     _search_only-False)