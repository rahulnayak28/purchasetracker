"""
My Purchase Tracker App
"""

#import libraries
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

#end import libraries

# open Mongodb database and collection
try:
	myclient = MongoClient("mongodb://localhost:27017/")
	print("Connected successfully!")
except:
	print("Could not connect to MongoDB")

db = myclient['mydb']
print("Database mydb assigned...")

mycollection = db['purchase']
print("Collection purchase assigned...")

######## end try block

#PyQT App declaration
application = QApplication([])
mainWindow = QWidget()
mainWindow.setGeometry(0,0,800,600)
mainWindow.setWindowTitle("Purchase Registry")
formLayout = QFormLayout()

###########Add Gui fields
calendar = QCalendarWidget()
# setting geometry to the calendar
calendar.setGeometry(10, 10, 400, 250)
purchaseDate = QLabel('Purchase Date')
purchaseDateField = QDateEdit()
#calendar.setSelectedDate(purchaseDateField)
purchaseType = QLabel('Type of Purchase')
purchaseTypeField = QLineEdit()
purchasedFor = QLabel("Purchased For")
purchasedForField = QLineEdit()
source = QLabel('Source of Purchase')
sourceField = QLineEdit()
addInfo = QLabel('Additional Information')
addInfoField = QPlainTextEdit()
btns = QDialogButtonBox()
btns.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Save)

############### End UI Fields

#Add fields in Form Layout
formLayout.addWidget(calendar)
formLayout.addRow(purchaseDate, purchaseDateField)
formLayout.addRow(purchaseType, purchaseTypeField)
formLayout.addRow(purchasedFor, purchasedForField)
formLayout.addRow(source, sourceField)
formLayout.addRow(addInfo, addInfoField)
formLayout.addWidget(btns)






mainWindow.setLayout(formLayout)
mainWindow.show()

application.exec()