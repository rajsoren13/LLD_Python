class Database_connection:
    _instance=None
    def __new__(cls):
        #check if instance is already exist
        if cls._instance is None: 
            cls._instance=super().__new__(cls)
            print("Database connection created")
        return cls._instance


db1=Database_connection()
db2=Database_connection()
db3=Database_connection()
print(db1 is db2)
print(db2 is db3)
