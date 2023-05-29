from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import os


cythonize_folders = ["metrics", "models", "simulator"]
ext_modules = []
split_by = "/"
if os.name != 'posix':
    split_by = "\\"

for folder in cythonize_folders:
    path = os.path.join(".", "src", folder )
    files = list(filter(lambda x: not x.startswith("_") and x[-3::]== ".so", os.listdir(path)))

    for source_file in files:
        # if source_file == "cythonGraphFunctions.cpython-39-x86_64-linux-gnu.so":
        #     print()
        # if exits .pyx do not remove
        pathNo = os.path.join(path, source_file.replace(".cpython-39-x86_64-linux-gnu.so", ".pyx"))
        if os.path.exists(pathNo):
            print("Not removing by {}".format(pathNo))
            continue
        os.remove(os.path.join(path, source_file))