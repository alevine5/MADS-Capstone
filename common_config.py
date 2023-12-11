# common_config.py
import os

# set a standard directory for each notebook
default_working_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
os.chdir(default_working_directory)
