import mysql.connector
from mysql.connector import Error

class Koneksi :
    def konek(self, query):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bookingfutsal"
        )

        mycursor = mydb.cursor()

        mycursor.execute(query)

        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)

    def readData(self):
        username = "admin"
        password = "admin"
        self.konek("SELECT * FROM admin WHERE username='"+username+"' AND password='"+password+"'")