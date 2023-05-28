# import libraries
import sys
import sqlite3
import streamlit as st

##### end import libraries

# open sqlite3 database and collection
# setup database connections
my_conn = sqlite3.connect('purchase.db')
print("Database opened successfully! Proceed further...")
cursor_obj = my_conn.cursor()


class Record:
    def __init__(self, purchaseDate, purchaseItem, purchasedFor, source, sourceType, addInfo):
        self.purchaseDate = purchaseDate
        self.purchaseItem = purchaseItem
        self.purchasedFor = purchasedFor
        self.source = source
        self.sourceType = sourceType
        self.addInfo = addInfo


# Give Title for the page
st.set_page_config(page_title="Purchase Register", page_icon="🚀")


# st.title("My Purchase Register")


def saveRecord(a):
    """
    This is the function where data is inserted into Sqlite 3 DB.


    """

    # For insert operation , creating a try except block
    try:
        cursor_obj.execute(
            "Insert into purchase values (:purchaseDate,:purchaseItem,:purchasedFor,:source, :sourceType,:addInfo)",
            {'purchaseDate': a.purchaseDate, 'purchaseType': a.purchaseItem, 'purchaseFor': a.purchasedFor,
             'source': a.source, 'sourceType': a.sourceType, 'addInfo': a.addInfo})
        # cursor_obj.execute(my_query, mydata)
        my_conn.commit()
        # For showing success message box
        st.success("{} Record inserted successfully".format(purchaseItem))
        print(f" Data committed to Database... {purchaseItem}")

    except sqlite3.OperationalError as error:
        print(f"Record not inserted due to Sqlite3 Operational Error: {error}")

    except sqlite3.InternalError as error:
        print(f"Record not inserted due to Sqlite3 Internal Error: {error}")

    ### End of Try-Except Block #########

    ####### END OF SAVE RECORD FUNCTION ###########################################


# Define UI Fields
purchaseDate = st.date_input("Enter Date of Purchase")
st.write('Date of Purchase is : ', purchaseDate)
purchaseItem = st.text_input("Enter Item purchased: ", max_chars=150, autocomplete="purchaseItem")
purchasedFor = st.text_input("Enter Item is purchased for whom: ", max_chars=150, autocomplete="purchasedFor")
source = st.text_input("Enter Source of Purchase: ", max_chars=150, autocomplete="source")
sourceType = st.multiselect('Select the type of source: ', options=['Online', 'Offline'], default=['Online'])
addInfo = st.text_input("Enter any additional information:  ", max_chars=500)
saveButton = st.button(label='Save Record')
### Call Save Record Function on Button Click
if saveButton:
    try:
        # create empty list and append fields in the list
        mydata = Record(purchaseDate,purchaseItem,purchasedFor,source,sourceType,addInfo)
        saveRecord(mydata)
        st.success(f"{purchaseItem} is saved to the database")
    except Exception as e:
        st.warning(f"Error in saving the record. please check & try again {e}")

############### End UI Fields


#### Insert data in SQlite 3 DB ################
### Start of saveRecord Function ###########################
