import streamlit as st

# Example usage with a unique key generated using the widget's content
options = ["Option 1", "Option 2", "Option 3"]
unique_key = hash(tuple(options))  # Generate a unique key based on the options
selected_options = st.multiselect("Select options:", options, key=unique_key)

# Use 'selected_options' in your application logic
# ...

 import streamlit
streamlit.title( 'MY PARANTS NEW HEALTHY DINER')
streamlit.header( 'BREAKFAST MENU')
streamlit.text( 'OMEGA 3 & BLUEBERRY OATMEAL')
streamlit.text( 'KALE, SPINACH & ROCKET SMOOTHIE')
streamlit.text( 'HARD-BOILED FREE RANGE EGG')
               
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), key = 'Lime')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# Let's put a pick list here so they can pick the fruit they want to include 

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]   
# Display the table on the page.
streamlit.dataframe(fruits_to_show)



