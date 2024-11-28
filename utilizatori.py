from database import DATABASE
import random

class UTILIZATORI:
    
    def __init__(self):
        self.database=DATABASE("data_base.db")
        
    def adauga_clienti(self, clienti, soferi, administratori):
        self.database.open_data_base()
        id_uri=[]
        ID=random.randint(1000, 100000)
        self.database.cursor.execute("SELECT ID FROM utilizatori")
        id_utilizator=self.database.cursor.fetchall()
        id_uri.append(id_utilizator)
        if ID not in id_uri:
            self.database.cursor.execute("INSERT INTO utilizatori (ID, soferi, administratori, clienti) VALUES (?, ?, ?, ?)", (ID, soferi, administratori, clienti,))
            self.database.conexiune.commit()
            print("Utilizator adaugat cu succes.")
        else:
            print("ID-ul nu este valabil.")
        self.database.close_data_base()
            
    def sterge_utilizator(self, ID):
        self.database.open_data_base()
        self.database.cursor.execute("SELECT ID FROM utilizatori")
        id_utilizator=self.database.cursor.fetchall()
        id_validation=False
        if id_utilizator is not None:
            id_validation=True
            if id_validation:
                self.database.cursor.execute("DELETE FROM utilizatori WHERE ID=?", (ID,))
                self.database.conexiune.commit()
                print("Utilizator sters.")
                
        else:
            print("MISSING ID!")
        
                
                

utlizator=UTILIZATORI()
# utlizator.adauga_utilizatori("Marian", "Marian", "-")
utlizator.sterge_utilizator(74606)
                
                
                
    