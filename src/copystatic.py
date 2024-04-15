import os
import shutil

def copy_files_recursive(src, dst):
    if not os.path.exists(dst):
        os.mkdir(dst)

    for item in os.listdir(src):
        src_item_path = os.path.join(src, item)
        dest_item_path = os.path.join(dst, item)

        if os.path.isfile(src_item_path):
            shutil.copy(f"{src}/{item}", dest_item_path)
        else:
            copy_files_recursive(src_item_path, dest_item_path)
