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

# Give Title for the page
st.title("My Purchase Register")

# Define UI Fields
purchaseDate = st.date_input("Enter Date of Purchase")
st.write('Date of Purchase is : ', purchaseDate)
purchaseItem = st.text_input("Enter Item purchased: ", max_chars= 150, autocomplete= "purchaseItem")
purchasedFor = st.text_input("Enter Item is purchased for whom: ", max_chars= 150, autocomplete= "purchasedFor")
source = st.text_input("Enter Source of Purchase: ", max_chars=150, autocomplete= "source")
sourceType = st.multiselect('Select the type of source: ' , options= ['Online', 'Offline'], default=['Online'])
addInfo = st.text_input("Enter any additional information:  ", max_chars= 500)
saveButton = st.button('Save Record')


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
    # create empty list and append fields in the list
    mydata = []
    mydata.append(purchaseDate)
    mydata.append(purchaseItem)
    mydata.append(purchasedFor)
    mydata.append(source)
    mydata.append(sourceType)
    mydata.append(addInfo)

    ## For Debugging Purposes
    print(f"Type Purchase Type For: {type(purchaseDate)}")
    print(f" value of the variable source is : {source} ")
    print(f" value of the variable purchaseFor is :  {purchasedFor}")
    print(f" value of the variable purchaseType is : {purchaseItem} ")
    ########## End For Debugging Purposes

    # For insert operation , creating a try except block
    try:
        my_query = "Insert into purchase values (?,?,?,?,?,?)"
        cursor_obj.execute(my_query, mydata)
        my_conn.commit()
        # For showing success message box
        st.success("{} Record inserted successfully".format(purchaseItem))
        print(f" Data committed to Database... {purchaseItem}")

    except sqlite3.OperationalError as error:
        print(f"Record not inserted due to Sqlite3 Operational Error: {error}")

    except sqlite3.NameError as error:
        print(f"Record not inserted due to Sqlite3 Name Error : {error} ")

    except sqlite3.ValueError as error:
        print(f" Failed...Record not inserted due to Sqlite3 Value Error: {error}")

    except sqlite3.InternalError as error:
        print(f"Record not inserted due to Sqlite3 Internal Error: {error}")

    ### End of Try-Except Block #########

    ####### END OF SAVE RECORD FUNCTION ###########################################


    ### Call Save Record Function on Button Click
    if saveButton:
        print("Button Clicked. Calling SaveRecord Function Now")
        saveRecord()


