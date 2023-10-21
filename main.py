import streamlit as st
import pandas as pd

# st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('images/Kartik.jpg')
    
with col2:
    st.title("Kartik Neti")
    content = """I am GOD"""
    st.info(content)
    
st.subheader("This is a subheader. Feel free to contact me from the email mentioned below.")

col3, col4 = st.columns(2)

df = pd.read_csv('data.csv', sep=';')
with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
    
