"""
My Purchase Tracker App
"""

# import libraries
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import (
    QGroupBox,
    QLabel,
    QLineEdit,
    QPlainTextEdit,
    QRadioButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
    QApplication,
    QFormLayout,
)
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from pymongo import MongoClient
import sys
import sqlite3

# end import libraries

# open sqlite3 database and collection
# setup database connections
my_conn = sqlite3.connect('purchase.db')
print("Database opened successfully! Proceed further...")
cursor_obj = my_conn.cursor()



# PyQT App declaration
application = QApplication([])
mainWindow = QWidget()
mainWindow.setGeometry(0, 0, 800, 600)
mainWindow.setWindowTitle("Purchase Registry")
formLayout = QFormLayout()

###########Add Gui fields
calendar = QCalendarWidget()
# setting geometry to the calendar
calendar.setGeometry(10, 10, 400, 250)
purchaseDate = QLabel('Purchase Date')
purchaseDateField = QDate.currentDate()
purchaseDateStr = purchaseDateField.toString()

# calendar.setSelectedDate(purchaseDateField)
purchaseType = QLabel('Type of Purchase')
purchaseTypeField = QLineEdit()
purchaseTypeStr = str(purchaseTypeField.text())
print(purchaseTypeStr)
purchasedFor = QLabel("Purchased For")
purchasedForField = QLineEdit()
purchasedForStr = str(purchasedForField.text())
print(purchasedForStr)
source = QLabel('Source of Purchase')
sourceField = QLineEdit()
sourceStr = str(sourceField.text())
print(sourceStr)
addInfo = QLabel('Additional Information')
addInfoField = QLineEdit()
addInfoStr = str(addInfoField.text())
print(f"Type Purchase Type For: {type(purchaseTypeStr)}")

############### End UI Fields

#### Insert data in MongoDB
def saveRecord():


    mydata = (purchaseDateStr,purchaseTypeStr,purchasedForStr,sourceStr,addInfoStr)
    my_query = "Insert into purchase values (?,?,?,?,?)"
    cursor_obj.execute(my_query, mydata)
    my_conn.commit()
    print("Data committed to Database...")



# Save Button
saveButton = QPushButton("Save")
saveButton.clicked.connect(saveRecord)





# Add fields in Form Layout
formLayout.addWidget(calendar)
#formLayout.addRow(purchaseDate, purchaseDateField)
#formLayout.addWidget(purchaseDateField)
formLayout.addRow(purchaseType, purchaseTypeField)
formLayout.addRow(purchasedFor, purchasedForField)
formLayout.addRow(source, sourceField)
formLayout.addRow(addInfo, addInfoField)
formLayout.addWidget(saveButton)

#### Insert data in MongoDB





mainWindow.setLayout(formLayout)
mainWindow.show()
#saveRecord()

application.exec()
my_conn.close()
