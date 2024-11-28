import sqlite3

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    def open(self):
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            print("Database connected successfully!")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def create_tables(self):
        if self.cursor:
            try:
                self.cursor.execute("""
                    CREATE TABLE utilizatori (ID INTEGER PRIMARY KEY AUTO_INCREMENT,
                    nume TEXT NOT NULL,email TEXT UNIQUE NOT NULL,parola TEXT NOT NULL,
                    rol TEXT NOT NULL CHECK (rol IN ('client', 'sofer', 'administrator')),
                    data_creare TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );

                    )
                """)
                self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS materiale_de_constructii (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        nume TEXT NOT NULL,
                        pret REAL NOT NULL,
                        descriere TEXT,
                        stoc INTEGER NOT NULL
                    )
                """)
                self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS comenzi (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        utilizator_id INTEGER,
                        detalii TEXT,
                        status TEXT,
                        FOREIGN KEY (utilizator_id) REFERENCES utilizatori(ID)
                    )
                """)
                self.connection.commit()
                print("Tables created successfully!")
            except sqlite3.Error as e:
                print(f"Error creating tables: {e}")
        else:
            print("Connection is not open!")

    def close(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed.")
