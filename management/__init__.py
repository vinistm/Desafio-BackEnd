from utils.database import insert_table
from utils.read import read_file
import os.path

pythonfile = 'db.sqlite3'
file_path = os.path.isfile(pythonfile)
FILEPATH = "upload/CNAB.txt"

if file_path == True:
    try:
        data = read_file(FILEPATH)
        insert_table(data)
        print("File found successfully")
    except(FileNotFoundError):
            print("File not found")