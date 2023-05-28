# import libraries
import json

import streamlit as st
from tinydb import TinyDB
from tinydb import Query
from tinydb import *
import pandas as pd
import json

# End of library imports

#Setup DB connection
db = TinyDB("purchase.json")
db_data = db.all()
myQuery = Query()

# Give Title for the page
st.set_page_config(page_title="Purchase Register", page_icon="🚀")

# Define UI Fields for Add purchase Record screen
radio_option = st.sidebar.radio("Menu", options=["Add Purchase Record", "Show Purchases", "Delete Record"])

if radio_option == "Add Purchase Record":
    st.subheader("Add new Purchase Entry")
    purchaseDate = st.date_input("Enter Date of Purchase")
    st.write('Date of Purchase is : ', purchaseDate)
    purchaseItem = st.text_input("Enter Item purchased: ", max_chars=150, autocomplete="purchaseItem")
    purchasedFor = st.text_input("Enter Item is purchased for whom: ", max_chars=150, autocomplete="purchasedFor")
    source = st.text_input("Enter Source of Purchase: ", max_chars=150, autocomplete="source")
    sourceType = st.multiselect('Select the type of source: ', options=['Online', 'Offline'], default=['Online'])
    addInfo = st.text_input("Enter any additional information:  ", max_chars=500)


###Facing error as Object of type date is not JSON serializable. To solve the error
    purchaseDate = json.dumps(purchaseDate, indent=4, default=str)

    saveButton = st.button(label='Save Record')
    if saveButton:
        try:
            new_item = {"purchaseDate": purchaseDate, "purchaseItem": purchaseItem, "purchasedFor": purchasedFor,
                        "source": source, "sourceType": sourceType, "addInfo": addInfo}
            db.insert(new_item)
            st.success(f"Item --> {purchaseItem} is saved to the database")
            st.empty() ## For clearing the screen

        except Exception as e:
            st.warning(f"Error in saving the record. please check & try again {e}")

##### End of UI Fields definition for Add Purchase Record screen

if radio_option == "Show Purchases":
    db_data = db.all()

    type(db_data)
    ## Expected type 'str', got 'List[Document]' instead. To Solve, convert the db record into df
    df = pd.DataFrame(db_data, columns= ['purchaseDate', 'purchaseItem', 'purchasedFor','source','sourceType',
                                                                                                 'addInfo'])


    st.table(df)


   # st.json(get, expanded= True)

if radio_option == 'Delete Record':
    st.subheader('Remove an entry from the database')
    purchaseItem = st.text_input('Enter the item that needs to be removed', autocomplete='purchaseItem')
    deleteButton = st.button(label='Delete Record')
    if deleteButton:
        try:
            db.remove(myQuery.purchaseItem == 'purchaseItem')
            st.warning(f'Item Record {purchaseItem} has been deleted from the database!')
        except Exception as e:
            print(f"Not able to Delete the record because of an Exception --> {e}")
            st.error(f"Not able to Delete the record because of an Exception --> {e}")




















