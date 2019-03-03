import os


def get_extension_file(file_path):
    return os.path.splitext(file_path)[1][1:].strip()
