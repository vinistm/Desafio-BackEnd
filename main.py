from utils.CNAB_database import insert_values
from utils.cnba import read_text

FILEPATH = "CNAB.txt"

def main():
    try:
        data = read_text(FILEPATH)
        insert_values(data)   
        
    except(FileNotFoundError):
        print("file not found")    

if __name__ == "__main__":
    main()    
  