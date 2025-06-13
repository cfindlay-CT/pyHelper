import os
import time

def list_files_by_folder(path):
    contents = {}
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            contents[entry] = list_files_by_folder(full_path)
        else:
            contents.setdefault('files', []).append(full_path)
    return contents

def create_snapshot(root, include_extensions=None, skip_dirs=None, output_dir="."):
    if include_extensions:
        include_extensions = [ext.lower() for ext in include_extensions]
    if skip_dirs is None:
        skip_dirs = []

    timestamp = int(time.time())
    output_file = os.path.join(output_dir, f"snapshot_{timestamp}.txt")

    with open(output_file, "w", encoding="utf-8") as out:
        for dirpath, dirnames, filenames in os.walk(root):
            if any(skip in dirpath for skip in skip_dirs):
                continue

            for filename in filenames:
                if include_extensions and not any(filename.lower().endswith(ext) for ext in include_extensions):
                    continue

                file_path = os.path.join(dirpath, filename)
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        out.write(f"\n--- FILE: {file_path} ---\n")
                        out.write(f.read())
                        out.write("\n")
                except Exception as e:  
                    out.write(f"\n--- FILE: {file_path} (Could not read: {e}) ---\n")

    print(f"Snapshot saved to {output_file}")


