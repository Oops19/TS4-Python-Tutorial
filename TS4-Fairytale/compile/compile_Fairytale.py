# compile.sh version 2.0.4

# This file searches from the parent directory for 'modinfo.py' in it or in any sub directory.
# Make sure to have only one 'modinfo.py' in your project directory. The first found 'modinfo.py' is used and loaded.
#
#

# Folder structure:
# PyCharm-Folder/_compile/compile.sh
# PyCharm-Folder/_TS4/mod_data|mod_documentation|Mods/ - These folders will be added to the mod.
# If extracted properly 'mod_data' and 'mod_documentation' will folders next to 'Mods'.
#
# PyCharm-Folder/your-mod-name/modinfo.py and other files and folders to be compiled


import os
import re
import ast
import sys
import shutil
from typing import Tuple, Dict, Any

from Utilities.unpyc3_compiler import Unpyc3PythonCompiler

additional_directories: Tuple = ()
include_sources = False

beta_appendix = "-beta"  # or "-test-build"

modinfo_py = 'modinfo.py'
mi = None
for root, dirs, files in os.walk('..'):
    if modinfo_py in files:
        modinfo = os.path.join(root, modinfo_py)
        print(f"Using '{modinfo}' ...")
        try:
            sys.path.insert(1, root)
            # noinspection PyUnresolvedReferences
            from modinfo import ModInfo
            mi = ModInfo.get()
            print(f"Imported data for '{mi._author}:{mi._name}' from '../{mi._base_namespace}' with version '{mi._version}'")
            try:
                with open(modinfo.replace(".py", ".dict"), 'rt') as fp:
                    cfg: Dict[str, Any] = ast.literal_eval(fp.read())
                    additional_directories = cfg.get('additional_directories', additional_directories)
                    include_sources = cfg.get('include_sources', include_sources)
            except:
                pass
            break
        except Exception as e:
            print(f"Error importing '{modinfo_py}' ({e}).")
        break
if not mi:
    print(f"Error '{modinfo_py}' not found.")
    exit(1)


author = mi._author
mod_name = mi._name
mod_directory = mi._base_namespace
version = mi._version  # All versions 0., x.1, x.3, x.5, x.7, x.9 (also x.1.y, x.1.y.z) will be considered beta and the 'beta_appendix' gets appended.

release_directory = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(os.getcwd()))), 'Release')
mod_base_directory = os.path.join(release_directory, mod_name)
ts4_directory = os.path.join(mod_base_directory, 'Mods', f"_{author}_")


src_folder = os.path.join(os.path.dirname(os.path.abspath(os.getcwd())), '_TS4')
for folder in ['mod_data', 'mod_documentation', 'Mods', 'mod_sources']:
    try:
        if os.path.exists(os.path.join(src_folder, folder)):
            shutil.copytree(os.path.join(src_folder, folder), os.path.join(mod_base_directory, folder))
    except:
        print(f"WARNING: Remove the folder {os.path.join(mod_base_directory, folder)} to update the data.")

zip_file_name = os.path.join(release_directory, f"{mod_name}")
if version:
    zip_file_name = f"{zip_file_name}_v{version}"
    if re.match(r"^(?:0|(?:0|[1-9][0-9]*)\.[0-9]*[13579])(?:\.[0-9]+)*$", version):
        zip_file_name = f"{zip_file_name}{beta_appendix}"


# Add source

if include_sources:
    _mod_src_directory = os.path.dirname(os.path.abspath(os.getcwd()))
    for folder in (mod_directory, ) + additional_directories:
        try:
            shutil.copytree(os.path.join(_mod_src_directory, folder), os.path.join(mod_base_directory, 'mod_sources', mod_name, folder), ignore=shutil.ignore_patterns('__pycache__', '.*'))
        except Exception as e:
            print(f"{e}")
            print(f"WARNING: Remove the folder {os.path.join(mod_base_directory, 'mod_sources', mod_name, folder)} to update the data.")


# Compile
os.makedirs(ts4_directory, exist_ok=True)
print(f"Compiling '{mod_directory}' and {additional_directories} in '{ts4_directory}'")

Unpyc3PythonCompiler.compile_mod(
    names_of_modules_include=(mod_directory, ) + additional_directories,
    folder_path_to_output_ts4script_to=ts4_directory,
    output_ts4script_name=mod_directory
)

shutil.make_archive(os.path.join(release_directory, f"{zip_file_name}"), 'zip', mod_base_directory)
print(f'Created {os.path.join(release_directory, f"{zip_file_name}.zip")}')

'''
v2.0.4
    Moved both settings to modinfo.dict so they are not included in the source / compiled.
v2.0.3
    Add 'include_source = True' to 'modinfo.py' to add also the source.
v2.0.2
    Add 'additional_directories = ('foo', )' to 'modinfo.py' to include also other directories ('foo' in this case).
'''
