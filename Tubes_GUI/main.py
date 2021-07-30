# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from PyQt5 import QtWidgets, uic
import sys
import pymysql

import mysql.connector

class Ui_Login(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_Login, self).__init__()
        uic.loadUi('login.ui', self)

        self.icon = self.findChild(QtWidgets.QLabel, 'ilogin')
        self.icon.setStyleSheet("image: url(sorce/roundicon.png)")

        self.inputUsername = self.findChild(QtWidgets.QLineEdit, 'username')
        self.inputPassword = self.findChild(QtWidgets.QLineEdit, 'password')

        self.daftarButton = self.findChild(QtWidgets.QPushButton, 'daftarBtn')
        self.daftarButton.clicked.connect(self.forDaftar)

        self.loginButton = self.findChild(QtWidgets.QPushButton, 'login_2')
        self.loginButton.clicked.connect(self.testButton)

        self.show()

    def testButton(self):
        user = self.inputUsername.text()
        pw = self.inputPassword.text()
        con = pymysql.connect(db='bookingfutsal',
                              user='root',
                              passwd='',
                              host='localhost',
                              port=3306,
                              autocommit=True)
        cur = con.cursor()
        sql = "SELECT * FROM admin WHERE username=%s AND password=%s"
        data = cur.execute(sql, (user, pw))
        if(len(cur.fetchall()) > 0):
            self.close()

            super(Ui_Login, self).__init__()
            uic.loadUi('booking.ui', self)

            self.gambar = self.findChild(QtWidgets.QLabel, 'piclap')
            self.gambar.setStyleSheet("background-image: url(sorce/lp2.jpg)")

            self.bNamaPembayar = self.findChild(QtWidgets.QLineEdit, 'namapembayar')
            self.bNominalDp = self.findChild(QtWidgets.QLineEdit, 'nominaldp')

            self.bBooking = self.findChild(QtWidgets.QPushButton, 'booking')
            self.bBooking.clicked.connect(self.bookingFunc)

            self.show()


    def forDaftar(self):
        self.close()

        super(Ui_Login, self).__init__()
        uic.loadUi('daftar.ui', self)

        self.dUsername = self.findChild(QtWidgets.QLineEdit, 'username')
        self.dPassword = self.findChild(QtWidgets.QLineEdit, 'password')
        self.dAlamat = self.findChild(QtWidgets.QLineEdit, 'alamat')
        self.dNoTelpU = self.findChild(QtWidgets.QLineEdit, 'notelepon')

        self.dDaftarButton = self.findChild(QtWidgets.QPushButton, 'daftar')
        self.dDaftarButton.clicked.connect(self.daftarFunc)

        self.show()

    def daftarFunc(self):
        user = self.dUsername.text()
        pw = self.dPassword.text()
        con = pymysql.connect(db='bookingfutsal',
                              user='root',
                              passwd='',
                              host='localhost',
                              port=3306,
                              autocommit=True)
        cur = con.cursor()
        insert = (user, pw)
        sql = "INSERT INTO admin (username, password) VALUES" + str(insert)
        data = cur.execute(sql)

        self.close()

        self.__init__();

#        booking.Ui_Booking().Boking()
#       koneksi.Koneksi()

    def bookingFunc(self):
        nama = self.bNamaPembayar.text()
        nominal = self.bNominalDp.text()

        con = pymysql.connect(db='bookingfutsal',
                              user='root',
                              passwd='',
                              host='localhost',
                              port=3306,
                              autocommit=True)
        cur = con.cursor()
        insert = (nama, nominal)
        sql = "INSERT INTO pembayaran (atasNama, namaPembayaran) VALUES" + str(insert)
        data = cur.execute(sql)

app = QtWidgets.QApplication(sys.argv)
window = Ui_Login()
app.exec_()