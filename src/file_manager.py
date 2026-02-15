import os
import shutil

def upload_file(src_path, dest_folder="data/files/"):
    if not os.path.exists(src_path):
        return False

    filename = os.path.basename(src_path)
    shutil.copy(src_path, dest_folder + filename)
    return True