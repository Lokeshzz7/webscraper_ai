import streamlit as st

st.title("Web Scraper")

url = st.text_input("Enter the url")

if st.button("Scrape"):
    st.write("Running")
