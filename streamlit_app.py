import streamlit
streamlit.title( 'MY PARANTS NEW HEALTHY DINER')
streamlit.header( 'BREAKFAST MENU')
streamlit.text( 'OMEGA 3 & BLUEBERRY OATMEAL')
streamlit.text( 'KALE, SPINACH & ROCKET SMOOTHIE')
streamlit.text( 'HARD-BOILED FREE RANGE EGG')
               
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

inport pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
