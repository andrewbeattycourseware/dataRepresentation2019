import mysql.connector
class BookDAO:
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        #user="datarep",  # this is the user name on my mac
        #passwd="password" # for my mac
        database="datarepresentation"
        )
    
            
    def create(self, values):
        cursor = self.db.cursor()
        sql="insert into book (title,author, price) values (%s,%s,%s)"
        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from book"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))

        return returnArray

    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from book where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)

    def update(self, values):
        cursor = self.db.cursor()
        sql="update book set title= %s,author=%s, price=%s  where id = %s"
        cursor.execute(sql, values)
        self.db.commit()
    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from book where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.db.commit()
        print("delete done")

    def convertToDictionary(self, result):
        colnames=['id','Title','Author', "Price"]
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
        
bookDAO = BookDAO()