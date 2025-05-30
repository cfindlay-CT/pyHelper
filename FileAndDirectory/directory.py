import os

def list_files_by_folder(path):
    contents = {}
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            contents[entry] = list_files_by_folder(full_path)
        else:
            contents.setdefault('files', []).append(full_path)
    return contents

