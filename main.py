from utils.CNAB_database import insert_values
from utils.cnba import read_text

FILEPATH = "CNAB.txt"

# teste = [1,20200510,1431111,17307329913,"4253*****2236",141020,"VINICIUS MARTINS","CENTRINHO"]
def main():
    try:
        data = read_text(FILEPATH)
        insert_values(data)   
        
    except(FileNotFoundError):
        print("file not found")    

if __name__ == "__main__":
    main()    
    # insert_values(teste)