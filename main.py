import streamlit as st
from scraper import scrape

st.title("Web Scraper")

url = st.text_input("Enter the url")

if st.button("Scrape"):
    st.write("Running")
    result = scrape(url)
    print(result)