# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import sys
import datetime
from PyQt6 import uic, QtCore, QtGui, QtWidgets
import requests
from requests .exceptions import HTTPError
import json


class MainWindow(QtWidgets.QMainWindow):
    ServerAddress = "http://localhost:5000"
    MessageID = 0

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('pyQtClient.ui', self)
        self.pushButton1.clicked.connect(self.pushButton1_clicked)

    def pushButton1_clicked(self):
        self.SendMessage();

    def SendMessage(self):
        UserName = self.lineEdit1.text()
        MessageText = self.lineEdit2.text()
        TimeStamp = str(datetime.datetime.today())
        msg = f"{{\"UserName\": \"{UserName}\", \"MessageText\": \"{MessageText}\", \"TimeStamp\": \"{TimeStamp}\"}}"
        print("Message sent: " + msg)
        url = self.ServerAddress + "/api/Messenger"
        data = json.loads(msg)
        r = requests.post(url, json=data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
