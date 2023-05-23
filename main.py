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
from PyQt5 import QtCore, QtGui, QtWidgets
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
purchaseType = QLabel('Item Purchased')
purchaseTypeField = QLineEdit()

purchasedFor = QLabel("Purchased For")
purchasedForField = QLineEdit()
#purchasedForStr = str(purchasedForField.text())


source = QLabel('Source of Purchase')
sourceField = QLineEdit()
#sourceStr = str(sourceField.text())


addInfo = QLabel('Additional Information')
addInfoField = QLineEdit()
#addInfoStr = str(addInfoField.text())



############### End UI Fields

#### Insert data in SQlite 3 DB ################
### Start of saveRecord Function ###########################
def saveRecord():
    """
    This is the function where data is inserted into Sqlite 3 DB.
    There is a need to fetch the text from QlineEdit elements and then converting into string format as Sqlite3 is not
    compatible with QlineEdit Data types and other PyQT5 widgets. hence all the elements are required to be converted
    first before inserting into the DB

    """
    #mydata = (purchaseDateStr,purchaseTypeStr,purchasedForStr,sourceStr,addInfoStr)
    purchaseTypeStr = purchaseTypeField.text()
    purchasedForStr = purchasedForField.text()
    sourceStr = sourceField.text()
    addInfoStr = addInfoField.text()

# create empty list and append fields in the list
    mydata = []

    mydata.append(purchaseDateStr)
    mydata.append(purchaseTypeStr)
    mydata.append(purchasedForStr)
    mydata.append(sourceStr)
    mydata.append(addInfoStr)


    ## For Debugging Purposes
    print(f"Type Purchase Type For: {type(purchaseTypeStr)}")
    print(f" value of the variable sourceStr is : {sourceStr} ")
    print(f" value of the variable purchaseForStr is :  {purchasedForStr}")
    print(f" value of the variable purchaseTypeStr is : {purchaseTypeStr} ")
    ########## For Debugging Purposes

    try:
        my_query = "Insert into purchase values (?,?,?,?,?)"
        cursor_obj.execute(my_query, mydata)
        my_conn.commit()
    # For showing success message box
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Record Saved Successfully")
        msg.setWindowTitle("Information")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()
        ### End message box

        print("Data committed to Database...")

## To Clear screen data from fields once data is saved into the database
        purchaseTypeField.setText("")
        purchasedForField.setText("")
        sourceField.setText("")
        addInfoField.setText("")
        print("Data Cleared from the screen...")

    except sqlite3.OperationalError as error:
        print(f"Record not inserted due to Sqlite3 Operational Error: {error}")
    except sqlite3.NameError as error:
        print(f"Record not inserted due to Sqlite3 Name Error : {error} ")
    except sqlite3.ValueError as error:
        print(f"Record not inserted due to Sqlite3 Value Error: {error}")
    except sqlite3.InternalError as error:
        print(f"Record not inserted due to Sqlite3 Internal Error: {error}")


####### END OF SAVE RECORD FUNCTION ###########################################




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






mainWindow.setLayout(formLayout)
mainWindow.show()
#saveRecord()

application.exec()
my_conn.close()
