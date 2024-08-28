import os
import shutil

def prepare_data(source_folder, dest_folder):
    """Prepare data by copying from source to destination folder."""
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    for item in os.listdir(source_folder):
        s = os.path.join(source_folder, item)
        d = os.path.join(dest_folder, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, False, None)
        else:
            shutil.copy2(s, d)

if __name__ == "__main__":
    prepare_data('data/raw/', 'data/processed/')